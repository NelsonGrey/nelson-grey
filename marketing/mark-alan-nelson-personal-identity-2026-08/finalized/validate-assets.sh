#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
expected_png_count=31

actual_png_count="$(find "$script_dir" -type f -name '*.png' | wc -l | tr -d ' ')"
if [[ "$actual_png_count" != "$expected_png_count" ]]; then
  echo "Expected $expected_png_count PNG files, found $actual_png_count" >&2
  exit 1
fi

cmp \
  "$script_dir/sources/prairie-lineage-approved-icon-master.png" \
  "$script_dir/prairie-lineage/png/icon-master-1254x1254.png"
cmp \
  "$script_dir/sources/prairie-lineage-approved-logo-master.png" \
  "$script_dir/prairie-lineage/png/logo-master-1800x512.png"

for concept in prairie-lineage four-bearings; do
  for size in 1024 512 256 128 64 32; do
    file="$script_dir/$concept/png/icon-${size}x${size}.png"
    geometry="$(magick identify -format '%wx%h' "$file")"
    alpha="$(magick identify -format '%[opaque]' "$file")"
    [[ "$geometry" == "${size}x${size}" ]] || {
      echo "Unexpected geometry for $file: $geometry" >&2
      exit 1
    }
    [[ "$alpha" == "False" ]] || {
      echo "Expected transparency in $file" >&2
      exit 1
    }
  done
done

expected_files=(
  "prairie-lineage/png/icon-master-1254x1254.png"
  "prairie-lineage/png/logo-master-1800x512.png"
  "prairie-lineage/png/logo-1600x455.png"
  "prairie-lineage/png/logo-1200x341.png"
  "four-bearings/png/icon-master-1254x1254.png"
  "four-bearings/png/logo-master-1710x546.png"
  "four-bearings/png/logo-1600x511.png"
  "four-bearings/png/logo-1200x383.png"
  "proofs/prairie-lineage-on-light-1920x1080.png"
  "proofs/four-bearings-on-light-1920x1080.png"
  "proofs/fidelity-overview-1920x1080.png"
  "proofs/small-size-proof-1200x360.png"
  "proofs/four-bearings-native-icon-reference.png"
  "proofs/four-bearings-native-logo-reference.png"
)

for relative_path in "${expected_files[@]}"; do
  [[ -f "$script_dir/$relative_path" ]] || {
    echo "Missing expected file: $relative_path" >&2
    exit 1
  }
done

four_icon_alpha="$(magick identify -format '%[opaque]' "$script_dir/four-bearings/png/icon-master-1254x1254.png")"
four_logo_alpha="$(magick identify -format '%[opaque]' "$script_dir/four-bearings/png/logo-master-1710x546.png")"
[[ "$four_icon_alpha" == "False" && "$four_logo_alpha" == "False" ]] || {
  echo "Four Bearings masters must contain genuine transparency" >&2
  exit 1
}

echo "Validated $actual_png_count faithful raster assets. Prairie masters are byte-identical to the approved files."
