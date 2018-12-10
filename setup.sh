#!/bin/sh

VERSION=3.7.1
# known stable release
#PELICAN_THEMES_RELEASE=12d89d4
#PELICAN_PLUGINS_RELEASE=d79a52ab820e0a7ea4bbf882a90b3086b367d72b

# new release - produces error
#VERSION=4.0.1

# install python packages
# beautifulsoup is needed for plugin tipue search
# pillow is needed for pelican comment system (for generating identicons)
pip3 install pelican==$VERSION beautifulsoup4 markdown pillow

# install plugins repo
test -d pelican-plugins || git clone https://github.com/getpelican/pelican-plugins

# install theme repo
test -d pelican-themes || git clone https://github.com/getpelican/pelican-themes

# setup pelican comment system
# https://github.com/getpelican/pelican-plugins/tree/master/pelican_comment_system
#
THEMEDIR=pelican-themes/pelican-bootstrap3
PCSDIR=pelican-plugins/pelican_comment_system
mkdir -p  $THEMEDIR/templates/pcs
mkdir -p $THEMEDIR/static/js
cp $PCSDIR/theme/templates/pcs/comments.html $THEMEDIR/templates/pcs/comments.html
cp $PCSDIR/theme/static/js/comments.js      $THEMEDIR/static/js/comments.js
# copy local version of article template
cp theme.local/article.html $THEMEDIR/templates/
