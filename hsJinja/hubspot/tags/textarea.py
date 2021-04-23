"""
textarea tag that will mimic Hubspot {% textarea %}
"""
from jinja2.ext import Extension


class textareaExtension(Extension):
    tags = {"textarea"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
