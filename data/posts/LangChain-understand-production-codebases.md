title: Understand langChain to Quickly Get Started with Production Codebases
slug: LangChain-understand-production-codebases
pub: 2023-11-13 09:31:20
authors: arj
tags: langchain, software architecture, code analysis
category: artificial intelligence
related_posts: chat-own-data-chatgpt-langchain,json-response-google-genai,how-to-run-tencents-hunyuan-video-model-using-python

LangChain is a superb library to productionize LLMs. It has few concepts which make it great.
If you want to quickly get started with LangChain as maybe like me you have production in front of you, then i hope that this post will help!

First, we know that LangChain has few components.

![](https://github.com/pythonkitchen/pythonkitchen/assets/22630684/82f5cf19-26e5-4623-8895-47560d9509f3)

The components are used to build chains.

![chain3](https://github.com/pythonkitchen/pythonkitchen/assets/22630684/15b957ca-7b55-464d-844c-5d852e25e12a)

Then, we have the concept of agent, which takes a lot of components, including a chain to perform tasks.

![agent](https://github.com/pythonkitchen/pythonkitchen/assets/22630684/ef1b7182-55d4-461d-8121-9f1afc39ed11)

Finally, you can also add your own data store and knowledge base to prevent hallucinations.

![ownstore](https://github.com/pythonkitchen/pythonkitchen/assets/22630684/ca36b750-9b03-4b63-b7f3-85f61abfba79)

