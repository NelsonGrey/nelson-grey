#!/usr/bin/env python3
"""Static checks for the website and repo config. Standard library only.

Checks every deployed HTML page (repo root and games/*) for: <html lang>, <title>, viewport,
meta description, and that local links, scripts, stylesheets, and images resolve to files.
Also validates the JSON config files.
Run from the repository root: python3 scripts/check-site.py
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT
SKIP = {"node_modules", "marketing", "output", "artifacts", ".git", ".github", ".playwright-cli", ".firebase"}
JSON_FILES = [".firebaserc", *(p.name for p in ROOT.glob("firebase*.json"))]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = False
        self.title = False
        self.viewport = False
        self.description = False
        self.refs = []
        self.canonical = None
        self.og_url = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html" and a.get("lang"):
            self.lang = True
        if tag == "title":
            self.title = True
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "meta":
            if a.get("name") == "viewport":
                self.viewport = True
            if a.get("name") == "description" and a.get("content"):
                self.description = True
            if a.get("property") == "og:url":
                self.og_url = a.get("content")
        for attr in ("href", "src"):
            if tag in ("a", "link", "script", "img", "source") and a.get(attr):
                self.refs.append(a[attr])


def local_target(site: Path, page: Path, ref: str):
    parsed = urlparse(ref)
    if parsed.scheme or parsed.netloc or ref.startswith(("#", "mailto:", "tel:", "data:")):
        return None
    path = parsed.path
    if not path:
        return None
    base = site if path.startswith("/") else page.parent
    target = (base / path.lstrip("/")).resolve()
    if target.is_dir():
        target = target / "index.html"
    return target


APP_STORE = "https://apps.apple.com/us/app/modulo-squares/id6783995654"
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def trailing_slash_url(url: str) -> bool:
    path = urlparse(url).path or ""
    return path != "/" and path.endswith("/")


def check_sitemap() -> list[str]:
    path = ROOT / "sitemap.xml"
    if not path.is_file():
        return ["sitemap.xml: missing"]
    errors = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"sitemap.xml: invalid XML ({exc})"]
    locs = [(node.text or "").strip() for node in root.findall("sm:url/sm:loc", SITEMAP_NS)]
    if "https://nelsongrey.com/games" not in locs:
        errors.append("sitemap.xml: missing https://nelsongrey.com/games")
    for loc in locs:
        if trailing_slash_url(loc):
            errors.append(f"sitemap.xml: trailing slash in {loc}")
    return errors


def check_modulo_squares() -> list[str]:
    errors = []
    directory = ROOT / "games" / "modulo-squares"
    for page in sorted(directory.glob("*.html")):
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(ROOT)
        if 'name="apple-itunes-app"' not in text or "app-id=6783995654" not in text:
            errors.append(f"{rel}: missing apple-itunes-app app-id=6783995654")
        if "aggregateRating" in text:
            errors.append(f"{rel}: do not add aggregateRating")
        if re.search(r"\bnine buckets\b", text, re.I):
            errors.append(f"{rel}: still says nine buckets")
        if "Remove Ads" in text:
            errors.append(f"{rel}: still calls the purchase Remove Ads")
        for match in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            try:
                data = json.loads(match.group(1))
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD ({exc})")
                continue
            if data.get("@type") != "MobileApplication" or data.get("name") != "Modulo Squares":
                continue
            offers = data.get("offers") or {}
            if str(offers.get("price")) not in {"0", "0.0", "0.00"} or offers.get("priceCurrency") != "USD":
                errors.append(f"{rel}: MobileApplication offers must be price 0 USD")
            if data.get("url") != APP_STORE or data.get("sameAs") != APP_STORE:
                errors.append(f"{rel}: MobileApplication url and sameAs must point at the App Store listing")
    return errors


def main() -> int:
    errors = []
    pages = 0
    site = SITE
    if True:
        for page in sorted(p for p in site.rglob("*.html") if not SKIP & set(p.relative_to(ROOT).parts)):
            pages += 1
            rel = page.relative_to(ROOT)
            parser = Page()
            parser.feed(page.read_text(encoding="utf-8"))
            for ok, label in ((parser.lang, "<html lang>"), (parser.title, "<title>"), (parser.viewport, "viewport meta")):
                if not ok:
                    errors.append(f"{rel}: missing {label}")
            if page.name != "404.html" and not parser.description:
                errors.append(f"{rel}: missing meta description")
            for ref in parser.refs:
                parsed_ref = urlparse(ref)
                if not parsed_ref.scheme and not parsed_ref.netloc and parsed_ref.path.endswith(".html"):
                    errors.append(f"{rel}: use a clean URL instead of {ref!r}")
                target = local_target(site, page, ref)
                if target is None:
                    continue
                if not target.exists():
                    # clean URLs: /about resolves to about.html
                    clean = target.with_name(target.name + ".html") if not target.suffix else target
                    if not clean.exists():
                        errors.append(f"{rel}: broken local reference {ref!r}")
            for label, url in (("canonical", parser.canonical), ("og:url", parser.og_url)):
                if url and trailing_slash_url(url):
                    errors.append(f"{rel}: {label} should not use a trailing slash ({url})")
    if not (ROOT / "404.html").is_file():
        errors.append("404.html: missing custom 404 page")
    errors.extend(check_sitemap())
    errors.extend(check_modulo_squares())
    for name in JSON_FILES:
        path = ROOT / name
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{name}: invalid JSON ({exc})")
                continue
            hosting = data.get("hosting") if isinstance(data, dict) else None
            if isinstance(hosting, dict):
                for rewrite in hosting.get("rewrites") or []:
                    if rewrite.get("destination") == "/index.html":
                        errors.append(f"{name}: rewrite to /index.html serves the homepage for unknown URLs")
    if pages == 0:
        errors.append("no HTML pages found ")
    for line in errors:
        print(f"ERROR {line}")
    print(f"checked {pages} pages, {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
