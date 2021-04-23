"""
language_switcher tag that will mimic Hubspot {% language_switcher %}
"""
from jinja2.ext import Extension


class language_switcherExtension(Extension):
    tags = {"language_switcher"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
