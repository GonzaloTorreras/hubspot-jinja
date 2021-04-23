"""
rss_listing tag that will mimic Hubspot {% rss_listing %}
"""
from jinja2.ext import Extension


class rss_listingExtension(Extension):
    tags = {"rss_listing"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
