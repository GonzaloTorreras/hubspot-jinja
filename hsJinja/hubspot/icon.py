"""
icon tag that will mimic Hubspot {% icon %}
"""
from jinja2.ext import Extension


class iconExtension(Extension):
    tags = {"icon"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
