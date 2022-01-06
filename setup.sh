#!/usr/bin/bash

# exit on error
set -e

#VERSION=4.5.3
# known stable release
#PELICAN_THEMES_RELEASE=12d89d4
#PELICAN_PLUGINS_RELEASE=d79a52ab820e0a7ea4bbf882a90b3086b367d72b

# install python packages
# beautifulsoup is needed for plugin tipue search
#pip3 install pelican==$VERSION beautifulsoup4 markdown
poetry install

# install plugins repo
test -d pelican-plugins || git clone https://github.com/getpelican/pelican-plugins

# hotfix for old plugin tipue search
pushd pelican-plugins/tipue_search/
cp pelican/plugins/tipue_search/* .
popd

# install theme repo
test -d pelican-themes || git clone https://github.com/getpelican/pelican-themes

