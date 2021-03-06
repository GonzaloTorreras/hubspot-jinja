from os import path, walk, getcwd
import glob

from jinja2 import Environment
#from jinja2.loaders import PackageLoader
from jinja2.loaders import FileSystemLoader
from jinja2.utils import select_autoescape

from jinja2 import TemplateNotFound
from jinja2 import TemplateSyntaxError

from .hubspot.tags.blog_comments import blog_commentsExtension
from .hubspot.tags.blog_social_sharing import blog_social_sharingExtension
from .hubspot.tags.blog_subscribe import blog_subscribeExtension
from .hubspot.tags.boolean import booleanExtension
from .hubspot.tags.choice import choiceExtension
from .hubspot.tags.color import colorExtension
from .hubspot.tags.cta import ctaExtension
from .hubspot.tags.email_simple_subscription import email_simple_subscriptionExtension
from .hubspot.tags.email_subscriptions import email_subscriptionsExtension
from .hubspot.tags.email_subscriptions_confirmation import email_subscriptions_confirmationExtension
from .hubspot.tags.form import formExtension
from .hubspot.tags.gallery import galleryExtension
from .hubspot.tags.global_partial import global_partialExtension
from .hubspot.tags.header import headerExtension
from .hubspot.tags.icon import iconExtension
from .hubspot.tags.image_src import image_srcExtension
from .hubspot.tags.image import imageExtension
from .hubspot.tags.language_switcher import language_switcherExtension
from .hubspot.tags.linked_image import linked_imageExtension
from .hubspot.tags.logo import logoExtension
from .hubspot.tags.menu import menuExtension
from .hubspot.tags.module import moduleExtension
from .hubspot.tags.page_footer import page_footerExtension
from .hubspot.tags.password_prompt import password_promptExtension
from .hubspot.tags.post_filter import post_filterExtension
from .hubspot.tags.post_listing import post_listingExtension
from .hubspot.tags.raw_html import raw_htmlExtension
from .hubspot.tags.related_blog_posts import related_blog_postsExtension
from .hubspot.tags.require_css import require_cssExtension
from .hubspot.tags.require_head import require_headExtension
from .hubspot.tags.require_js import require_jsExtension
from .hubspot.tags.rich_text import rich_textExtension
from .hubspot.tags.rss_listing import rss_listingExtension
from .hubspot.tags.section_header import section_headerExtension
from .hubspot.tags.simple_menu import simple_menuExtension
from .hubspot.tags.social_sharing import social_sharingExtension
from .hubspot.tags.space import spaceExtension
from .hubspot.tags.text import textExtension
from .hubspot.tags.textarea import textareaExtension
from .hubspot.tags.videoplayer import video_playerExtension
from .hubspot.tags.widget_container import widget_containerExtension

class hsJinja(object):
    def __init__(self,templates,output):
        self.template_folder = templates
        self.templates = self.listTemplates()
        print("List of templates found:", self.templates)

        self.output = output

        self.env = self.loadJinjaEnv()
        print("Jinja2 ENV loaded!")
        #print(self.env.list_templates())
    def main(self):
        print("Running!")
        
        for template in self.templates:
            self.renderJinja(template)

    def listTemplates(self):
        
        files = list()
        for (dirpath,dirnames,filenames) in walk(self.template_folder):
            files += [path.join(dirpath.replace(self.template_folder,""),file) for file in filenames]
        return files

    def loadJinjaEnv(self):
        env = Environment(
            #loader=PackageLoader('hsJinja',self.template_folder),
            loader=FileSystemLoader(searchpath=self.template_folder),
            extensions=["jinja2.ext.do",
                        blog_commentsExtension,
                        blog_social_sharingExtension,
                        blog_subscribeExtension,
                        booleanExtension,
                        choiceExtension,
                        colorExtension,
                        ctaExtension,
                        email_simple_subscriptionExtension,
                        email_subscriptionsExtension,
                        email_subscriptions_confirmationExtension,
                        formExtension,
                        galleryExtension,
                        global_partialExtension,
                        headerExtension,
                        iconExtension,
                        image_srcExtension,
                        imageExtension,
                        language_switcherExtension,
                        linked_imageExtension,
                        logoExtension,
                        menuExtension,
                        moduleExtension,
                        page_footerExtension,
                        password_promptExtension,
                        post_filterExtension,
                        post_listingExtension,
                        raw_htmlExtension,
                        related_blog_postsExtension,
                        require_cssExtension,
                        require_headExtension,
                        require_jsExtension,
                        rich_textExtension,
                        rss_listingExtension,
                        section_headerExtension,
                        simple_menuExtension,
                        social_sharingExtension,
                        spaceExtension,
                        textExtension,
                        textareaExtension,
                        video_playerExtension,
                        widget_containerExtension
            ],
            autoescape=select_autoescape(["html","xml"]),
            auto_reload=True,
            cache_size=0 #disable cache so it rebuilds when watching for changes
        )
        env.trim_blocks = True
        env.lstrip_blocks = True
        env.strip_trailing_newlines = True
        print(self.template_folder)
        return env

    def renderJinja(self,template="base.html"):
        try:
            render = self.env.get_template(template)
        except TemplateNotFound:
            import sys
            print("Error, can't find the template: " + template)
            print(sys.exc_info())
            return False
        except TemplateSyntaxError as e:
            print(
                "Jinja2 template syntax error during render: {}:{} error: {}".
                format(e.filename, e.lineno, e.message))
            raise e
        

    
