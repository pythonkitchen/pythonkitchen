title: Chatterbot Google Colab Train English Corpus
slug: chatterbot-google-colab-train-english-corpus
pub: 2021-03-22 17:39:43
authors: arj
tags: 
category: chatbot

Here's how to solve the file not found for training chatterbot on Google collab:


```python
# Install
!pip install chatterbot
!pip install chatterbot-corpus

# move english to content viz our workign directory
import os
os.system('mv /usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data/english /content/english')

import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


import os
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(bot)
path = '/content/english'
for file in os.listdir(path):
    file_path = '/content/english/'+ file
    trainer.train(file_path)

    print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

```

