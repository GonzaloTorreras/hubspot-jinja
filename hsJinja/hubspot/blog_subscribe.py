"""
blog_subscribe tag that will mimic Hubspot {% blog_subscribe %}
"""
from jinja2.ext import Extension


class blog_subscribeExtension(Extension):
    tags = {"blog_subscribe"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
