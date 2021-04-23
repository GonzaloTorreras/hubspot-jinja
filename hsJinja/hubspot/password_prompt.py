"""
password_prompt tag that will mimic Hubspot {% password_prompt %}
"""
from jinja2.ext import Extension


class password_promptExtension(Extension):
    tags = {"password_prompt"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
