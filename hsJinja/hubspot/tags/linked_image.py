"""
linked_image tag that will mimic Hubspot {% linked_image %}
"""
from jinja2.ext import Extension


class linked_imageExtension(Extension):
    tags = {"linked_image"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
