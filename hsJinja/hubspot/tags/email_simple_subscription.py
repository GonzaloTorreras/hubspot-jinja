"""
email_simple_subscription tag that will mimic Hubspot {% email_simple_subscription %}
"""
from jinja2.ext import Extension


class email_simple_subscriptionExtension(Extension):
    tags = {"email_simple_subscription"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
