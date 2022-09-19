from .models import Blog
import markdown
from jinja2 import Environment, BaseLoader
from shopyo.api.assets import get_static

def get_blog_posts():
    return Blog.query.order_by(Blog.pub.desc()).all()


def render_blog_md(source):

    def ilink(asset_name):
        return get_static('blogz', asset_name)

    rtemplate = Environment(loader=BaseLoader()).from_string(source)
    data = {
        'ilink': ilink
    }
    source = rtemplate.render(**data)

    return source

def md_to_html(source):
    html = markdown.markdown(source, extensions=["extra", "smarty", "meta"])
    return html


# global templates variables in here
available_everywhere = {
'len': len,
    'render_blog_md': render_blog_md,
    'get_blog_posts': get_blog_posts,
    'md_to_html': md_to_html
}

# global configs in here, defined by profile
# configs = {
#     "development": {
#         "CONFIG_VAR": "DEVVALUE"
#     },
#     "production": {
#         "CONFIG_VAR": "PRODVALUE"
#     },
#     "testing": {
#         "CONFIG_VAR": "TESTVALUE"
#     }
# }
