"""
raw_html tag that will mimic Hubspot {% raw_html %}
"""
from jinja2.ext import Extension


class raw_htmlExtension(Extension):
    tags = {"raw_html"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
