# Nelson Grey LLC developer-profile promotion kit

Production-ready identity, profile artwork, copy, and publication guidance for Nelson Grey LLC across Google Play, Apple, the web, press, social, and email.

The official Nelson Grey icon in `assets/nelson-grey-mark.svg` is the source of truth. Its Core treatment now includes a quiet `#D7CCB8` inset keyline for contrast on white. `DEVELOPER_MARK.md` documents the developer treatment: identical internal geometry, a `#101722` build-environment field, a `#F8F4EA` `N`, and the original teal and gold details unchanged.

The platform requirements were verified on **2026-08-04**. Run the included validator and recheck `PLATFORM_REQUIREMENTS.md` before a substantially later publication.

## Recommended identity

- Legal organization: **Nelson Grey LLC**
- Public brand: **Nelson Grey**
- Developer-page label: **Software & apps**
- Public website: **https://nelsongrey.com/**
- Public contact: **hello@nelsongrey.com**
- Account owner/login only: **marknelson@nelsongrey.com**
- Logo lockups: **Nelson Grey with a standardized raised `LLC` legal suffix; no slogan or descriptor**
- Visual direction: official company mark in a dark developer context; expressive product brands remain distinct

## What uploads where

| Destination | Direct profile capability | Deliverable |
|---|---|---|
| Google Play Developer Profile | Custom developer icon | `google/developer-icon-512x512.png` |
| Google Play Developer Profile | Custom 16:9 header | `google/developer-header-4096x2304.png` and smaller JPG alternative |
| Google Play Developer Profile | 140-character promotional text | `copy/google-promotional-text.txt` |
| Google Play Developer Profile | Optional website and featured app | Guidance in `copy/developer-profile-copy.md` |
| Apple public developer page | Generated catalog page; no comparable logo/banner/bio fields | See `apple/README.md` for the external portfolio and per-app promotion path |
| Apple featuring nomination | Developer/app story | Two limit-checked text files under `copy/` |
| Portfolio website | Hero, site icon, OG card, and complete page copy | `web/`, `social/`, and `copy/portfolio-landing-page.md` |
| Press and channels | Cover, banner, profile image, boilerplate | `press/`, `social/`, and `copy/` |
| Email | Branded signature image and text | `email/` and `copy/developer-profile-copy.md` |

## Asset inventory

### Google

- 512 × 512 32-bit PNG developer icon
- 4096 × 2304 lossless 24-bit PNG header
- 4096 × 2304 smaller JPEG header
- 1600 × 1200 concept preview showing the assets together

### Brand system

- Official keyed Core icon plus a developer treatment with matching internal geometry
- High-resolution developer mark and a core/developer comparison board
- Light, reverse, and one-color vector marks
- Horizontal wordmarks with the standardized raised `LLC` suffix
- Stacked composition using the same raised `LLC` suffix
- 1920 × 1080 compact brand board
- Palette, typography, clear-space, voice, and co-branding rules in `BRAND_GUIDE.md`

### Cross-platform promotion

- 1080 × 1080 profile image
- 1200 × 630 Open Graph/social card
- 2560 × 1440 channel banner with central safe composition
- 2400 × 1350 portfolio-site hero
- 1920 × 1080 press cover
- 1920 × 1080 three-product portfolio overview with an availability guardrail
- 1200 × 280 email signature

All raster deliverables and their measured properties are listed in `asset-manifest.csv`.

## Copy inventory

- Google promotional text validated under 140 characters
- Apple featuring nomination description validated under 1,000 characters
- Apple Helpful Details validated under 500 characters
- Short, medium, long, press, social, channel, and email bios
- Product snippets for Modulo Squares, Vehicle-Vitals, and Wishlist Wizard with status guardrails
- Complete portfolio landing-page content and SEO fields

## Account and public-contact roles

Use `https://nelsongrey.com/` as the official public website and `hello@nelsongrey.com` as the public company contact. Keep `marknelson@nelsongrey.com` private as the account owner/login only; do not place it in profile copy, artwork, support pages, or public store metadata. Google says an organization account's verified legal name and address, developer email, and developer phone are displayed on Google Play.

## Rebuild and validate

The renderer requires `rsvg-convert`, ImageMagick, Python 3, and Pillow.

```bash
./marketing/developer-profile-kit-2026-08/render-assets.sh
```

The command deterministically rebuilds every raster composition, the website's touch-icon and favicon derivatives, and `asset-manifest.csv`. It preserves the hand-authored SVG sources and fails on missing assets, wrong dimensions, incorrect image formats/alpha state, icon-source drift, lockup-ratio drift, missing copy, or text over platform limits.

## Source and provenance

The repository's `assets/nelson-grey-mark.svg` is the authoritative Core icon. The kit duplicates that field and keyline exactly; the developer treatment preserves the internal N, arc, signal, and node geometry while using its dark field without the light-background keyline.

The canonical identity typography lives in `sources/nelson-grey-name-lockup.svg` and `sources/nelson-grey-name-lockup-reverse.svg`. Every visual lockup embeds one of those two sources, keeping the raised `LLC` size, spacing, tracking, and position consistent. Plain legal prose and platform-controlled account names remain inline `Nelson Grey LLC`.

The wide header is deterministic vector artwork in `sources/header-art-master.svg`. The renderer produces both Google-ready header files directly from that source, so the artwork can be reproduced and reviewed without a generative-image dependency.

The portfolio overview uses the three product-icon references under `sources/portfolio/`. They remain separate product identities and should be reconfirmed against each product's current official icon before publication.

## Publication boundaries

- No Apple or Google account was changed.
- No website, store listing, social profile, or email signature was published.
- `https://nelsongrey.com/` is the official public company website; publishing this kit does not alter it automatically.
- Product descriptions are not proof of current storefront availability.
- Preserve the existing, separate Modulo Squares store-promotion kit; this company-level kit does not replace app-level store media.
