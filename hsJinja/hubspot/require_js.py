"""
require_js tag that will mimic Hubspot {% require_js %}
"""
from jinja2.ext import Extension


class require_jsExtension(Extension):
    tags = {"require_js","end_require_js"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
