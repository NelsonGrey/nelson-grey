# Four Bearings extraction prompts

The built-in OpenAI image-generation tool was used in edit mode. The approved
concept board was the edit target. These prompts extracted usable high-resolution
assets; they did not authorize redesign.

## Standalone icon

> Isolate only the large Four Bearings emblem shown on the left side of the
> approved board. Remove the limestone background, all text, the smaller lockup
> icon, name, title, and color swatches. Preserve the large emblem pixel-for-pixel
> in design: its exact open-diamond silhouette, every angle, intersection, gap,
> stroke width, taper, alignment, navy-to-blue tonal variation, and aged-brass
> upper chevron and side bars. Center it on a square transparent canvas. Do not
> rotate, redraw, simplify, symmetrize, sharpen into different geometry, or add a
> container. Change only the crop and background. Use genuine alpha transparency
> with clean antialiased edges and no halo.

## Horizontal lockup

> Isolate only the smaller Four Bearings emblem and two-line name lockup shown
> together on the right side of the approved board. Remove the limestone board
> background, large left emblem, concept title, and color swatches. Preserve the
> lockup exactly as approved: the smaller emblem's geometry, every angle and gap,
> its position and scale relative to the name, the letterforms, tracking, line
> spacing, baselines, colors, and two-line hierarchy. Preserve the exact text
> `MARK ALAN` and `NELSON`, each rendered once. Change only the crop and
> background. Do not substitute fonts, change kerning, or alter proportions. Use
> genuine alpha transparency with clean antialiased edges and no halo.

The tool encoded a checkerboard rather than alpha in both initial exports. The
reproducible `build-assets.sh` step removes only that background, decontaminates
the antialiased edge pixels, and preserves native aspect ratios.

