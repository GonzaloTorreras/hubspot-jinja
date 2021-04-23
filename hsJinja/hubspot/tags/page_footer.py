"""
page_footer tag that will mimic Hubspot {% page_footer %}
"""
from jinja2.ext import Extension


class page_footerExtension(Extension):
    tags = {"page_footer"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
