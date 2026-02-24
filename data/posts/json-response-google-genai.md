title: How to get gemini response as json using python and google genai
slug: json-response-gemini-google-genai
pub: 2025-01-16 15:42:02
authors: arj
tags: gemini, generative ai, apis
related_posts: chat-own-data-chatgpt-langchain,LangChain-understand-production-codebases,simple-json-parser
category: artificial intelligence


Normally you can tune models to return json. But, fortunately, Gemini


First install the lib

```
pip install google-genai
```

Here is a snippet i used to receive JSON response from Google GenAi.

```
from google import genai

prompt = '<prompt here>'
client = genai.Client(api_key='YOURKEYHERE')

chat = client.chats.create(model='gemini-2.0-flash-exp', 
    config={
        'response_mime_type': 'application/json',
        
    }
)
for chunk in chat.send_message_stream(prompt):
    print(chunk.text)
```

You can also use PyDantic to customise the schema


```
from google.genai import types



from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    email: str


response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents="Give me info about 2 random persons",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Profile,
    ),
)
print(response.text)
```


You can customise the schema as in the examples.

```
response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents="Give me information for the United States.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "required": [
                "name",
                "population",
                "capital",
                "continent",
                "gdp",
                "official_language",
                "total_area_sq_mi",
            ],
            "properties": {
                "name": {"type": "STRING"},
                "population": {"type": "INTEGER"},
                "capital": {"type": "STRING"},
                "continent": {"type": "STRING"},
                "gdp": {"type": "INTEGER"},
                "official_language": {"type": "STRING"},
                "total_area_sq_mi": {"type": "INTEGER"},
            },
            "type": "OBJECT",
        },
    ),
)
print(response.text)
```

Json types can be one of those:

- "TYPE_UNSPECIFIED"
- "STRING"
- "NUMBER"
- "INTEGER"
- "BOOLEAN"
- "ARRAY"
- "OBJECT"

