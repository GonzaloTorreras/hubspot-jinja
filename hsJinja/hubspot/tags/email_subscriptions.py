"""
email_subscriptions tag that will mimic Hubspot {% email_subscriptions %}
"""
from jinja2.ext import Extension


class email_subscriptionsExtension(Extension):
    tags = {"email_subscriptions"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
