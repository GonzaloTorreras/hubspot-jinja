"""
form tag that will mimic Hubspot {% form %}
"""
from jinja2.ext import Extension


class formExtension(Extension):
    tags = {"form"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
