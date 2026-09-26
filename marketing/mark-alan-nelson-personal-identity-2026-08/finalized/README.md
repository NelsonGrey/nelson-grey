# Mark Alan Nelson faithful final assets

This package replaces the rejected hand-reconstructed vector set. The approved chat
renderings—not approximated SVG geometry—are the source of truth.

## What is preserved

- Prairie Lineage icon and lockup are copied byte-for-byte from the approved
  transparent masters.
- Four Bearings icon and lockup are extracted from the approved chat rendering.
- Four Bearings post-processing is limited to checkerboard removal, edge cleanup,
  transparent padding, and resizing.
- No angles, intersections, line weights, letterforms, tracking, baselines, colors,
  or icon-to-type proportions are manually redrawn.

## Deliverables

Each direction includes:

- its highest-resolution transparent PNG master;
- transparent icon exports at 1024, 512, 256, 128, 64, and 32 pixels;
- two smaller transparent horizontal-logo exports;
- a 1920 × 1080 light-background usage proof.

`proofs/fidelity-overview-1920x1080.png` shows both faithful systems together.
`proofs/small-size-proof-1200x360.png` shows both icons at 32, 64, and 128 pixels.
The two `four-bearings-native-*-reference.png` files are pixel-for-pixel crops of
the original approved concept board and serve as immutable geometry references.
`asset-manifest.csv` lists every user-facing file.
`EXTRACTION_PROMPTS.md` records the exact Four Bearings extraction intent and
post-processing boundary.

## Why there are no production SVGs

The previous SVGs were unusable because their geometry was manually approximated.
This replacement does not claim that an automatic or reconstructed trace is the
approved mark. If vector artwork is needed later, commission or perform a dedicated
Bezier trace while continuously overlaying it against these raster masters at high
magnification. Do not start from the rejected SVGs.

## Recommended use

- Use the master or the nearest larger PNG and scale down once in the destination.
- Do not enlarge a derived PNG above its named dimensions.
- Use both identities on white, parchment, limestone, or another quiet light field.
- Do not recolor, skew, rotate, independently move internal pieces, or recombine the
  two systems.
- Use 64 pixels as the preferred practical minimum for the icons. The 32-pixel files
  are supplied for favicon contexts only.

## Rebuilding

```bash
./build-assets.sh
./validate-assets.sh
```

The source renderings are retained under `sources/`, making the package reproducible
without relying on the image-generation cache.
