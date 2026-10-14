# Nelson Grey LLC brand guide

## Brand idea

Nelson Grey is the company brand. Individual products can be bright, specific, playful, practical, or technical; the company identity gives them a clear shared owner without forcing them into one visual template.

- Developer-page label: **Software & apps**
- Logo lockups: **Standardized raised `LLC` legal suffix; no slogan or descriptor**
- Character: clear, useful, curious, dependable, and respectfully understated
- Public brand: `Nelson Grey`
- Legal organization: `Nelson Grey LLC`

## Logo concept

The Core mark is maintained in `assets/nelson-grey-mark.svg`. Its continuous `N`, teal arc, gold details, stroke geometry, endpoints, spacing, and rounded-square construction are the recognizable identity and must not be redrawn. A `#D7CCB8` inset keyline follows the outer silhouette and gives the ivory field quiet definition against white.

The developer edition is a contextual treatment, not a new symbol. It preserves the internal path and node geometry exactly, changes the field from warm ivory to `#101722`, changes the `N` from ink to `#F8F4EA`, and leaves the teal and gold unchanged. Its dark field already defines the edge, so it does not carry the Core's light-background keyline. The result evokes a focused build environment without adding literal code symbols or a developer badge.

Use the developer treatment for developer-program profiles and engineering channels. Use the official Core icon for company, portfolio, social, and general identity. Use the standardized wordmark when `Nelson Grey LLC` must be immediately legible. `Software & apps` is a page label or metadata value, never part of a logo lockup.

### Recommended variants

| Situation | Asset |
|---|---|
| Google Play Developer Profile | `google/developer-icon-512x512.png` |
| High-resolution developer mark | `brand/nelson-grey-developer-mark-1024x1024.png` |
| Core company icon | `brand/nelson-grey-mark-1024x1024.png` |
| Core general avatar | `social/nelson-grey-profile-1080x1080.png` |
| Light layout | `sources/nelson-grey-wordmark-primary.svg` |
| Dark layout | `sources/nelson-grey-wordmark-primary-reverse.svg` |
| One-color production | `sources/nelson-grey-mark-mono-ink.svg` or `sources/nelson-grey-mark-mono-white.svg` |

### Clear space and minimum size

- Keep clear space around the monogram equal to at least the width of the `N` stroke.
- Keep clear space around a wordmark equal to the height of the lowercase letters in `Nelson Grey`.
- Do not render the standalone monogram below 32 px digitally.
- Do not render the horizontal wordmark below 220 px wide digitally; use the monogram below that size.
- Keep the full square developer icon unmasked. Let the destination platform apply any display crop.

### Do not

- Rotate, stretch, bevel, add a drop shadow, or add another outline beyond the official Core keyline.
- Alter the official path geometry, stroke widths, endpoints, spacing, or corner radius.
- Recolor individual strokes outside the official core palette or documented developer colorway.
- Place the reverse mark on a busy or low-contrast area.
- Add code brackets, terminal prompts, gears, numbers, vehicle symbols, gifts, or another product's literal iconography to the company mark.
- Use the Nelson Grey mark as an app icon unless the app itself is the company portfolio app.
- Add a slogan, descriptor, or `Software & apps` beneath or beside the wordmark.

## Color system

| Name | Hex | Role |
|---|---|---|
| Build Ink | `#101722` | Core `N`; developer-edition field |
| Nelson Ivory | `#F8F4EA` | Core field; developer-edition `N` |
| Nelson Teal | `#08756F` | Official arc and endpoint; unchanged between editions |
| Nelson Gold | `#C9952F` | Official accent and endpoint; unchanged between editions |
| Nelson Line | `#D7CCB8` | Core keyline; dark-layout legal suffix; supporting rules |

These icon values are exact. Supporting layout neutrals may vary for accessibility, but do not substitute approximate colors inside the mark. Product palettes may differ; do not recolor an app to match the parent brand.

## Typography

The supplied SVGs prefer `Space Grotesk`, matching the public website, with `Avenir Next`, `Avenir`, `Helvetica Neue`, `Arial`, and generic sans-serif fallbacks. `Newsreader` remains available for editorial accents on the website. The identity depends on clean proportions and spacing, not a proprietary display typeface.

- Headings: Space Grotesk Bold
- Body: Space Grotesk Regular or Medium
- Editorial accent: Newsreader Regular or Semibold
- Metadata: Space Grotesk Bold, tracked in uppercase
- SVG fallback: `Space Grotesk, Avenir Next, Avenir, Helvetica Neue, Arial, sans-serif`

If materials must be produced on systems without Space Grotesk, use the documented fallback stack and preserve the hierarchy, tracking, and generous whitespace.

### Legal suffix standard

In identity lockups, `LLC` is a raised legal suffix—not a tagline or descriptor. Use the shared sources `nelson-grey-name-lockup.svg` and `nelson-grey-name-lockup-reverse.svg` instead of rebuilding the typography.

- `LLC` size: 31.25% of the `Nelson Grey` name size
- Baseline raise: 50% of the name size
- Left gap: 16% of the name size
- Suffix tracking: 8% of the suffix size
- Weight: 700, matching the name
- Light layouts: `#53616F`; dark layouts: `#D7CCB8`

Keep ordinary legal prose, contracts, metadata, copyrights, and platform-controlled account names inline as `Nelson Grey LLC`. The public-brand form `Nelson Grey` may appear without the suffix; never place `LLC` beneath the name or enlarge it to the name's baseline size in a visual lockup.

## Composition

- Use deep, quiet fields with precise modular structures at the edges.
- Keep key copy in a calm zone instead of laying text over the most detailed artwork.
- Prefer one strong mark and concise page copy over a slogan or descriptor lockup.
- Use rounded geometry and connected paths as company motifs; reserve literal gameplay, vehicle, or gifting imagery for product pages.
- Show multiple app identities as separate cards or icons. Do not blend their marks together.

## Voice

### Clear

Name the customer job and the current capability. Prefer `Keep service records ready` over `Revolutionize vehicle ownership`.

### Specific

Use concrete nouns and verbs. Explain what falls, what gets organized, or which record stays ready.

### Warmly restrained

Invite interest without hype. A small moment of delight is enough.

### Honest about status

Separate available features, planned work, and experiments. Never turn a roadmap item into profile copy.

## Portfolio architecture

The company identity appears first on a developer profile, press page, or portfolio hub. On an app product page, the app identity appears first and Nelson Grey is an endorsement in the footer, legal copy, Marketing URL destination, or press boilerplate.

Recommended relationship:

```text
Nelson Grey LLC
├── Modulo Squares — expressive game identity
├── Vehicle-Vitals — practical ownership identity
├── Wishlist Wizard — warm organization identity
└── Future products — their own customer-job identity
```

## Contact treatment

Use `https://nelsongrey.com/` as the public website and `hello@nelsongrey.com` as the public company contact. Keep `marknelson@nelsongrey.com` private as the account owner/login only. See `PLATFORM_REQUIREMENTS.md` for the distinction between account identity, public developer contact, and per-app support contact.
