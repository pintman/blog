#!/bin/bash

# This script sets up the Pelican environment by installing required plugins and themes.
# It is used by the github action to prepare the environment for building the site.

# git hashes as of 2025-10-2
PLUGINS_VERSION=216d1ddb5cf5dc8f5a308d1b1554102013ff7c79
THEMES_VERSION=90beb1272fe1eef58b0432ad2fa4890847e2283b

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
