"""
rich_text tag that will mimic Hubspot {% rich_text %}
"""
from jinja2.ext import Extension


class rich_textExtension(Extension):
    tags = {"rich_text"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
