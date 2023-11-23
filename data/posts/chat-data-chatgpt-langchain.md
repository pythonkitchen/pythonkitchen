title: Chat with your own data/text files using chatGPT and LangChain
slug: chat-own-data-chatgpt-langchain
pub: 2023-11-23 10:35:00
authors: arj
tags: langchain
category: data science,machine learning

There are many different approaches to chatting with your own data.
One way is to upload your PDF to the OpenAi chatGPT cloud.
This comes with several limitations such as data being deleted or umm the risk of a not smart chatGPT leaking it.

Now, you can also download a model from somewhere. 
And you need to find a good one.
And it will probably not be as good as chatGPT.
So, to benefit from the advantage of chatGPT with local data, [LangChain]() presents an interesting option. 
We, however, need a vector store.

## What is a vector store?

A vector store stores data as data encodings.
This allows us to plug our own data in chatGPT.
It augments the contextual awareness of chatGPT.
If you asks about "Mauritius tourist activities", it might give some response.
If you give it more information, the response will be more detailed.
You need to convert your data into vector embeddings and store it in a vector database.
You can use Redis, PineCone (A SaaS offering) or [ChromaDB](https://python.langchain.com/docs/integrations/vectorstores/chroma) as vector databases among others.
Fortunately, [LangChain](https://python.langchain.com/) helps us a lot in connecting a vector store for use in chatGPT.

Please read this before to understand more about vector databases: [Understand langChain to Quickly Get Started with Production Codebases](/LangChain-understand-production-codebases/)

## The code

You need to install those:

```
pip install langchain openai chromadb==0.4.15 tiktoken unstructured
```
Then create a directory called `data/`.

Then add your files in the data folder.

Then create a file called chat.py.

Your directory looks like this

```
./
data/
    friends.txt
    bugs.txt
chat.py
```

You can add whatever info you want in the data folder.

You can add pdfs also.

Then paste:

```python
import os
import sys

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

os.environ["OPENAI_API_KEY"] = "sk-myopenaikey"

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False
query = None

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=embedding_function)
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  # loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
  loader = DirectoryLoader("exp-data/") # Also supports glob="<pattern>"
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = [] # preserve context
while True:
  if not query:
    query = input("Prompt > ")
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  result = chain({"question": query, "chat_history": chat_history})
  print(result['answer'],end="\n\n")

  chat_history.append((query, result['answer']))
  query = None
```

The persist part is if you don't want to load it in the db each time.

## Notes

If you have errors like:

```
Traceback (most recent call last):
  File "", line 34, in <module>
    index = VectorstoreIndexCreator().from_loaders([loader])
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "", line 82, in from_loaders
    return self.from_documents(docs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "", line 87, in from_documents
    vectorstore = self.vectorstore_cls.from_documents(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "site-packages/langchain/vectorstores/chroma.py", line 684, in from_documents
    return cls.from_texts(
           ^^^^^^^^^^^^^^^
  File "site-packages/langchain/vectorstores/chroma.py", line 620, in from_texts
    chroma_collection = cls(
                        ^^^^
  File "site-packages/langchain/vectorstores/chroma.py", line 125, in __init__
    self._collection = self._client.get_or_create_collection(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "site-packages/chromadb/api/client.py", line 226, in get_or_create_collection
    return self._server.get_or_create_collection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 127, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "site-packages/chromadb/api/segment.py", line 216, in get_or_create_collection
    return self.create_collection(  # type: ignore
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 127, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "site-packages/chromadb/api/segment.py", line 190, in create_collection
    return Collection(
           ^^^^^^^^^^^
  File "site-packages/chromadb/api/models/Collection.py", line 85, in __init__
    validate_embedding_function(embedding_function)
  File "site-packages/chromadb/api/types.py", line 210, in validate_embedding_function
    raise ValueError(
ValueError: Expected EmbeddingFunction.__call__ to have the following signature: odict_keys(['self', 'input']), got odict_keys(['self', 'args', 'kwargs'])
Please see https://docs.trychroma.com/embeddings for details of the EmbeddingFunction interface.
Please note the recent change to the EmbeddingFunction interface: https://docs.trychroma.com/migration#migration-to-0416---november-7-2023 
```
The solution is probably to pin an older version of chromadb as we did above.

## Nice resources

- [Techlead video explanation](https://www.youtube.com/watch?v=9AXP7tCI9PI)
- [Techlead faulty code (Which I fixed in this post)](https://github.com/techleadhd/chatgpt-retrieval)
- [LangChain chroma notebook](https://github.com/rubentak/Langchain/blob/main/notebooks/Langchain_doc_chroma.ipynb)
