"""
blog_social_sharing tag that will mimic Hubspot {% blog_social_sharing %}
"""
from jinja2.ext import Extension


class blog_social_sharingExtension(Extension):
    tags = {"blog_social_sharing"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
