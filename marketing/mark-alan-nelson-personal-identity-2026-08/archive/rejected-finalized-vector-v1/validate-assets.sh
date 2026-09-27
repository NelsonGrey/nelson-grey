#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
expected_png_count=25
expected_manifest_rows=38

find "$script_dir" -type f -name '*.svg' -print0 | xargs -0 xmllint --noout

actual_png_count="$(find "$script_dir" -type f -name '*.png' | wc -l | tr -d ' ')"
if [[ "$actual_png_count" != "$expected_png_count" ]]; then
  echo "Expected $expected_png_count PNG files, found $actual_png_count" >&2
  exit 1
fi

for concept in prairie-lineage four-bearings; do
  for size in 1024 512 256 64 32; do
    file="$script_dir/$concept/png/icon-primary-${size}x${size}.png"
    geometry="$(magick identify -format '%wx%h' "$file")"
    [[ "$geometry" == "${size}x${size}" ]] || {
      echo "Unexpected geometry for $file: $geometry" >&2
      exit 1
    }
  done

  for logo in primary reverse mono; do
    file="$script_dir/$concept/png/logo-${logo}-2200x620.png"
    geometry="$(magick identify -format '%wx%h' "$file")"
    [[ "$geometry" == "2200x620" ]] || {
      echo "Unexpected geometry for $file: $geometry" >&2
      exit 1
    }
  done

  grep -q 'MARK' "$script_dir/$concept/sources/logo-primary.svg"
  grep -q 'ALAN' "$script_dir/$concept/sources/logo-primary.svg"
  grep -q 'NELSON' "$script_dir/$concept/sources/logo-primary.svg"
done

comparison_geometry="$(magick identify -format '%wx%h' "$script_dir/identity-comparison-1920x1080.png")"
[[ "$comparison_geometry" == "1920x1080" ]] || {
  echo "Unexpected comparison geometry: $comparison_geometry" >&2
  exit 1
}

manifest_rows="$(tail -n +2 "$script_dir/asset-manifest.csv" | sed '/^[[:space:]]*$/d' | wc -l | tr -d ' ')"
if [[ "$manifest_rows" != "$expected_manifest_rows" ]]; then
  echo "Expected $expected_manifest_rows manifest rows, found $manifest_rows" >&2
  exit 1
fi

while IFS=, read -r concept asset path format dimensions background use; do
  [[ "$concept" == "concept" ]] && continue
  [[ -z "$path" ]] && continue
  [[ -f "$script_dir/$path" ]] || {
    echo "Manifest path is missing: $path" >&2
    exit 1
  }
done < "$script_dir/asset-manifest.csv"

echo "Validated $actual_png_count PNG files all SVG sources and $manifest_rows manifest rows."
