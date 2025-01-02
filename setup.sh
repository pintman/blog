#!/bin/bash

# git hashes as of 2022-01-07
PLUGINS_VERSION=483215d2e1998684b7f413b6b1c8e26058fd2e6b
THEMES_VERSION=565cb3fb8c88f1089502dc82a70fda5a7c7b322e

# exit on error
set -e

# update python packages
poetry update

# install plugins repo
test -d pelican-plugins || git clone https://github.com/getpelican/pelican-plugins
git  -C pelican-plugins checkout $PLUGINS_VERSION

echo "hotfix for old plugin tipue search"
pushd pelican-plugins/tipue_search/
cp -v pelican/plugins/tipue_search/* .
popd

# install theme repo
test -d pelican-themes || git clone https://github.com/getpelican/pelican-themes
git  -C pelican-themes checkout $THEMES_VERSION

cp -v theme.local/* pelican-themes/pelican-bootstrap3/templates
