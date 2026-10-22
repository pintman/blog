#!/bin/bash
set -euo pipefail

IN=${1?"File missing"}
WIDTH=${2:-1000}
COLORS=${3:-32}
OUT="${IN%.*}-dithered.png"

[[ -f "$IN" ]] || { echo "File not found: $IN" >&2; exit 1; }

if command -v magick >/dev/null; then
    IM=magick
elif command -v convert >/dev/null; then
    IM=convert
else
    echo "ImageMagick not installed" >&2
    exit 1
fi

if [[ -e "$OUT" ]]; then
    read -r -p "$OUT exists. Overwrite? [y/N] " answer
    [[ "$answer" =~ ^[yYjJ]$ ]] || exit 1
fi

echo "Convert $IN"
echo "Resize to max width $WIDTH"
echo "using $COLORS colors"
echo "New file name $OUT"

"$IM" "$IN" -strip -resize "${WIDTH}x>" -dither FloydSteinberg -colors "$COLORS" "$OUT"
