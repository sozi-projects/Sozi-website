#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Savaton'
SITENAME = u'Sozi'
SITEURL = ''
GITHUB_URL = 'https://github.com/senshu/Sozi'
PIWIK_URL = 'http://baierouge.fr/piwik'
PIWIK_SITE = '2'
TIMEZONE = 'Europe/Paris'

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
    ('Mastodon', 'https://mamot.fr/@senshu'),
    ('Twitter', 'https://twitter.com/senshua'),
    ('Facebook', 'https://www.facebook.com/sozi.project'),
    # TODO add YouTube
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/sozi'

ARTICLE_EXCLUDES = ['wiki', 'presentations']

STATIC_PATHS = ['images', 'releases', 'extra/favicon.ico', 'wiki', 'presentations']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

MD_EXTENSIONS = ["codehilite(css_class=highlight)", "headerid", "extra", "meta"]
