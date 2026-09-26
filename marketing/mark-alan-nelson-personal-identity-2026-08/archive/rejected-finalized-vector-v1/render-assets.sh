#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

render_icon_set() {
  local concept="$1"
  local source_dir="$script_dir/$concept/sources"
  local output_dir="$script_dir/$concept/png"

  mkdir -p "$output_dir"

  for size in 1024 512 256 64 32; do
    rsvg-convert --width "$size" --height "$size" \
      --output "$output_dir/icon-primary-${size}x${size}.png" \
      "$source_dir/icon-primary.svg"
  done

  for size in 1024 512; do
    rsvg-convert --width "$size" --height "$size" \
      --output "$output_dir/icon-reverse-${size}x${size}.png" \
      "$source_dir/icon-reverse.svg"
    rsvg-convert --width "$size" --height "$size" \
      --output "$output_dir/icon-mono-${size}x${size}.png" \
      "$source_dir/icon-mono.svg"
  done

  rsvg-convert --width 2200 --height 620 \
    --output "$output_dir/logo-primary-2200x620.png" \
    "$source_dir/logo-primary.svg"
  rsvg-convert --width 2200 --height 620 \
    --output "$output_dir/logo-reverse-2200x620.png" \
    "$source_dir/logo-reverse.svg"
  rsvg-convert --width 2200 --height 620 \
    --output "$output_dir/logo-mono-2200x620.png" \
    "$source_dir/logo-mono.svg"
}

render_icon_set "prairie-lineage"
render_icon_set "four-bearings"

rsvg-convert --width 1920 --height 1080 \
  --output "$script_dir/identity-comparison-1920x1080.png" \
  "$script_dir/identity-comparison.svg"

