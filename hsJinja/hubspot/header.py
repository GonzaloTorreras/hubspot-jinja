"""
header tag that will mimic Hubspot {% header %}
"""
from jinja2.ext import Extension


class headerExtension(Extension):
    tags = {"header"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
