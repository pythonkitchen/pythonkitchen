title: How to run a Flask Linux-only  App on Windows - The AFPy Site
slug: run-flask-linux-only-windows-afpy
pub: 2020-11-09 09:41:13
authors: arj
tags: flask, linux, portability
category: web development
related_posts: how-to-disable-csrf-protection-in-flask-wtf-for-particular-routes,why-choose-flask-over-fastapi,how-to-have-django-packages-in-flask

There are in the Python world many Flask Linux-only apps. However in many case, with some twerking we can make them work on Windows. We'll take the case of the AFPy site.

First fork the [AFPy site](https://github.com/AFPy/site)

Then clone it


```python
git clone https://github.com/<your-username>/site.git

```


The makefile looks like this


```python
VENV = $(PWD)/.env
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python
FLASK = $(VENV)/bin/flask
ISORT = $(VENV)/bin/isort
BLACK = $(VENV)/bin/black

all: install serve

install:
    test -d $(VENV) || python3 -m venv $(VENV)
    $(PIP) install --upgrade --no-cache pip setuptools -e .[test]

clean:
    rm -fr dist
    rm -fr $(VENV)
    rm -fr *.egg-info

check-outdated:
    $(PIP) list --outdated --format=columns

test:
    $(PYTHON) -m pytest tests.py afpy.py --flake8 --isort --cov=afpy --cov=tests --cov-report=term-missing

serve:
    env FLASK_APP=afpy.py FLASK_ENV=development $(FLASK) run

isort:
    $(ISORT) -rc .isort.cfg afpy.py tests.py

black:
    $(VENV)/bin/black afpy.py tests.py

.PHONY: all install clean check-outdated test serve isort black


```


We also do not see any requirements.txt but see them listed in setup.py


```python
    install_requires=[
        'Flask',
        'Flask-Caching',
        'libsass',
        'docutils',
        'feedparser',
        'python-dateutil',
        'itsdangerous',
    ],

```


We need to install the package to get the setup working

First setup a virtual environment. If you checked the .gitignore you will see that it is not the usual github one. You will need to add `venv/` to it. See [reapplying gitignore](https://stackoverflow.com/questions/19663093/apply-gitignore-on-an-existing-repository-already-tracking-large-number-of-file). Let's name our virtual environment venv


```python
python -m venv venv

```


Then we install the package


```python
pip install -e .

```


Flask apps use `flask run` to run. But first some variables must be set. From the makefile:


```python
serve:
    env FLASK_APP=afpy.py FLASK_ENV=development $(FLASK) run

```


Translated to batch


```python
set FLASK_APP=afpy.py
set FLASK_ENV=development

```


On running you can see a locale error. You can comment it out and rerun.

![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/afpy_local.png)
*The AFPy promotes Python in the French world and is a combination of many organising bodies*

Note of caution: recomment our the locale line before comitting!

### Testing



For testing you will need to run black, flake8, tests.py
