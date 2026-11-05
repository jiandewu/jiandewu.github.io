#!/usr/bin/env bash
# Prepare a photo for zh/photos/: fix orientation, strip all metadata (EXIF, GPS, ICC
# comments), and write a full-size and a thumbnail WebP.
#
#   tools/prepare-photo.sh SOURCE NAME          -> zh/photos/NAME.webp, zh/photos/NAME-thumb.webp
#   tools/prepare-photo.sh SOURCE banner-SEASON CROP
#                                               -> zh/photos/banner-SEASON.webp (5:1), cropped with -crop CROP
set -euo pipefail

src=$1 name=$2 crop=${3:-}
out=$(dirname "$0")/../zh/photos
mkdir -p "$out"

if [[ $name == banner-* ]]; then
  magick "$src" -auto-orient -crop "$crop" +repage -resize '1600x>' -strip -quality 80 "$out/$name.webp"
else
  magick "$src" -auto-orient -resize '1600x1600>' -strip -quality 80 "$out/$name.webp"
  magick "$src" -auto-orient -resize '600x600>' -strip -quality 75 "$out/$name-thumb.webp"
fi
