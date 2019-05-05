#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Catling'
SITENAME = "Tom's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

SITEURL = 'http://localhost:8000'

THEME = '/Users/tomcatling/git/tomcatling.github.io/theme/elegant'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'images/gallery']

THEME_TEMPLATES_OVERRIDES = ['/Users/tomcatling/git/tomcatling.github.io/templates']

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS = 'categories.html'

TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('GitHub', 'https://github.com/tomcatling'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/Users/tomcatling/git/pelican-plugins']
PLUGINS = ['gallery']