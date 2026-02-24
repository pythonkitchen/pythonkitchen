import logging
import os
from os.path import join
import markdown
from datetime import datetime
from bs4 import BeautifulSoup
import re

def add_internal_links(html_content, posts_metadata, current_slug):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Sort titles by length (longest first) to avoid partial matches
    sorted_posts = sorted(posts_metadata, key=lambda x: len(x['title']), reverse=True)
    
    # Track which titles we've already linked in this post to avoid multiple links to same post
    linked_slugs = set()
    linked_slugs.add(current_slug)

    for post in sorted_posts:
        if post['slug'] in linked_slugs:
            continue
            
        title = post['title']
        slug = post['slug']
        
        # Use word boundaries to avoid matching parts of words
        pattern = re.compile(r'\b' + re.escape(title) + r'\b', re.IGNORECASE)
        
        # Find text nodes
        text_nodes = soup.find_all(string=True)
        
        for node in text_nodes:
            # Skip nodes that are already links or inside elements where we shouldn't add links
            if node.parent.name in ['a', 'script', 'style', 'pre', 'code', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                continue
                
            if pattern.search(node):
                # Replace logic: replace only the first occurrence in the entire document
                # This is a bit simplified; for better SEO we might want to be more specific
                new_html = pattern.sub(f'<a href="/{slug}">{title}</a>', node, count=1)
                
                if new_html != node:
                    new_soup = BeautifulSoup(new_html, 'html.parser')
                    node.replace_with(new_soup)
                    linked_slugs.add(slug)
                    break # Move to next post title
                    
    return str(soup)

def get_posts(settings):
    posts = []
    logging.info("Start Generating blog posts ...")

    # First pass: Gather metadata
    posts_metadata = []
    for mdfile in os.listdir(settings.POSTS_PATH):
        if not mdfile.endswith('.md'):
            continue
        blog_post_path = join(settings.POSTS_PATH, mdfile)
        with open(blog_post_path, encoding="utf-8") as f:
            text = f.read()
        md = markdown.Markdown(extensions=["extra", "smarty", "meta"])
        md.convert(text)
        metadata = md.Meta
        
        if 'title' in metadata and 'slug' in metadata:
            posts_metadata.append({
                'title': metadata['title'][0],
                'slug': metadata['slug'][0]
            })

    # Second pass: Process content
    for mdfile in os.listdir(settings.POSTS_PATH):
        if not mdfile.endswith('.md'):
            continue
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
                
        # Add internal links
        html = add_internal_links(html, posts_metadata, slug)

        try:
            related_posts = metadata["related_posts"][0].split(',')
            related_posts = [r.strip() for r in related_posts if r.strip()]
        except:
            related_posts = []
                
        post = {
            "slug": slug,
            "content": html,
            "authors": authors,
            "pub": date,
            "title": title,
            "categories": categories,
            "tags": tags,
            "related_posts": related_posts
        }
        posts.append(post)

    posts.sort(key=lambda date: datetime.strptime(date['pub'], "%Y-%m-%d %H:%M:%S"), reverse=True)
    return posts



def get_suggested_posts(current_post, all_posts, limit=3):



    suggested = []



    for post in all_posts:



        if post['slug'] == current_post['slug']:



            continue



        



        # Calculate score based on categories and tags



        score = 0



        common_categories = set(current_post['categories']) & set(post['categories'])



        score += len(common_categories) * 2



        



        common_tags = set(current_post['tags']) & set(post['tags'])



        score += len(common_tags)



        



        if score > 0:



            suggested.append((post, score))



    



    # Sort by score and then by date



    suggested.sort(key=lambda x: (x[1], x[0]['pub']), reverse=True)



    



    return [p[0] for p in suggested[:limit]]







def generate_blog_posts(settings, context, generate):



    posts = get_posts(settings)



    logging.info("Start Generating blog posts ...")







    for post in posts:
        slug = post["slug"]
        suggested = get_suggested_posts(post, posts)
        
        # If not enough suggested, fill with latest posts
        if len(suggested) < 3:
            for p in posts:
                if p['slug'] != slug and p not in suggested:
                    suggested.append(p)
                if len(suggested) >= 3:
                    break

        context.update({
            "post": post, 
            "suggested_posts": suggested,
            "path": "../" * 1
        })
        






        try:



            os.makedirs(join(settings.OUTPUT_FOLDER, slug), exist_ok=True)



        except: 



            pass



        generate(



            "post.html",



            join(settings.OUTPUT_FOLDER, slug, "index.html"),



            context=context,



        )



        logging.info(f"Generating blog post {slug}...")


