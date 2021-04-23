"""
section_header tag that will mimic Hubspot {% section_header %}
"""
from jinja2.ext import Extension


class section_headerExtension(Extension):
    tags = {"section_header"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
