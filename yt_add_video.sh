#!/bin/bash

# fail fast
set -o errexit

VIDID=${1?"need video id"}
URL=https://img.youtube.com/vi/$VIDID/hqdefault.jpg
YEAR=$(date +"%Y")
MONTH=$(date +"%m")
IMGPATH="content/images/$YEAR/$MONTH"


mkdir -p $IMGPATH
wget -O $IMGPATH/$VIDID.jpg $URL

echo "Add to article:"
echo ".. image:: $IMGPATH/$VIDID.jpg"
echo "   :target: https://www.youtube-nocookie.com/embed/${VIDID}?rel=0"
