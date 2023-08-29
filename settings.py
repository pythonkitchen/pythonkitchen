from jamstack.api.template import load_json
import os 

OUTPUT_FOLDER = 'docs/'
DATA_PATH = 'data/'
POSTS_PATH = os.path.join(DATA_PATH, "posts")
AUTHORS_PATH = os.path.join(DATA_PATH, "authors")

info = load_json('info.json')
