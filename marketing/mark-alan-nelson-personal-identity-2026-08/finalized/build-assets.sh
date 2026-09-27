#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_dir="$script_dir/sources"
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT

mkdir -p \
  "$script_dir/prairie-lineage/png" \
  "$script_dir/four-bearings/png" \
  "$script_dir/proofs"

# Exact native-resolution board crops are retained as pixel-for-pixel geometry references.
magick "$source_dir/four-bearings-approved-concept-board.png" \
  -crop 600x620+45+80 +repage \
  "$script_dir/proofs/four-bearings-native-icon-reference.png"
magick "$source_dir/four-bearings-approved-concept-board.png" \
  -crop 950x340+680+230 +repage \
  "$script_dir/proofs/four-bearings-native-logo-reference.png"

clean_checker_to_alpha() {
  local source_file="$1"
  local output_file="$2"
  local keyed_file="$work_dir/keyed-$(basename "$output_file")"
  local mask_file="$work_dir/mask-$(basename "$output_file")"

  magick "$source_file" \
    -alpha on \
    -channel A -fx 'clamp((0.93-(r+g+b)/3)/0.04)' +channel \
    -channel RGB -fx 'a<0.02?0:clamp((u-(1-a)*0.97)/a)' +channel \
    "$keyed_file"

  magick "$keyed_file" \
    -alpha extract \
    -morphology Erode Disk:1 \
    -blur 0x0.35 \
    "$mask_file"

  magick "$keyed_file" "$mask_file" \
    -alpha off -compose CopyOpacity -composite \
    "$output_file"
}

# Prairie Lineage: the approved transparent masters are copied byte-for-byte.
cp "$source_dir/prairie-lineage-approved-icon-master.png" \
  "$script_dir/prairie-lineage/png/icon-master-1254x1254.png"
cp "$source_dir/prairie-lineage-approved-logo-master.png" \
  "$script_dir/prairie-lineage/png/logo-master-1800x512.png"

# Four Bearings: preserve the chat render and remove only the encoded checkerboard.
clean_checker_to_alpha \
  "$source_dir/four-bearings-extracted-icon-chat-render.png" \
  "$work_dir/four-bearings-icon-clean.png"
magick "$work_dir/four-bearings-icon-clean.png" \
  -trim +repage \
  "$work_dir/four-bearings-icon-trimmed.png"
magick -size 1254x1254 canvas:none \
  "$work_dir/four-bearings-icon-trimmed.png" \
  -gravity center -compose over -composite \
  "$script_dir/four-bearings/png/icon-master-1254x1254.png"

clean_checker_to_alpha \
  "$source_dir/four-bearings-extracted-logo-chat-render.png" \
  "$work_dir/four-bearings-logo-clean.png"
magick "$work_dir/four-bearings-logo-clean.png" \
  -trim +repage -bordercolor none -border 70 \
  "$script_dir/four-bearings/png/logo-master-1710x546.png"

for concept in prairie-lineage four-bearings; do
  icon_master="$script_dir/$concept/png/icon-master-1254x1254.png"
  for size in 1024 512 256 128 64 32; do
    magick "$icon_master" -filter Lanczos -resize "${size}x${size}" \
      "$script_dir/$concept/png/icon-${size}x${size}.png"
  done
done

magick "$script_dir/prairie-lineage/png/logo-master-1800x512.png" \
  -filter Lanczos -resize 1600x \
  "$script_dir/prairie-lineage/png/logo-1600x455.png"
magick "$script_dir/prairie-lineage/png/logo-master-1800x512.png" \
  -filter Lanczos -resize 1200x \
  "$script_dir/prairie-lineage/png/logo-1200x341.png"

magick "$script_dir/four-bearings/png/logo-master-1710x546.png" \
  -filter Lanczos -resize 1600x \
  "$script_dir/four-bearings/png/logo-1600x511.png"
magick "$script_dir/four-bearings/png/logo-master-1710x546.png" \
  -filter Lanczos -resize 1200x \
  "$script_dir/four-bearings/png/logo-1200x383.png"

# Faithful usage previews. These flatten the transparent masters without changing them.
magick -size 1920x1080 xc:'#F4EFE5' \
  \( "$script_dir/prairie-lineage/png/logo-master-1800x512.png" -resize 1660x \) \
  -gravity center -compose over -composite \
  "$script_dir/proofs/prairie-lineage-on-light-1920x1080.png"

magick -size 1920x1080 xc:'#F1EBDD' \
  \( "$script_dir/four-bearings/png/logo-master-1710x546.png" -resize 1660x \) \
  -gravity center -compose over -composite \
  "$script_dir/proofs/four-bearings-on-light-1920x1080.png"

magick -size 1920x1080 xc:'#FFFFFF' \
  -font '/System/Library/Fonts/Supplemental/Arial.ttf' -fill '#53616F' -pointsize 30 \
  -draw "text 90,82 'PRAIRIE LINEAGE' text 90,620 'FOUR BEARINGS'" \
  -stroke '#D7CCB8' -strokewidth 2 -draw 'line 80,540 1840,540' +stroke \
  \( "$script_dir/prairie-lineage/png/icon-512x512.png" -resize 330x330 \) -geometry +110+130 -compose over -composite \
  \( "$script_dir/prairie-lineage/png/logo-1200x341.png" -resize 1220x \) -geometry +560+140 -compose over -composite \
  \( "$script_dir/four-bearings/png/icon-512x512.png" -resize 330x330 \) -geometry +110+670 -compose over -composite \
  \( "$script_dir/four-bearings/png/logo-1200x383.png" -resize 1220x \) -geometry +560+650 -compose over -composite \
  "$script_dir/proofs/fidelity-overview-1920x1080.png"

magick -size 1200x360 xc:'#FFFFFF' \
  -font '/System/Library/Fonts/Supplemental/Arial.ttf' -fill '#53616F' -pointsize 24 \
  -draw "text 55,48 'PRAIRIE LINEAGE' text 655,48 'FOUR BEARINGS'" \
  \( "$script_dir/prairie-lineage/png/icon-32x32.png" \) -geometry +70+155 -compose over -composite \
  \( "$script_dir/prairie-lineage/png/icon-64x64.png" \) -geometry +155+139 -compose over -composite \
  \( "$script_dir/prairie-lineage/png/icon-128x128.png" \) -geometry +280+107 -compose over -composite \
  \( "$script_dir/four-bearings/png/icon-32x32.png" \) -geometry +670+155 -compose over -composite \
  \( "$script_dir/four-bearings/png/icon-64x64.png" \) -geometry +755+139 -compose over -composite \
  \( "$script_dir/four-bearings/png/icon-128x128.png" \) -geometry +880+107 -compose over -composite \
  "$script_dir/proofs/small-size-proof-1200x360.png"
