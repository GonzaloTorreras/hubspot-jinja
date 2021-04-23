"""
gallery tag that will mimic Hubspot {% gallery %}
"""
from jinja2.ext import Extension


class galleryExtension(Extension):
    tags = {"gallery"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
