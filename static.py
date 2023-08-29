import argparse
from os.path import join

from livereload import Server

import settings
from jamstack.api.template import generate
from datetime import datetime
from logic import generate_blog_posts
from logic import get_posts
import calendar 
import toml
import os

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

def get_author_info(key):
    infos = {}
    for author_file in os.listdir(settings.AUTHORS_PATH):
        author = author_file.split(".")[0]
        with open(os.path.join(settings.AUTHORS_PATH, f'{author_file}')) as f:
            info = toml.load(f)
            infos[author] = info
    
    return infos[key]

def generate_site():
    extra_context = {"info": settings.info, "posts": get_posts(settings), 
                     "clean_text": clean_text, "format_post_date": format_post_date,
                     "get_author_info": get_author_info}
    generate('index.html', join(settings.OUTPUT_FOLDER, 'index.html'), context=extra_context)

    generate_blog_posts(settings, extra_context, generate)


def serve_files(port, watch):
    server = Server()
    for x in watch.split('|'):
        server.watch(x, func=generate_site)
    try:
        server.serve(root=settings.OUTPUT_FOLDER, port=port)
    except KeyboardInterrupt:
        print("Shutting down...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Project manager.')
    parser.add_argument('--serve', action='store_true', help='Serve files for livewatch')
    parser.add_argument('--watch', type=str, default='*.py|templates|templates/sections', help='Files/Folders to watch')
    parser.add_argument('--port', type=int, default=8000, help='Port to serve')
    args = parser.parse_args()

    if args.serve:
        serve_files(args.port, args.watch)
    else:
        generate_site()
