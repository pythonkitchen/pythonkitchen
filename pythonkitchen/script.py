import feedparser
import pprint
import markdownify

data = feedparser.parse('/home/appinv/Downloads/pythonkitchen.WordPress.2022-09-19.xml')


pp = pprint.PrettyPrinter(indent=4)
posts = []

for entry in data['entries']:
    # posts.append(entry['content'][0]['value'])
    # pp.pprint(entry)

    content = entry['content'][0]['value']
    slug = entry['link'].split('/')[3]
    print(slug)
    pub = entry['published']
    title = entry['title']

    content = markdownify.markdownify(content, code_language='python')
    with open(f'modules/blogz/data/posts/{slug}.md', 'w+') as f:
    	f.write(f'''title: {title}
slug: {slug}
pub: {pub}

{content}
''')