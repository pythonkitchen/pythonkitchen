title: How To Have Django Packages in Flask
slug: how-to-have-django-packages-in-flask
pub: 2022-08-30 03:43:51
authors: arj
tags: flask, django, ecosystem
category: web development
related_posts: why-choose-flask-over-fastapi,shopyo-understand-advanced-flask-app,build-a-note-app-in-flask-as-fast-as-it-can-get-using-shopyo

Django packages in Flask seems like a far-away dream, but [shopyo](https://pypi.org/project/shopyo/) 4.6.0 allows you to install Shopyo apps from pypi.

What is Shopyo?
---------------



Shopyo implements Django functionalities such as the admin panel etc by using existing Flask packages. But, it also implements Django-specifics like the `collectstatic` command, migrations, apps, even new concepts like boxes etc.

What the fuss about django packages?
------------------------------------



Shopyo allows you to use apps in your project. Shopyo apps are in the format


```python
demo/
├── forms.py
├── global.py
├── info.json
├── models.py
├── static
├── templates
│   └── demo
│       ├── blocks
│       │   └── sidebar.html
│       └── dashboard.html
├── tests
│   ├── test_demo_functional.py
│   └── test_demo_models.py
└── view.py

```


Until now, shopyo apps could not be installed but used locally. Now, the project has been updated to allow it! You can examine [shopyo-demo](https://github.com/shopyo/shopyo-demo) the first shopyo app to get a feel of what it's like. Yes, you even have a sandbox to test the app, just like Django apps.

What to change from older projects?
-----------------------------------


`init.py` has a new variable called `installed_packages` which should contain the installed app you want to add.

Then, nothing to change really, just imports and in `info.json` make sure to set module name as `shopyo_<your module name>`
Conclusion
----------



Having such a system for Flask is very convenient instead of having to build components from scratch time and again. Sites like [djangopackages.com](https://djangopackages.org/) are very useful to find what we need real quick.
