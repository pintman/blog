#!/bin/sh

# install python packages
pip3 install pelican beautifulsoup4 markdown

# install plugins repo
test -d pelican-plugins || git clone https://github.com/getpelican/pelican-plugins

# install theme repo
test -d pelican-themes || git clone https://github.com/getpelican/pelican-themes
# FIX: for theme pelican-bootstrap3
git -C pelican-themes checkout be36234
