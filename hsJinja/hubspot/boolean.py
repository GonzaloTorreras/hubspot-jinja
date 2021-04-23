"""
boolean tag that will mimic Hubspot {% boolean %}
"""
from jinja2.ext import Extension


class booleanExtension(Extension):
    tags = {"boolean"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
