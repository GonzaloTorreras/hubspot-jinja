"""
choice tag that will mimic Hubspot {% choice %}
"""
from jinja2.ext import Extension


class choiceExtension(Extension):
    tags = {"choice"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
