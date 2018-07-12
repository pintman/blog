#!/bin/bash

FILEPATH=${1:?"give filename as first parameter"}

DIRNAME=$(dirname $FILEPATH)
# strip string content from path
DIRNAME_STRIPPED=${DIRNAME##content/}
FILENAME=$(basename $FILEPATH)

# shrink image ('>': only shrink)
convert $FILEPATH -resize 600\> $DIRNAME/small_$FILENAME

echo ".. image:: {filename}/$DIRNAME_STRIPPED/small_$FILENAME"
echo "   :target: {filename}/$DIRNAME_STRIPPED/$FILENAME"
echo "   :alt: image"
