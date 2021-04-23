"""
social_sharing tag that will mimic Hubspot {% social_sharing %}
"""
from jinja2.ext import Extension


class social_sharingExtension(Extension):
    tags = {"social_sharing"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
