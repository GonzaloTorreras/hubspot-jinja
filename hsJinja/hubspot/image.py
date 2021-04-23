"""
image tag that will mimic Hubspot {% image %}
"""
from jinja2.ext import Extension


class imageExtension(Extension):
    tags = {"image"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
