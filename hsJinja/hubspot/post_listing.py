"""
post_listing tag that will mimic Hubspot {% post_listing %}
"""
from jinja2.ext import Extension


class post_listingExtension(Extension):
    tags = {"post_listing"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
