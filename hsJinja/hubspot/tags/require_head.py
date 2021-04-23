"""
require_head tag that will mimic Hubspot {% require_head %}
"""
from jinja2.ext import Extension


class require_headExtension(Extension):
    tags = {"require_head","end_require_head"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
