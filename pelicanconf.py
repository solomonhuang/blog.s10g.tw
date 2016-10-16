#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Solomon Huang'
SITENAME = 'Solomon\'s Notebook'
SITEURL = ''
SITELOGO = 'https://www.gravatar.com/avatar/09a35c0d580bf63af7dac9bbbd76e0a6?s=200'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
ARTICLE_EXCLUDES = ['drafts']

try:
    if os.environ['CI'] == 'true':
        PLUGIN_PATH = ['../pelican-plugins']
    else:
        PLUGIN_PATH = ['../pelican-plugins']
except KeyError:
    PLUGIN_PATH = ['../pelican-plugins']

PLUGINS = ['liquid_tags.graphviz']

MAIN_MENU = True


TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'
HTML_LANG = 'zh'
THEME = 'themes/flex'
OG_LOCALE = 'zh_TW'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = ()
LINKS = (('多國超快 VPN', 'https://goo.gl/VO3IuK'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = (('github', 'https://github.com/solomonhuang/'),
          ('twitter', 'https://twitter.com/solomonhuang/'),
          ('linkedin', 'https://tw.linkedin.com/in/solomon-huang-4074b356'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'


STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

MENUITEMS = [
    # ('home', '/index'),
    ('Categories', '/categories'),
    ('Archives', '/archives'),
    ('Tags', '/tags'),
    # ('search', 'search'),
    # ('authors', 'authors'),
    # ('about', 'about'),
]

