"""
require_css tag that will mimic Hubspot {% require_css %}
"""
from jinja2.ext import Extension


class require_cssExtension(Extension):
    tags = {"require_css", "end_require_css"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
