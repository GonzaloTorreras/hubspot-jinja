"""
simple_menu tag that will mimic Hubspot {% simple_menu %}
"""
from jinja2.ext import Extension


class simple_menuExtension(Extension):
    tags = {"simple_menu"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
