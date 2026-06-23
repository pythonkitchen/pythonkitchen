import argparse
from os.path import join

from livereload import Server

import settings
from jamstack.api.template import generate
from datetime import datetime
from logic import generate_blog_posts
from logic import get_posts
from logic import build_toc
from logic import slugify
import calendar 
import toml
import os


from functools import wraps 

def clean_text(raw_html):
    from bs4 import BeautifulSoup
    cleantext = BeautifulSoup(raw_html, "lxml").text
    return cleantext

def format_post_date(date):
    dateobj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    year = dateobj.year
    month = calendar.month_name[dateobj.month]
    day = dateobj.day
    return f'{month} {day}, {year}'

def reading_time(html, wpm=220):
    words = len(clean_text(html).split())
    mins = max(1, round(words / wpm))
    return f'{mins} min read'

def get_author_info(key):
    infos = {}
    for author_file in os.listdir(settings.AUTHORS_PATH):
        author_slug = author_file.split(".")[0]
        with open(os.path.join(settings.AUTHORS_PATH, f'{author_file}')) as f:
            info = toml.load(f)
            # Index by filename slug
            infos[author_slug] = info
            # Index by name (case-insensitive and slugified)
            name = info['base']['name']
            infos[name] = info
            infos[name.lower().replace(' ', '-')] = info
    
    if key in infos:
        return infos[key]
    
    # Fallback to case-insensitive search if direct key fails
    for k in infos:
        if k.lower() == key.lower():
            return infos[k]
            
    return infos[key] # Will still raise KeyError if totally missing

def get_related_posts(post, all_posts):
    if not post.get('related_posts'):
        return []
    
    posts_map = {p['slug']: p for p in all_posts}
    related = []
    for slug in post['related_posts']:
        if slug in posts_map:
            related.append(posts_map[slug])
    
    # Fill with latest if less than 3
    if len(related) < 3:
        for p in all_posts:
            if p['slug'] != post['slug'] and p not in related:
                related.append(p)
            if len(related) >= 3:
                break
    return related[:3]

POSTS_PER_PAGE = 12

def generate_category_pages(posts, base_context):
    """Generate /category/<slug>/ index pages, interlinked."""
    from collections import OrderedDict
    by_cat = OrderedDict()
    for post in posts:
        for i, name in enumerate(post['categories']):
            slug = post['category_slugs'][i]
            by_cat.setdefault(slug, {'name': name, 'posts': []})['posts'].append(post)

    other_cats = [{'slug': s, 'name': v['name']} for s, v in by_cat.items()]
    for slug, data in by_cat.items():
        ctx = dict(base_context)
        ctx.update({
            'category_slug': slug,
            'category_name': data['name'],
            'category_posts': data['posts'],
            'other_categories': other_cats,
        })
        out_dir = join(settings.OUTPUT_FOLDER, 'category', slug)
        os.makedirs(out_dir, exist_ok=True)
        generate('category.html', join(out_dir, 'index.html'), context=ctx)


def generate_paginated_home(posts, base_context):
    """Split the homepage into /, /page/2/, /page/3/ ... with prev/next links."""
    import math
    total = len(posts)
    pages = max(1, math.ceil(total / POSTS_PER_PAGE))

    for p in range(1, pages + 1):
        ctx = dict(base_context)
        page_posts = posts[(p - 1) * POSTS_PER_PAGE: p * POSTS_PER_PAGE]
        ctx.update({
            'posts': page_posts,
            'page': p,
            'total_pages': pages,
            'total_posts': total,
        })
        if p == 1:
            generate('index.html', join(settings.OUTPUT_FOLDER, 'index.html'), context=ctx)
        else:
            out_dir = join(settings.OUTPUT_FOLDER, 'page', str(p))
            os.makedirs(out_dir, exist_ok=True)
            generate('index.html', join(out_dir, 'index.html'), context=ctx)


def generate_site():
    extra_context = {"info": settings.info, "posts": get_posts(settings), 
                     "clean_text": clean_text, "format_post_date": format_post_date,
                     "get_author_info": get_author_info,
                     "get_related_posts": get_related_posts,
                     "reading_time": reading_time,
                     "build_toc": build_toc,
                     "slugify": slugify,
                     "year": datetime.now().year}
    
    all_posts = extra_context["posts"]

    # Unique categories for sitemap + interlinking
    from collections import OrderedDict
    cats = OrderedDict()
    for post in all_posts:
        for i, name in enumerate(post['categories']):
            cats[post['category_slugs'][i]] = name
    extra_context['categories'] = [{'slug': s, 'name': n} for s, n in cats.items()]

    generate('sitemap.html', join(settings.OUTPUT_FOLDER, 'sitemap.txt'), context=extra_context)
    generate('sitemap_xml.html', join(settings.OUTPUT_FOLDER, 'sitemap.xml'), context=extra_context)

    generate_paginated_home(all_posts, extra_context)
    generate_category_pages(all_posts, extra_context)

    generate_blog_posts(settings, extra_context, generate)


def serve_files(port, watch):
    server = Server()
    for x in watch.split('|'):
        # Static assets live in the output folder; only refresh the browser on change.
        if x.startswith(settings.OUTPUT_FOLDER):
            server.watch(x)
        else:
            server.watch(x, func=generate_site)
    try:
        server.serve(root=settings.OUTPUT_FOLDER, port=port)
    except KeyboardInterrupt:
        print("Shutting down...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Project manager.')
    parser.add_argument('--serve', action='store_true', help='Serve files for livewatch')
    parser.add_argument('--watch', type=str, default='*.py|templates|templates/sections|docs/css|docs/js', help='Files/Folders to watch')
    parser.add_argument('--port', type=int, default=8000, help='Port to serve')
    args = parser.parse_args()

    if args.serve:
        serve_files(args.port, args.watch)
    else:
        generate_site()