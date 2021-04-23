"""
text tag that will mimic Hubspot {% text %}
"""
from jinja2.ext import Extension


class textExtension(Extension):
    tags = {"text"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
