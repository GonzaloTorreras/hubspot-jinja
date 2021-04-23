"""
menu tag that will mimic Hubspot {% menu %}
"""
from jinja2.ext import Extension


class menuExtension(Extension):
    tags = {"menu"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
