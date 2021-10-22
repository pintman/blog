#!/bin/bash

IN=${1?"File missing"}
OUT=$IN-dithered.png
WIDTH=1000
COLORS=32

echo "Convert $IN"
echo "Resize to new width $WIDTH"
echo "using $COLORS colors"
echo "New file name $OUT"

convert $1 -resize $WIDTH -dither FloydSteinberg -colors $COLORS $OUT
