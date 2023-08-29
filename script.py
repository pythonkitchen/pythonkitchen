import feedparser
import pprint
import markdownify

data = feedparser.parse('/home/appinv/Downloads/pythonkitchen.WordPress.2023-08-29.xml')


pp = pprint.PrettyPrinter(indent=4)
posts = []

for entry in data['entries']:
    # posts.append(entry['content'][0]['value'])
    pp.pprint(entry)
    
    content = entry['content'][0]['value']
    slug = entry['link'].split('/')[3]
    print(slug)
    pub = entry['wp_post_date']
    title = entry['title']

    authors = entry['authors']
    authors = [a['name'] for a in authors]
    authors = ','.join(authors)

    tags = entry['tags']
    tags = [t["term"] for t in tags if t["scheme"] == "post_tag"]
    tags = ','.join(tags)

    category = entry['tags']
    category = [t["term"] for t in category if t["scheme"] == "category"]
    category = ','.join(category)

    content = markdownify.markdownify(content, code_language='python')
    with open(f'data/posts/{slug}.md', 'w+') as f:
    	f.write(f'''title: {title}
slug: {slug}
pub: {pub}
authors: {authors}
tags: {tags}
category: {category}

{content}
''')