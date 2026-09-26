#!/usr/bin/env bash
set -euo pipefail

KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_ROOT="$KIT_ROOT/sources"
REPO_ROOT="$(cd "$KIT_ROOT/../.." && pwd)"
WEBSITE_MARK_SOURCE="$REPO_ROOT/assets/nelson-grey-mark.svg"

for command_name in rsvg-convert magick; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    echo "Missing required command: $command_name" >&2
    exit 1
  fi
done

mkdir -p \
  "$KIT_ROOT/google" \
  "$KIT_ROOT/brand" \
  "$KIT_ROOT/social" \
  "$KIT_ROOT/web" \
  "$KIT_ROOT/email" \
  "$KIT_ROOT/press"

if [[ ! -f "$WEBSITE_MARK_SOURCE" ]]; then
  echo "Missing authoritative website mark: $WEBSITE_MARK_SOURCE" >&2
  exit 1
fi

render_svg() {
  local source_file="$1"
  local width="$2"
  local height="$3"
  local output_file="$4"
  rsvg-convert \
    --width "$width" \
    --height "$height" \
    "$SOURCE_ROOT/$source_file" \
    --output "$KIT_ROOT/$output_file"
}

icon_temp_dir="$(mktemp -d)"
rsvg-convert --width 180 --height 180 "$WEBSITE_MARK_SOURCE" --output "$REPO_ROOT/assets/apple-touch-icon.png"
rsvg-convert --width 16 --height 16 "$WEBSITE_MARK_SOURCE" --output "$REPO_ROOT/assets/favicon-16x16.png"
rsvg-convert --width 32 --height 32 "$WEBSITE_MARK_SOURCE" --output "$REPO_ROOT/assets/favicon-32x32.png"
rsvg-convert --width 16 --height 16 "$WEBSITE_MARK_SOURCE" --output "$icon_temp_dir/favicon-16.png"
rsvg-convert --width 32 --height 32 "$WEBSITE_MARK_SOURCE" --output "$icon_temp_dir/favicon-32.png"
rsvg-convert --width 48 --height 48 "$WEBSITE_MARK_SOURCE" --output "$icon_temp_dir/favicon-48.png"
magick \
  "$icon_temp_dir/favicon-16.png" \
  "$icon_temp_dir/favicon-32.png" \
  "$icon_temp_dir/favicon-48.png" \
  "$REPO_ROOT/favicon.ico"
rm \
  "$icon_temp_dir/favicon-16.png" \
  "$icon_temp_dir/favicon-32.png" \
  "$icon_temp_dir/favicon-48.png"
rmdir "$icon_temp_dir"

render_svg "nelson-grey-developer-icon.svg" 512 512 ".developer-icon-rgb.png"
magick "$KIT_ROOT/.developer-icon-rgb.png" \
  -alpha on \
  -define png:color-type=6 \
  "PNG32:$KIT_ROOT/google/developer-icon-512x512.png"
rm "$KIT_ROOT/.developer-icon-rgb.png"

render_svg "header-art-master.svg" 4096 2304 ".header-art-rgb.png"
magick "$KIT_ROOT/.header-art-rgb.png" \
  -colorspace sRGB \
  -alpha off \
  -type TrueColor \
  -strip \
  "PNG24:$KIT_ROOT/google/developer-header-4096x2304.png"
rm "$KIT_ROOT/.header-art-rgb.png"

magick "$KIT_ROOT/google/developer-header-4096x2304.png" \
  -quality 91 \
  -sampling-factor 4:4:4 \
  -strip \
  "$KIT_ROOT/google/developer-header-4096x2304.jpg"

render_svg "google-profile-preview.svg" 1600 1200 "google/developer-profile-preview-1600x1200.png"

render_svg "nelson-grey-brand-icon.svg" 1024 1024 "brand/nelson-grey-mark-1024x1024.png"
render_svg "nelson-grey-developer-icon.svg" 1024 1024 "brand/nelson-grey-developer-mark-1024x1024.png"
render_svg "nelson-grey-mark-on-light.svg" 1024 1024 "brand/nelson-grey-mark-on-light-1024x1024.png"
render_svg "nelson-grey-mark-reverse.svg" 1024 1024 "brand/nelson-grey-mark-reverse-1024x1024.png"
render_svg "nelson-grey-mark-mono-ink.svg" 1024 1024 "brand/nelson-grey-mark-mono-ink-1024x1024.png"
render_svg "nelson-grey-mark-mono-white.svg" 1024 1024 "brand/nelson-grey-mark-mono-white-1024x1024.png"
render_svg "nelson-grey-wordmark-primary.svg" 2200 620 "brand/nelson-grey-wordmark-primary-2200x620.png"
render_svg "nelson-grey-wordmark-primary-reverse.svg" 2200 620 "brand/nelson-grey-wordmark-primary-reverse-2200x620.png"
render_svg "nelson-grey-stacked-lockup.svg" 1400 1600 "brand/nelson-grey-stacked-lockup-1400x1600.png"
render_svg "brand-board.svg" 1920 1080 "brand/nelson-grey-brand-board-1920x1080.png"
render_svg "developer-mark-board.svg" 1920 1080 "brand/nelson-grey-core-developer-board-1920x1080.png"

render_svg "nelson-grey-brand-icon.svg" 1080 1080 "social/nelson-grey-profile-1080x1080.png"
render_svg "open-graph-card.svg" 1200 630 "social/nelson-grey-open-graph-1200x630.png"
render_svg "youtube-banner.svg" 2560 1440 "social/nelson-grey-youtube-banner-2560x1440.png"

render_svg "portfolio-hero.svg" 2400 1350 "web/nelson-grey-portfolio-hero-2400x1350.png"
render_svg "nelson-grey-brand-icon.svg" 512 512 "web/nelson-grey-site-icon-512x512.png"
render_svg "email-signature.svg" 1200 280 "email/nelson-grey-email-signature-1200x280.png"
render_svg "portfolio-hero.svg" 1920 1080 "press/nelson-grey-press-cover-1920x1080.png"
render_svg "portfolio-overview.svg" 1920 1080 "press/nelson-grey-portfolio-overview-1920x1080.png"

python3 "$KIT_ROOT/validate-assets.py"
