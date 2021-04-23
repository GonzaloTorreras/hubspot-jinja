"""
space tag that will mimic Hubspot {% space %}
"""
from jinja2.ext import Extension


class spaceExtension(Extension):
    tags = {"space"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
