"""
image_src tag that will mimic Hubspot {% image_src %}
"""
from jinja2.ext import Extension


class image_srcExtension(Extension):
    tags = {"image_src"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
