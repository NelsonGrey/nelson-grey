# Rejected artwork — do not use

This directory contains the failed hand-reconstructed vector package. Its angles,
intersections, alignment, spacing, and typography do not faithfully match the
approved chat renderings. It is retained only as a recoverable audit artifact.

The active approved assets are in `../../../finalized/`. Do not publish, print,
trace, derive from, or otherwise use any SVG or PNG in this rejected directory.

## Original rejected documentation

# Mark Alan Nelson finalized personal identities

This package preserves two complete identity directions so either can be adopted
later without reopening the exploratory design work.

## The two directions

### Prairie Lineage

The warmer and more personal direction.

- The navy `M` suggests shelter and Mark's role as husband and father.
- The rising teal `A` represents education, growth, and achievement.
- The copper `N` represents lineage carried forward.
- Four copper waypoints represent the family of four.
- The low teal curve anchors the identity in the Illinois prairie.

Best suited to personal profiles, family-centered work, a personal website, and
social avatars.

### Four Bearings

The more directional and editorial direction.

- Four connected diamond corners represent family as stabilizing bearings.
- The brass upper point represents education and purposeful direction.
- Parallel architectural paths balance marketing judgment with computer-science
  structure.
- The restrained woven construction suggests ancestry without flags or heraldry.
- The serif surname emphasizes heritage while the sans-serif given names keep the
  identity contemporary.

Best suited to writing, speaking, consulting, an executive biography, and formal
presentation covers.

## Package structure

Each concept includes:

- editable full-color, reverse, and one-color SVG sources;
- transparent primary icons at 1024, 512, 256, 64, and 32 pixels;
- reverse and one-color icons at 1024 and 512 pixels;
- primary, reverse, and one-color horizontal PNG logos at 2200 × 620 pixels.

See `asset-manifest.csv` for every deliverable. The comparison board is available
as both SVG and PNG.

## Typography

The SVG wordmarks intentionally retain editable text so the name can be adjusted
later without recreating the artwork.

- Prairie Lineage: `Avenir Next` Bold/Medium; fallbacks are Avenir, Helvetica Neue,
  Arial, and a generic sans serif.
- Four Bearings given names: `Avenir Next` Demi Bold; the same sans-serif fallbacks
  apply.
- Four Bearings surname: `Bodoni 72` Book; fallbacks are Georgia, Times New Roman,
  and a generic serif.

`Avenir Next` and `Bodoni 72` are macOS system fonts and are not bundled. Before
sending final artwork to a printer or another designer, convert the wordmark text
to outlines in the design application being used. Keep the live-text SVG as the
editable master.

## Color systems

### Prairie Lineage

| Color | Hex | Primary role |
|---|---|---|
| Midnight navy | `#142033` | Structure and primary name |
| Prairie teal | `#236E70` | Learning path and Illinois horizon |
| Burnished copper | `#B66A3C` | Lineage and family waypoints |
| Warm parchment | `#F4EFE5` | Icon field and human warmth |

Reverse accents use `#74C7C2` and `#E7A06F` for dark-field contrast.

### Four Bearings

| Color | Hex | Primary role |
|---|---|---|
| Lake navy | `#18314A` | Structure and surname |
| River blue | `#3B7186` | Contemporary path and given names |
| Aged brass | `#AD7B32` | Direction and achievement |
| Limestone | `#F1EBDD` | Warm neutral field |

Reverse accents use `#75AABE` and `#D8AA57` for dark-field contrast.

All wordmark color pairings in the supplied primary and reverse variants meet or
exceed a 4.5:1 contrast ratio. Logos are not ordinary body text, but the threshold
was used as a conservative production check.

## Usage

- Use the primary logo on white, parchment, limestone, or another quiet light field.
- Use the supplied reverse logo as a complete dark-field asset; do not remove its
  background and retain the original accent colors.
- Use the one-color version for engraving, embossing, vinyl cutting, stamps, and
  single-ink printing.
- Use the standalone icon below 240 pixels of available horizontal space.
- Do not render either icon below 32 pixels digitally.
- Keep clear space around an icon equal to at least half the width of its outer
  stroke. Keep clear space around a horizontal logo equal to the cap height of
  `MARK`.
- Do not combine elements from the two directions into a third mark.
- Do not recolor either system with Nelson Grey's exact corporate palette.

## Rebuilding and validation

From this directory:

```bash
./render-assets.sh
./validate-assets.sh
```

Rendering requires `rsvg-convert`; validation also requires ImageMagick and
`xmllint`. The scripts use paths relative to their own location and do not modify
the exploratory concept files.

## Originality and legal status

The marks were created as original personal-identity concepts and intentionally
avoid school crests, flags, state outlines, heraldry, and the protected geometry of
the Nelson Grey company mark. No formal trademark clearance or legal review has
been performed. Conduct an appropriate clearance search before commercial launch
or registration.
