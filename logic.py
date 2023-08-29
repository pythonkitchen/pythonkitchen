import logging
import os
from os.path import join
import markdown
from datetime import datetime

def get_posts(settings):
    posts = []
    logging.info("Start Generating blog posts ...")

        # html = markdown.markdown(md, extensions=extensions, output_format='html5')
    for mdfile in os.listdir(settings.POSTS_PATH):
        blog_post_path = join(settings.POSTS_PATH, mdfile)
        with open(blog_post_path, encoding="utf-8") as f:
            text = f.read()
        md = markdown.Markdown(extensions=["extra", "smarty", "meta"])
        html = md.convert(text)
        metadata = md.Meta

        slug = metadata["slug"][0]
        try:
            authors = metadata["authors"]
        except:
            authors = ["arj"]
        title = metadata["title"][0]

        try:
            tags = metadata["tags"]
        except:
            tags = []
        date = metadata["pub"][0]
        
        if 'category' not in metadata:
            categories = ["Uncategorized"]
        else:
            categories = metadata['category'][0]
            categories = [c for c in categories.split(',') if c.strip()]
                
            
        
                
        post = {
            "slug": slug,
            "content": html,
            "authors": authors,
            "pub": date,
            "title": title,
            "categories": categories,
            "tags": tags,
        }
        posts.append(post)

    posts.sort(key=lambda date: datetime.strptime(date['pub'], "%Y-%m-%d %H:%M:%S"), reverse=True)
    return posts



def generate_blog_posts(settings, context, generate):
    posts = []
    logging.info("Start Generating blog posts ...")

        # html = markdown.markdown(md, extensions=extensions, output_format='html5')
    for post in get_posts(settings):
        slug = post["slug"]
        context.update({"post": post, "path": "../" * 1})

        try:
            os.mkdir(join(settings.OUTPUT_FOLDER, slug))
        except: 
            pass
        generate(
            "post.html",
            join(settings.OUTPUT_FOLDER, slug, "index.html"),
            context=context,
        )
        logging.info(f"Generating blog post {slug}...")