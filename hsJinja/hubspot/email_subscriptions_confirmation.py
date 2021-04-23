"""
email_subscriptions_confirmation tag that will mimic Hubspot {% email_subscriptions_confirmation %}
"""
from jinja2.ext import Extension


class email_subscriptions_confirmationExtension(Extension):
    tags = {"email_subscriptions_confirmation"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
