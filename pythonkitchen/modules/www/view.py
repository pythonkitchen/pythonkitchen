import json
import os

from flask import Blueprint
from flask import render_template

from shopyo.api.module import ModuleHelp
from shopyo.api.templates import yo_render
from modules.blogz.models import Blog

# from flask import url_for
# from flask import redirect
# from flask import flash
# from flask import request
#
# from shopyo.api.html import notify_success
# from shopyo.api.forms import flash_errors
# from shopyo.api.enhance import get_active_theme_dir
# from shopyo.api.enhance import get_setting
# from modules.box__ecommerce.shop.helpers import get_cart_data

mhelp = ModuleHelp(__file__, __name__)
globals()[mhelp.blueprint_str] = mhelp.blueprint
module_blueprint = globals()[mhelp.blueprint_str]

from modules.blogz.models import Blog
# @module_blueprint.route("/")
# def index():
#     # cant be defined above but must be manually set each time
#     # active_theme_dir = os.path.join(
#     #     dirpath, "..", "..", "themes", get_setting("ACTIVE_FRONT_THEME")
#     # )
#     # module_blueprint.template_folder = active_theme_dir

#     # return str(module_blueprint.template_folder)

#     # return render_template(get_setting("ACTIVE_FRONT_THEME") + "/index.html")

#     return render_template("www/index.html", get_static=get_static)


# from shopyo.api.assets import get_static


# @module_blueprint.route("/render_demo")
# def render_demo():
#     context = {"fruit": "mango"}
#     return yo_render("blogus/render_demo.html", context)
robots_txt = '''

User-agent: Googlebot
Disallow: /nogooglebot/

User-agent: *
Allow: /

Sitemap: http://www.pythonkitchen.com/sitemap.xml
'''



@module_blueprint.route("/")
@module_blueprint.route("/<slug>")
def index(slug=None):
    # cant be defined above but must be manually set each time
    # active_theme_dir = os.path.join(
    #     dirpath, "..", "..", "themes", get_setting("ACTIVE_FRONT_THEME")
    # )
    # module_blueprint.template_folder = active_theme_dir

    # return str(module_blueprint.template_folder)

    # return render_template(get_setting("ACTIVE_FRONT_THEME") + "/index.html")

    if slug is None:
        return render_template("www/index.html", str=str)
    elif slug == 'robots.txt':
        return robots_txt
    elif slug == 'sitemap.xml':
        urls = []
        posts = Blog.query.all()
        for post in posts:
            slug = post.slug
            pub = str(post.pub)
            urls.append(f'''
        <url>
            <loc>http://www.pythonkitchen.com/{slug}</loc>
            <lastmod>{pub}</lastmod>
        </url>
                ''')

        url_str = '\n'.join(urls)
        sitemap_xml = f'''
        <?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          {url_str}
        </urlset>
        '''
        return sitemap_xml
    else:
        current_post = Blog.query.filter(Blog.slug == slug).first()
        return render_template('blogz/post.html', current_post=current_post)