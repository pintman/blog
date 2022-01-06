#!/bin/bash

# exit on error
set -e

# install python packages
poetry install

# install plugins repo
test -d pelican-plugins || git clone https://github.com/getpelican/pelican-plugins

# hotfix for old plugin tipue search
pushd pelican-plugins/tipue_search/
cp -v pelican/plugins/tipue_search/* .
popd

# install theme repo
test -d pelican-themes || git clone https://github.com/getpelican/pelican-themes

