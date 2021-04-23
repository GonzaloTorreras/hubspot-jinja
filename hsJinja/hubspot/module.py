"""
Module tag that will mimic Hubspot {% module %}
"""
from jinja2.ext import Extension

class moduleExtension(Extension):
    tags = {"module"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
