"""
cta tag that will mimic Hubspot {% cta %}
"""
from jinja2.ext import Extension


class ctaExtension(Extension):
    tags = {"cta"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
