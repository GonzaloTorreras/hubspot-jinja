"""
color tag that will mimic Hubspot {% color %}
"""
from jinja2.ext import Extension


class colorExtension(Extension):
    tags = {"color"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
