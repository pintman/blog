#!/bin/sh

VERSION=3.7.1

# install python packages
# beautifulsoup is needed for plugin tipue search
pip3 install pelican==$VERSION beautifulsoup4 markdown

# install plugins repo
test -d pelican-plugins || git clone https://github.com/getpelican/pelican-plugins

# install theme repo
test -d pelican-themes || git clone https://github.com/getpelican/pelican-themes
# FIX: for theme pelican-bootstrap3
git -C pelican-themes checkout be36234

# setup pelican comment system
THEMEDIR=pelican-themes/pelican-bootstrap3
PCSDIR=pelican-plugins/pelican_comment_system
mkdir -p  $THEMEDIR/templates/pcs
mkdir -p $THEMEDIR/static/js
cp $PCSDIR/theme/templates/pcs/comments.html $THEMEDIR/templates/pcs/comments.html
cp $PCSDIR/theme/static/js/comments.js      $THEMEDIR/static/js/comments.js
# copy local version of article template
cp theme.local/article.html $THEMEDIR/templates/
