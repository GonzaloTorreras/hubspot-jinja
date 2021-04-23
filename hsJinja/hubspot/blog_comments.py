"""
blog_comments tag that will mimic Hubspot {% blog_comments %}
"""
from jinja2.ext import Extension


class blog_commentsExtension(Extension):
    tags = {"blog_comments"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
