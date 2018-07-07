#!/bin/bash

# fail fast
set -o errexit

VIDID=${1?"need video id"}
URL=https://img.youtube.com/vi/$VIDID/hqdefault.jpg
YEAR=$(date +"%Y")
MONTH=$(date +"%m")
IMGPATH1="images/$YEAR/$MONTH"
IMGPATH2="content/$IMGPATH1"


mkdir -p $IMGPATH2
wget -O $IMGPATH2/ytthumb_$VIDID.jpg $URL

echo "Add to article:"
echo ".. image:: $IMGPATH1/ytthumb_$VIDID.jpg"
echo "   :alt: Youtube-Video"
echo "   :target: https://www.youtube-nocookie.com/embed/${VIDID}?rel=0"
