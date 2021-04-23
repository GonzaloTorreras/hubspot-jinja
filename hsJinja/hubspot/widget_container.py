"""
widget_container tag that will mimic Hubspot {% widget_container %}
"""
from jinja2.ext import Extension


class widget_containerExtension(Extension):
    tags = {"widget_container"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
