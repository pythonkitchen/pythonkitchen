title: Why Choose Flask Over FastAPI
slug: why-choose-flask-over-fastapi
pub: 2021-04-18 21:48:04
authors: arj
tags: 
category: flask

[FastAPI](https://github.com/tiangolo/fastapi) positions itself as one of the best choices for API development in Python. The project is polished for sure, the [docs](https://fastapi.tiangolo.com/) are sleek and the commit messages awesome. It collected some nice parts and pieced them together to produce an artifact infused and driven by pragmatism. But the community is wrong, completely wrong and over hyped in comparing FastAPI with it's father in inspiration: The awesome, one & only, unique Flask

Index
-----


* FastAPI: Standing on the shoulders of giants
* A Culture Of Pushy Marketing: When Python Is Suddenly As Fast As Golang
* The Tiangolo Docs Says You Are Wrong Comparing FastAPI To Flask
* They All Fell Into The Trap: CTO, Respected Authors, StackOverflow's Partner, Big Names and What Not
* What To Compare With What?
* Why Choose Flask Over FastAPI


FastAPI: Standing on the shoulders of giants
--------------------------------------------



If one was to introduce and understand FastAPI, there is no better introduction than in the moustachu wizard's words:

*Here's some extra background that might help understanding where they come from.
The creator of Django-Rest-Framework, Tom Christie, created a new API framework with what he thought would be the best approach for building APIs in modern Python. It was called APIStar.*
*APIStar had to deal with some complexities underneath like supporting WSGI (the same used by Flask and Django) and ASGI, the new standard, etc. So, at some point, Tom decided that a new approach was needed. So, he created a new framework/toolkit form scratch, based on ASGI, called Starlette. The server part of APIStar was deprecated and from then on APIStar was only a set of tools for OpenAPI validation.*

...

*Then, FastAPI was created on top of Starlette, inheriting a lot of the ideas form APIStar (that actually come from even before, with Hug) and updating/improving them, to use standard Python type hints, dependency injection, OpenAPI with docs by default, etc.* [1]

It's also being used by Microsoft, Netflix and Uber [2]. So it's a respected package, being given serious thoughts and considerations in production.

A Culture Of Pushy Marketing: When Python Is Suddenly As Fast As Golang
-----------------------------------------------------------------------



FastAPI states in it's README [3]:


> 
>  The key features are:
>  
>  Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://github.com/tiangolo/fastapi#performance).
> 



Someone raised an issue entitled: Very poor performance does not align with marketing [4]. Some developers tried to assign a meaning to the phrase


> 
>  Very high performance, on par with NodeJS and Go
> 



They hold that it means:


> 
>  If you didn't use FastAPI and used Starlette directly (or another tool, like Sanic, Flask, Responder, etc) you would have to implement all the data validation and serialization yourself. So, your final application would still have the same overhead as if it was built using FastAPI. And in many cases, this data validation and serialization is the biggest amount of code written in applications.
> 



But the author is not going away with on par with.

According to the Cambridge dictionary [5]:


> 
>  on par with: the same as or equal to someone or something
> 



According to Oxford's learner's dictionary it means [6]:


> 
>  on a par/level with somebody/something 
>  - as good, bad, important, etc. as somebody/something else
> 



Tiangolo actually sheds some light on what it actually means:

*Starlette was made to be a minimal micro-framework and toolkit at the same time, so that other tools could be built on top of it, but providing a very solid foundation, and the best performance available in Python, on par with NodeJS and Go.* [1]

So unlike the attempted explanation above or what FastAPI fans would try to produce, the author is clearly saying that a minimal micro-framework in Python (that is Starlette) is as fast as Golang.

Well FastAPI folks, you can't explain it better than the author.

It's no wonder that the fan base attempt some wind in sail comparisons. Tiangolo & Co., you set the trend.

The Tiangolo Docs Says You Are Wrong Comparing FastAPI To Flask
---------------------------------------------------------------



There are an awesome amount of articles stating: Why we moved from Flask to FastAPI, Why I quit Flask, How to move from Flask to FastAPI. This is just crazy. I mean, come on folks, how can you miss the basic facts?

The docs might seems misleading. In discussing alternatives to FastAPI, it lists Flask [7].


> 
>  Flask is a "microframework", it doesn't include database integrations nor many of the things that come by default in Django.
>  
>  This simplicity and flexibility allow doing things like using NoSQL databases as the main data storage system.
>  
>  As it is very simple, it's relatively intuitive to learn, although the documentation gets somewhat technical at some points.
>  
>  It is also commonly used for other applications that don't necessarily need a database, user management, or any of the many features that come pre-built in Django. Although many of these features can be added with plug-ins.
>  
>  This decoupling of parts, and being a "microframework" that could be extended to cover exactly what is needed was a key feature that I wanted to keep.
>  
>  Given the simplicity of Flask, it seemed like a good match for building APIs. The next thing to find was a "Django REST Framework" for Flask.
> 



That's why fans go on to compare with Flask? I don't know. It's misleading for sure as people don't bother to actually read the whole page. The very same page actually lists requests saying:


> 
>  FastAPI is not actually an alternative to Requests. Their scope is very different.
> 



So this is not really a page for comparisons, at least not all. Don't take my words for it. The docs tells you:


> 
>  If you are comparing FastAPI, compare it against a web application framework (or set of tools) that provides data validation, serialization and documentation, like Flask-apispec, NestJS, Molten, etc. Frameworks with integrated automatic data validation, serialization and documentation. [8]
> 



Before you write Flask-bashing articles, at least read the FastAPI docs.

They All Fell Into The Trap: CTO, Respected Authors, StackOverflow's Partner, Big Names and What Not
----------------------------------------------------------------------------------------------------


#### Testdriven.io



One of the Testdriven.io blog authors whom i respect a lot, Amal Shaji wrote an article: Moving from Flask to FastAPI [9]. It's really puzzling to see that such an author, on such a blog has such an understanding. The article goes on detailing how do the installs compare etc. Side by side comparison of views templates etc. The author mentions:


> 
>  You can think of FastAPI as the glue that brings together Starlette, Pydantic, OpenAPI, and JSON Schema.
> 



it should have clicked like: well am i comparing some comparable things or not? Why not compare Flask and Starlette? The author ends with a sweeping statement:


> 
>  Switching to FastAPI is a solid choice.
> 



These types of articles while seemingly genuine just repel people from Flask.

#### Yuan Gao, The CTO



Yuan Gao wrote a somewhat lengthy article entitled: Flask vs FastAPI first impressions [10]. The person compares with visible enthusiasm:


> 
>  I've recently upgraded several of our API endpoints over from Flask to FastAPI, and honestly I haven't felt such a breath of fresh air in development for a long time.
> 



The person was really thinking that jsonify was the tool for apis:


> 
>  Contrast this with Flask, whose errors are HTML pages by default, and return JSON need to be jsonify()'d
> 



The comparison is a devastating head shaking piece, dripping all the way down:


> 
>  In Flask, you access both query and request body via the request singleton, which is a magic instance that when referenced inside and endpoint handler contains stuff relating to the request. ... This is actually highly annoying.
> 



He complains of the lack of validation in Flask:


> 
>  With Flask, there aren't many options for this; you either write a lot of if statements to check every possible part of the data coming in, and then manually make sure to go update your API documentation somewhere, or you use some kind of data validation library.
> 



Even complaining of the lack of web sockets in Flask:


> 
>  Websockets are another feature that Flask does't support,
> 



And concludes with:


> 
>  So while it's clear to me that FastAPI is a much better framework than Flask for APIs, Flask still remains a good choice for many other HTTP tasks.
> 



A miss all over and an overall mess.

#### Pluralsight.com



That one got a 'wow' from me. I mean, pluralsight is busy schooling and rating developers around the world. StackOverflow partnered with them to educate devs. I don't know where to put my head. John Walk writes [14]:


> 
>  This API will work for serving predictions (try it out yourself!)… but it’s entirely likely it will fall over if you try to put it into production. Notably, it lacks any data validation - any missing, misnamed, or mistyped information in the incoming request results in an unhandled exception, returning a 500 error and a singularly unhelpful response from Flask (along with some rather intimidating HTML in debug mode), while potentially firing alerts into your monitoring systems and waking up your DevOps.
>  
>  Frequently, error handling in Flask ends up with a brittle, tangled jumble of try-catches and protected dict access. Better approaches will use a package like pydantic or marshmallow to achieve more programmatic data validation. Fortunately, FastAPI includes pydantic validation out of the box.
> 



I mean how can people not blame Flask when pluralsight tells them to? And Flask is not to be blamed.

#### It's Splashed All Over



AnalyticsVidhya has an article by KAUSTUBH1828 [11] which repeats the arguments mentionned above. Section.io has one [12] by the name of "Choosing between Django, Flask, and FastAPI", Django added for better mismatch. It's published under Engineering Education. Oh my! Same goes for acubits.com [13]. Tivadar Danka from towardsdatascience.com [15] says:


> 
>  For many years, Flask was the number one tool for the job, but in case you haven’t heard, there is a new challenger in town. FastAPI is a relatively new web framework for Python, taking inspiration from its predecessors, perfecting them and fixing many of their flaws.
> 



and the title of the article is: "You Should Start Using FastAPI Now". And the portrayal are indeed in bashing style like Dieter Jordens from betterprogramming.pub [16] entitled "3 Reasons to Switch to FastAPI":


> 
>  FastAPI is based on type hints. Up to this point, Flask has just plain ignored them.
> 



The problem is that people hush Flask down under a False starting point, and some go hard on it. Cover to cover, first letter to last dot, these articles made a faux depart.

#### Re-stating: What these articles did wrong?



They simply compared Flask to FastAPI. They miscompared frameworks.

What To Compare With What?
--------------------------



You can compare Flask with Starlette. You can compare Flask-restx or flask-apispec to FastApi. You can compare Quart to Flask and Starlette. You can compare Quart-schema to FastAPI and Flask-aspispec.

Flask is a micro web framework. Starlette is a "is a lightweight ASGI framework/toolkit". Flask is a WSGI framework and Starlette is an ASGI one. They are barebones, non-purpose specific frameworks. Flask-restx is designed to build APIs, this is closer to FastAPI. It completely misses the point saying Flask misses validation or this and that while FastAPI has this and that. When you compare, compare the frameworks that match in purpose to start with.

Why Choose Flask Over FastAPI
-----------------------------



The title is just a note saying why you should not go about writing articles that way. The article is deliberately mistitled and put en relief the point that you should not compare Flask to FastAPI nor compare FastAPI to Flask. Both serve different purposes.

#### FaQ



Point:


> 
>  "A miss all over and an overall mess."
>  
>  Why does the article just state this opinion and then do little else? Did I miss something? I was expecting some paragraphs afterwards about reasons why, but there are none to be found.
>  
>  This sorta just reeks of bitterness.
> 



A miss all over and an overall mess illustrates the results you get when you compare two things which should not be compared.



---



Point:


> 
>  There are certainly reasons to choose Flask over FastAPI, but this article reads like it was written by an AI.
>  
>  "The problem is that people hush Flask down under a False starting point, and some go hard on it. Cover to cover, first letter to last dot, these articles made a faux depart."
>  
>  If an actual human wrote this: I have no idea what you are trying to say.
> 



People make points but they are False from the start.



---



[1] https://news.ycombinator.com/item?id=22776339
[2] https://fastapi.tiangolo.com/
[3] https://github.com/tiangolo/fastapi
[4] https://github.com/tiangolo/fastapi/issues/1664
[5] https://dictionary.cambridge.org/dictionary/english/par
[6] https://www.oxfordlearnersdictionaries.com/definition/english/level\_1#level\_idmg\_6
[7] https://fastapi.tiangolo.com/alternatives/
[8] https://fastapi.tiangolo.com/benchmarks/
[9] https://testdriven.io/blog/moving-from-flask-to-fastapi/
[10] https://dev.to/meseta/flask-vs-fastapi-first-impressions-1bnm
[11] https://www.analyticsvidhya.com/blog/2020/11/fastapi-the-right-replacement-for-flask/
[12] https://www.section.io/engineering-education/choosing-between-django-flask-and-fastapi/
[13] https://blog.accubits.com/flask-vs-fastapi-which-one-should-you-choose/
[14] https://www.pluralsight.com/tech-blog/porting-flask-to-fastapi-for-ml-model-serving/
[15] https://towardsdatascience.com/you-should-start-using-fastapi-now-7efb280fec02
[16] https://betterprogramming.pub/3-reasons-to-switch-to-fastapi-f9c788d017e5
