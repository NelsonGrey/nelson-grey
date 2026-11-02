#!/usr/bin/env python3
"""Validate Nelson Grey developer-profile deliverables and write the asset manifest."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys
import tempfile
from xml.etree import ElementTree as ET

from PIL import Image, ImageChops


KIT_ROOT = Path(__file__).resolve().parent
REPO_ROOT = KIT_ROOT.parents[1]
MANIFEST_PATH = KIT_ROOT / "asset-manifest.csv"
AUTHORITATIVE_TOUCH_ICON = REPO_ROOT / "assets/apple-touch-icon.png"
AUTHORITATIVE_CORE_SOURCE = REPO_ROOT / "assets/nelson-grey-mark.svg"
CORE_ICON_SOURCE = KIT_ROOT / "sources/nelson-grey-brand-icon.svg"
DEVELOPER_ICON_SOURCE = KIT_ROOT / "sources/nelson-grey-developer-icon.svg"
ACCOUNT_OWNER_EMAIL = "marknelson@nelsongrey.com"
PUBLIC_CONTACT_EMAIL = "support@nelsongrey.com"
# Keep this split so the validator can scan its own source for the deprecated
# address without matching the guardrail definition itself.
DEPRECATED_CONTACT_EMAIL = "nelson." + "gre.arc@gmail.com"
RETIRED_BRAND_PHRASES = (
    "Thoughtful " + "apps. Playful systems.",
    "Focused software for everyday life, " + "curious minds, and things worth keeping.",
    "A studio for useful ideas and " + "playful systems.",
    "Independent " + "software studio",
)
TEXT_FILE_SUFFIXES = {".csv", ".md", ".py", ".sh", ".svg", ".txt"}


@dataclass(frozen=True)
class ExpectedImage:
    relative_path: str
    width: int
    height: int
    allowed_formats: tuple[str, ...] = ("PNG",)
    alpha: bool | None = None


EXPECTED_IMAGES = (
    ExpectedImage("google/developer-icon-512x512.png", 512, 512, alpha=True),
    ExpectedImage("google/developer-header-4096x2304.png", 4096, 2304, alpha=False),
    ExpectedImage("google/developer-header-4096x2304.jpg", 4096, 2304, ("JPEG",), False),
    ExpectedImage("google/developer-profile-preview-1600x1200.png", 1600, 1200, alpha=False),
    ExpectedImage("brand/nelson-grey-mark-1024x1024.png", 1024, 1024, alpha=True),
    ExpectedImage("brand/nelson-grey-developer-mark-1024x1024.png", 1024, 1024, alpha=True),
    ExpectedImage("brand/nelson-grey-mark-on-light-1024x1024.png", 1024, 1024, alpha=True),
    ExpectedImage("brand/nelson-grey-mark-reverse-1024x1024.png", 1024, 1024, alpha=True),
    ExpectedImage("brand/nelson-grey-mark-mono-ink-1024x1024.png", 1024, 1024, alpha=True),
    ExpectedImage("brand/nelson-grey-mark-mono-white-1024x1024.png", 1024, 1024, alpha=True),
    ExpectedImage("brand/nelson-grey-wordmark-primary-2200x620.png", 2200, 620, alpha=True),
    ExpectedImage("brand/nelson-grey-wordmark-primary-reverse-2200x620.png", 2200, 620, alpha=True),
    ExpectedImage("brand/nelson-grey-stacked-lockup-1400x1600.png", 1400, 1600, alpha=False),
    ExpectedImage("brand/nelson-grey-brand-board-1920x1080.png", 1920, 1080, alpha=False),
    ExpectedImage("brand/nelson-grey-core-developer-board-1920x1080.png", 1920, 1080, alpha=False),
    ExpectedImage("social/nelson-grey-profile-1080x1080.png", 1080, 1080, alpha=True),
    ExpectedImage("social/nelson-grey-open-graph-1200x630.png", 1200, 630, alpha=False),
    ExpectedImage("social/nelson-grey-youtube-banner-2560x1440.png", 2560, 1440, alpha=False),
    ExpectedImage("web/nelson-grey-portfolio-hero-2400x1350.png", 2400, 1350, alpha=False),
    ExpectedImage("web/nelson-grey-site-icon-512x512.png", 512, 512, alpha=True),
    ExpectedImage("email/nelson-grey-email-signature-1200x280.png", 1200, 280, alpha=False),
    ExpectedImage("press/nelson-grey-press-cover-1920x1080.png", 1920, 1080, alpha=False),
    ExpectedImage("press/nelson-grey-portfolio-overview-1920x1080.png", 1920, 1080, alpha=False),
)


REQUIRED_VECTORS = (
    "sources/nelson-grey-brand-icon.svg",
    "sources/nelson-grey-developer-icon.svg",
    "sources/header-art-master.svg",
    "sources/developer-mark-board.svg",
    "sources/nelson-grey-mark-on-light.svg",
    "sources/nelson-grey-mark-reverse.svg",
    "sources/nelson-grey-mark-mono-ink.svg",
    "sources/nelson-grey-mark-mono-white.svg",
    "sources/nelson-grey-wordmark-primary.svg",
    "sources/nelson-grey-wordmark-primary-reverse.svg",
    "sources/nelson-grey-name-lockup.svg",
    "sources/nelson-grey-name-lockup-reverse.svg",
)


REQUIRED_SOURCE_IMAGES = (
    ("sources/portfolio/modulo-squares-icon.png", 1024, 1024),
    ("sources/portfolio/vehicle-vitals-icon.png", 4096, 4096),
    ("sources/portfolio/wishlist-wizard-icon.png", 1024, 1024),
)


ROOT_ICON_IMAGES = (
    ("assets/apple-touch-icon.png", 180, 180),
    ("assets/favicon-16x16.png", 16, 16),
    ("assets/favicon-32x32.png", 32, 32),
)


LOCKUP_SOURCES = (
    ("sources/nelson-grey-name-lockup.svg", "#101722", "#53616F"),
    ("sources/nelson-grey-name-lockup-reverse.svg", "#F8F4EA", "#D7CCB8"),
)


LOCKUP_EMBEDDINGS = (
    ("sources/nelson-grey-wordmark-primary.svg", "nelson-grey-name-lockup.svg"),
    ("sources/nelson-grey-wordmark-primary-reverse.svg", "nelson-grey-name-lockup-reverse.svg"),
    ("sources/nelson-grey-stacked-lockup.svg", "nelson-grey-name-lockup-reverse.svg"),
    ("sources/email-signature.svg", "nelson-grey-name-lockup.svg"),
    ("sources/portfolio-hero.svg", "nelson-grey-name-lockup-reverse.svg"),
    ("sources/open-graph-card.svg", "nelson-grey-name-lockup-reverse.svg"),
    ("sources/youtube-banner.svg", "nelson-grey-name-lockup-reverse.svg"),
    ("sources/brand-board.svg", "nelson-grey-name-lockup.svg"),
)


TEXT_LIMITS = (
    ("copy/google-promotional-text.txt", 140),
    ("copy/apple-featuring-nomination-description.txt", 1000),
    ("copy/apple-featuring-helpful-details.txt", 500),
)


REQUIRED_CONTACT_VALUES = (
    ("copy/developer-profile-copy.md", ACCOUNT_OWNER_EMAIL),
    ("copy/developer-profile-copy.md", PUBLIC_CONTACT_EMAIL),
    ("copy/portfolio-landing-page.md", f"mailto:{PUBLIC_CONTACT_EMAIL}"),
    ("sources/email-signature.svg", PUBLIC_CONTACT_EMAIL),
)


def has_alpha(image: Image.Image) -> bool:
    return image.mode in {"RGBA", "LA"} or "transparency" in image.info


def validate_images() -> tuple[list[dict[str, object]], list[str]]:
    rows: list[dict[str, object]] = []
    errors: list[str] = []

    for expected in EXPECTED_IMAGES:
        path = KIT_ROOT / expected.relative_path
        row: dict[str, object] = {
            "path": expected.relative_path,
            "width": "",
            "height": "",
            "format": "",
            "mode": "",
            "alpha": "",
            "bytes": "",
            "status": "FAIL",
        }
        if not path.exists():
            errors.append(f"missing image: {expected.relative_path}")
            rows.append(row)
            continue

        try:
            with Image.open(path) as image:
                actual_alpha = has_alpha(image)
                row.update(
                    {
                        "width": image.width,
                        "height": image.height,
                        "format": image.format or "",
                        "mode": image.mode,
                        "alpha": str(actual_alpha).lower(),
                        "bytes": path.stat().st_size,
                    }
                )
                image.load()

                problems: list[str] = []
                if image.size != (expected.width, expected.height):
                    problems.append(
                        f"expected {expected.width}x{expected.height}, got {image.width}x{image.height}"
                    )
                if image.format not in expected.allowed_formats:
                    problems.append(
                        f"expected format {expected.allowed_formats}, got {image.format}"
                    )
                if expected.alpha is not None and actual_alpha != expected.alpha:
                    problems.append(
                        f"expected alpha={expected.alpha}, got alpha={actual_alpha}"
                    )

                if problems:
                    errors.append(f"{expected.relative_path}: {'; '.join(problems)}")
                else:
                    row["status"] = "PASS"
        except Exception as exc:  # pragma: no cover - defensive validation path
            errors.append(f"{expected.relative_path}: could not read image: {exc}")

        rows.append(row)

    return rows, errors


def validate_supporting_files() -> list[str]:
    errors: list[str] = []

    for relative_path in REQUIRED_VECTORS:
        if not (KIT_ROOT / relative_path).exists():
            errors.append(f"missing vector source: {relative_path}")

    for relative_path, expected_width, expected_height in REQUIRED_SOURCE_IMAGES:
        path = KIT_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing portfolio icon source: {relative_path}")
            continue
        try:
            with Image.open(path) as image:
                if image.size != (expected_width, expected_height):
                    errors.append(
                        f"{relative_path}: expected {expected_width}x{expected_height}, "
                        f"got {image.width}x{image.height}"
                    )
                image.load()
        except Exception as exc:  # pragma: no cover - defensive validation path
            errors.append(f"{relative_path}: could not read source image: {exc}")

    for relative_path, expected_width, expected_height in ROOT_ICON_IMAGES:
        path = REPO_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing website icon derivative: {relative_path}")
            continue
        try:
            with Image.open(path) as image:
                if image.size != (expected_width, expected_height):
                    errors.append(
                        f"{relative_path}: expected {expected_width}x{expected_height}, "
                        f"got {image.width}x{image.height}"
                    )
                if image.format != "PNG":
                    errors.append(f"{relative_path}: expected PNG, got {image.format}")
                if not has_alpha(image):
                    errors.append(f"{relative_path}: expected alpha channel")
                image.load()
        except Exception as exc:  # pragma: no cover - defensive validation path
            errors.append(f"{relative_path}: could not read website icon: {exc}")

    favicon_path = REPO_ROOT / "favicon.ico"
    if not favicon_path.exists():
        errors.append("missing website icon derivative: favicon.ico")
    else:
        try:
            with Image.open(favicon_path) as favicon:
                sizes = favicon.ico.sizes()
                if sizes != {(16, 16), (32, 32), (48, 48)}:
                    errors.append(f"favicon.ico: unexpected embedded sizes: {sorted(sizes)}")
        except Exception as exc:  # pragma: no cover - defensive validation path
            errors.append(f"favicon.ico: could not read website icon: {exc}")

    for relative_path, maximum in TEXT_LIMITS:
        path = KIT_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing copy file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8").strip()
        if len(text) > maximum:
            errors.append(f"{relative_path}: {len(text)} characters exceeds {maximum}")
        if not text:
            errors.append(f"{relative_path}: copy is empty")

    for relative_path, required_value in REQUIRED_CONTACT_VALUES:
        path = KIT_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing contact source: {relative_path}")
            continue
        if required_value not in path.read_text(encoding="utf-8"):
            errors.append(f"{relative_path} does not contain required contact value: {required_value}")

    for path in KIT_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if "tagline" in path.name.lower():
            errors.append(f"{path.relative_to(KIT_ROOT)} uses the retired tagline naming")
        if path.suffix.lower() not in TEXT_FILE_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        if DEPRECATED_CONTACT_EMAIL in text:
            errors.append(f"{path.relative_to(KIT_ROOT)} contains the deprecated contact email")
        for phrase in RETIRED_BRAND_PHRASES:
            if phrase.lower() in text.lower():
                errors.append(f"{path.relative_to(KIT_ROOT)} contains retired brand language: {phrase}")

    return errors


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def validate_core_icon_sources() -> list[str]:
    errors: list[str] = []
    required_border = {
        "x": "0.75",
        "y": "0.75",
        "width": "94.5",
        "height": "94.5",
        "rx": "21.25",
        "stroke": "#D7CCB8",
        "stroke-width": "1.5",
    }

    trees: dict[str, ET.Element] = {}
    for label, path in (
        ("authoritative core", AUTHORITATIVE_CORE_SOURCE),
        ("kit core", CORE_ICON_SOURCE),
        ("developer", DEVELOPER_ICON_SOURCE),
    ):
        if not path.exists():
            errors.append(f"missing {label} icon source: {path}")
            continue
        try:
            trees[label] = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{path}: invalid SVG: {exc}")

    for label in ("authoritative core", "kit core"):
        root = trees.get(label)
        if root is None:
            continue
        matching_borders = [
            element
            for element in root
            if local_name(element) == "rect"
            and all(element.attrib.get(key) == value for key, value in required_border.items())
        ]
        if len(matching_borders) != 1:
            errors.append(f"{label} icon must contain the official core keyline exactly once")

    developer_root = trees.get("developer")
    if developer_root is not None:
        if any(
            local_name(element) == "rect" and element.attrib.get("stroke") == "#D7CCB8"
            for element in developer_root
        ):
            errors.append("developer icon must not use the light-field core keyline")

    core_root = trees.get("kit core")
    if core_root is not None and developer_root is not None:
        def internal_geometry(root: ET.Element) -> list[tuple[str, tuple[tuple[str, str], ...]]]:
            geometry: list[tuple[str, tuple[tuple[str, str], ...]]] = []
            for element in root:
                tag = local_name(element)
                if tag not in {"path", "circle"}:
                    continue
                attributes = tuple(
                    sorted(
                        (key, value)
                        for key, value in element.attrib.items()
                        if key not in {"fill", "stroke"}
                    )
                )
                geometry.append((tag, attributes))
            return geometry

        if internal_geometry(core_root) != internal_geometry(developer_root):
            errors.append("developer icon internal geometry does not match the core icon")

    return errors


def validate_lockup_system() -> list[str]:
    errors: list[str] = []

    for relative_path, expected_name_color, expected_suffix_color in LOCKUP_SOURCES:
        path = KIT_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing standardized LLC lockup: {relative_path}")
            continue
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{relative_path}: invalid SVG: {exc}")
            continue

        name_elements = [
            element
            for element in root.iter()
            if local_name(element) == "text" and element.attrib.get("data-role") == "brand-name"
        ]
        suffix_elements = [
            element
            for element in root.iter()
            if local_name(element) == "tspan" and element.attrib.get("data-role") == "legal-suffix"
        ]
        if len(name_elements) != 1 or len(suffix_elements) != 1:
            errors.append(f"{relative_path}: expected one brand name and one legal suffix")
            continue

        name = name_elements[0]
        suffix = suffix_elements[0]
        try:
            name_size = float(name.attrib["font-size"])
            suffix_size = float(suffix.attrib["font-size"])
            horizontal_gap = float(suffix.attrib["dx"])
            baseline_shift = abs(float(suffix.attrib["dy"]))
            tracking = float(suffix.attrib["letter-spacing"])
        except (KeyError, ValueError) as exc:
            errors.append(f"{relative_path}: malformed LLC proportion value: {exc}")
            continue

        checks = (
            (suffix_size / name_size, 0.3125, "suffix size"),
            (horizontal_gap / name_size, 0.16, "horizontal gap"),
            (baseline_shift / name_size, 0.5, "baseline raise"),
            (tracking / suffix_size, 0.08, "suffix tracking"),
        )
        for actual, expected, label in checks:
            if abs(actual - expected) > 0.0001:
                errors.append(
                    f"{relative_path}: {label} ratio {actual:.4f} does not match {expected:.4f}"
                )
        if name.text != "Nelson Grey" or suffix.text != "LLC":
            errors.append(f"{relative_path}: standardized lockup text is incorrect")
        if name.attrib.get("font-weight") != "700" or suffix.attrib.get("font-weight") != "700":
            errors.append(f"{relative_path}: standardized lockup must use weight 700")
        if name.attrib.get("fill") != expected_name_color:
            errors.append(f"{relative_path}: unexpected brand-name color")
        if suffix.attrib.get("fill") != expected_suffix_color:
            errors.append(f"{relative_path}: unexpected LLC suffix color")

    for relative_path, required_href in LOCKUP_EMBEDDINGS:
        path = KIT_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing lockup composition: {relative_path}")
            continue
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{relative_path}: invalid SVG: {exc}")
            continue
        hrefs = [
            element.attrib.get("href")
            for element in root.iter()
            if local_name(element) == "image"
        ]
        if required_href not in hrefs:
            errors.append(f"{relative_path}: does not embed {required_href}")

    return errors


def validate_core_icon_fidelity() -> list[str]:
    """Require both editable core sources to render like the approved touch icon."""

    if not AUTHORITATIVE_TOUCH_ICON.exists():
        return [f"missing authoritative icon: {AUTHORITATIVE_TOUCH_ICON}"]
    sources = (
        ("assets/nelson-grey-mark.svg", AUTHORITATIVE_CORE_SOURCE),
        ("sources/nelson-grey-brand-icon.svg", CORE_ICON_SOURCE),
    )
    for label, source in sources:
        if not source.exists():
            return [f"missing core icon source: {label}"]

    try:
        with tempfile.TemporaryDirectory(prefix="nelson-grey-icon-check-") as temp_dir:
            for index, (label, source) in enumerate(sources):
                rendered_path = Path(temp_dir) / f"core-icon-{index}-180.png"
                subprocess.run(
                    (
                        "rsvg-convert",
                        "--width",
                        "180",
                        "--height",
                        "180",
                        str(source),
                        "--output",
                        str(rendered_path),
                    ),
                    check=True,
                    capture_output=True,
                    text=True,
                )
                with Image.open(rendered_path) as rendered, Image.open(
                    AUTHORITATIVE_TOUCH_ICON
                ) as approved:
                    if rendered.size != approved.size:
                        return [
                            f"{label}: core icon fidelity check has mismatched dimensions: "
                            f"rendered {rendered.size}, approved {approved.size}"
                        ]
                    difference = ImageChops.difference(
                        rendered.convert("RGBA"), approved.convert("RGBA")
                    )
                    if difference.getbbox() is not None:
                        return [
                            f"{label} does not pixel-match assets/apple-touch-icon.png "
                            "at 180 x 180"
                        ]
    except (OSError, subprocess.CalledProcessError) as exc:
        return [f"could not run core icon fidelity check: {exc}"]

    return []


def write_manifest(rows: list[dict[str, object]]) -> None:
    with MANIFEST_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("path", "width", "height", "format", "mode", "alpha", "bytes", "status"),
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows, image_errors = validate_images()
    supporting_errors = validate_supporting_files()
    core_source_errors = validate_core_icon_sources()
    lockup_errors = validate_lockup_system()
    fidelity_errors = validate_core_icon_fidelity()
    write_manifest(rows)

    errors = (
        image_errors
        + supporting_errors
        + core_source_errors
        + lockup_errors
        + fidelity_errors
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(rows)} raster assets; manifest: {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
