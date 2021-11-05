#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Savaton'
SITENAME = u'Sozi'
SITEURL = 'https://sozi.baierouge.fr'
GITHUB_URL = 'https://github.com/sozi-projects/Sozi'
# PIWIK_URL = 'http://baierouge.fr/piwik'
# PIWIK_SITE = '2'
TIMEZONE = 'Europe/Paris'
KEYWORDS = 'presentation,slideshow,SVG,vector graphics,animation,office software'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Inkscape', 'http://inkscape.org/'),
)

# Social widget
SOCIAL = (
    ('Mastodon', 'https://mamot.fr/@aumouvantsillage'),
    ('Twitter', 'https://twitter.com/umouvantsillage'),
    # TODO add YouTube
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/sozi'

ARTICLE_EXCLUDES = ['wiki', 'presentations']

STATIC_PATHS = ['images', 'Releases', 'extra/favicon.ico', 'wiki', 'presentations']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.toc": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    }
}
