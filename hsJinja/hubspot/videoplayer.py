"""
video_player tag that will mimic Hubspot {% video_player %}
"""
from jinja2.ext import Extension


class video_playerExtension(Extension):
    tags = {"video_player"}

    def __init__(self, environment):
        pass

    def parse(self, parser):
        pass
