"""
related_blog_posts tag that will mimic Hubspot {% related_blog_posts %}
"""
from jinja2.ext import Extension


class related_blog_postsExtension(Extension):
    tags = {"related_blog_posts"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
