from os.path import dirname, basename, isfile, join
import glob

from jinja2 import Environment
from jinja2.loaders import PackageLoader
from jinja2.utils import select_autoescape

from .hubspot.blog_comments import blog_commentsExtension
from .hubspot.blog_social_sharing import blog_social_sharingExtension
from .hubspot.blog_subscribe import blog_subscribeExtension
from .hubspot.boolean import booleanExtension
from .hubspot.choice import choiceExtension
from .hubspot.color import colorExtension
from .hubspot.cta import ctaExtension
from .hubspot.email_simple_subscription import email_simple_subscriptionExtension
from .hubspot.email_subscriptions import email_subscriptionsExtension
from .hubspot.email_subscriptions_confirmation import email_subscriptions_confirmationExtension
from .hubspot.form import formExtension
from .hubspot.gallery import galleryExtension
from .hubspot.header import headerExtension
from .hubspot.icon import iconExtension
from .hubspot.image_src import image_srcExtension
from .hubspot.image import imageExtension
from .hubspot.language_switcher import language_switcherExtension
from .hubspot.linked_image import linked_imageExtension
from .hubspot.logo import logoExtension
from .hubspot.menu import menuExtension
from .hubspot.module import moduleExtension
from .hubspot.page_footer import page_footerExtension
from .hubspot.password_prompt import password_promptExtension
from .hubspot.post_filter import post_filterExtension
from .hubspot.post_listing import post_listingExtension
from .hubspot.raw_html import raw_htmlExtension
from .hubspot.related_blog_posts import related_blog_postsExtension
from .hubspot.require_css import require_cssExtension
from .hubspot.require_head import require_headExtension
from .hubspot.require_js import require_jsExtension
from .hubspot.rich_text import rich_textExtension
from .hubspot.rss_listing import rss_listingExtension
from .hubspot.section_header import section_headerExtension
from .hubspot.simple_menu import simple_menuExtension
from .hubspot.social_sharing import social_sharingExtension
from .hubspot.space import spaceExtension
from .hubspot.text import textExtension
from .hubspot.textarea import textareaExtension
from .hubspot.videoplayer import video_playerExtension
from .hubspot.widget_container import widget_containerExtension

class hsJinja(object):
    def __init__(self,templatesFolder = "templates"):
        self.template_folder = templatesFolder
        self.env = self.loadJinjaEnv()

    def main(self):
        print("Running!")

    def loadJinjaEnv(self):
        env = Environment(
            loader=PackageLoader('hsJinja',{
                "template_folder":  self.template_folder
            }),
            extensions=["jinja2.ext.do",
                blog_commentsExtension
            ],
            autoescape=select_autoescape(["html","xml"]),
            auto_reload=True,
            cache_size=0 #disable cache so it rebuilds when watching for changes
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        env.strip_trailing_newlines = True

        return env

    def render(self,page):
        pass
    
