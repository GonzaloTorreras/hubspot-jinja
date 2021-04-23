"""
post_filter tag that will mimic Hubspot {% post_filter %}
"""
from jinja2.ext import Extension


class post_filterExtension(Extension):
    tags = {"post_filter"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
