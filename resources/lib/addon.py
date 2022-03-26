# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

from urllib.parse import urlparse

import os
import json

import routing
import xbmcaddon
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setContent

import feedparser

plugin = routing.Plugin()  # pylint: disable=invalid-name
addon = xbmcaddon.Addon('plugin.video.youtube-rss')  # pylint: disable=invalid-name

real_path = os.path.realpath(__file__)
feedfile = os.path.join(os.path.dirname(real_path), '../..', 'subscriptions.json')

FEEDS = json.load(open(feedfile))


@plugin.route('/')
def main_menu():
    for name, url in FEEDS.items():
        url = plugin.url_for(show_dir, subdir=name)
        addDirectoryItem(plugin.handle, url, ListItem(name), True)
    setContent(plugin.handle, 'videos')
    endOfDirectory(plugin.handle)


@plugin.route('/dir/<path:subdir>')
def show_dir(subdir=''):
    if subdir:
        feed = feedparser.parse(FEEDS[subdir])
        for entry in feed.entries[:10]:
            parsed = urlparse(entry.link)
            # query='v=IR-hhat34LI'
            ytid = parsed.query.replace('v=', '')
            url = 'plugin://plugin.video.youtube/play/?video_id={}'.format(ytid)

            item = ListItem(entry.title)
            item.setProperty('IsPlayable', 'true')
            item.setInfo('video', {
                'plot': entry.description,
            })
            addDirectoryItem(plugin.handle, url, item, False)
            setContent(plugin.handle, 'videos')

    endOfDirectory(plugin.handle)


def run(argv):
    """Addon entry point from wrapper"""
    plugin.run(argv)
