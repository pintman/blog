#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marco Bakera'
SITENAME = '/home/bakera/blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'media', 'extra/CNAME', 'extra/favicon.ico']  
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
DEFAULT_CATEGORY = 'Sonstiges'
DISPLAY_CATEGORIES_ON_MENU = False
"""
MENUITEMS = (
    ("Archiv", "https://blog.bakera.de/archives.html"),
    ("Tags", "https://blog.bakera.de//tags.html"))
"""

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
"""
LINKS = (('Archiv', 'archives.html'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""
# Social widget
SOCIAL = (
    ("twitter", "https://www.twitter.com/pintman"),
    ("github", "https://github.com/pintman"),
    ("github TBS1", "https://github.com/tbs1-bo", "github"),
    ("gitlab", "https://gitlab.com/pintman", "git"),
    ("edugit", "https://edugit.org/bak", "git"))



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#THEME = "simple"
#THEME = "notmyidea"

# Theme pelican-bootstrap3
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
#
# FIX: theme needs 'git checkout be36234'
THEME = "pelican-themes/pelican-bootstrap3"
#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#I18N_TEMPLATES_LANG = 'en'
#GITHUB_REPO_COUNT = 5
#GITHUB_USER = "pintman"
#GITHUB_SHOW_USER_LINK = True
#GITHUB_SKIP_FORK = True
#PADDED_SINGLE_COLUMN_STYLE = True
#DISPLAY_TAGS_ON_SIDEBAR = True
#DISPLAY_ARCHIVE_ON_SIDEBAR = True
#HIDE_SIDEBAR = True
#PLUGINS = ['tipue_search']

# Theme pelican-elegant
#
# http://oncrashreboot.com/elegant-best-pelican-theme-features
#THEME = "pelican-elegant"
#
# settings suggested in doc:
#
#PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
#DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
#STATIC_PATHS = ['theme/images', 'images']
#TAG_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''
#AUTHOR_SAVE_AS = ''

# Install all plugins there
# git clone --recursive https://github.com/getpelican/pelican-plugins
# 
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['tipue_search', "sitemap"]
#DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
DIRECT_TEMPLATES = ('index', 'archives', 'search')
# Sitemap
# https://github.com/getpelican/pelican-plugins/tree/master/sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.9,
        "pages": 0.2,
        "indexes": 0.8
    },
    "changefreqs": {
        # values: always, hourly, daily, weekly, monthly, yearly and never
        "articles": "weekly",
        "pages": "monthly",
        "indexes": "daily"
    }
}
