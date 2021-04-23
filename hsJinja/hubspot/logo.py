"""
logo tag that will mimic Hubspot {% logo %}
"""
from jinja2.ext import Extension


class logoExtension(Extension):
    tags = {"logo"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
