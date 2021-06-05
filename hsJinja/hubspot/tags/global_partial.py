"""
global_partial tag that will mimic Hubspot {% global_partial %}
"""
from jinja2.ext import Extension


class global_partialExtension(Extension):
    tags = set(["global_partial"])

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
