title: An Advanced Flask App: Shopyo
slug: shopyo-understand-advanced-flask-app
pub: 2020-02-25 03:43:14
authors: arj
tags: flask, shopyo, modular architecture
category: web development
related_posts: build-a-note-app-in-flask-as-fast-as-it-can-get-using-shopyo,how-to-have-django-packages-in-flask,how-to-use-flask-admin-with-flask-login

![](https://raw.githubusercontent.com/Abdur-rahmaanJ/shopyo/master/shopyo.png)
[Shopyo](https://github.com/Abdur-rahmaanJ/shopyo) is an Open Source Flask-based, Python-powered inventory solution and upcoming point of sales. It's aim is to help small business owners get a nice Python-based product with essential amenities for their businesses. An empty Shopyo project at the very least makes a great Flask base. Shopyo also makes use of advanced flask concepts.

The Tech Stack
==============


![](https://images.unsplash.com/photo-1533630160910-65f5a1718c65?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60)

A peek at Shopyo's requirements.txt gives


```python
flask
flask_sqlalchemy
marshmallow_sqlalchemy
flask_marshmallow
flask_migrate
flask_script
flask_login
Flask-WTF
requests

```

* flask\_sqlalchemy



flask\_sqlalchemy is a wrapper around SQLAlchemy, a popular Python ORM. An ORM allows you to define your SQL tables without the need to write SQL codes. You just define models and the table is created for you. A typical model looks like this:


```python
class Settings(db.Model):
    __tablename__ = 'settings'
    setting = db.Column(db.String(100), primary_key=True)
    value = db.Column(db.String(100))

```

* flask\_migrate



flask\_migrate is used to migrate your models. If you change your models by adding a new field, the change is not reflected in your database. That's why you need to apply migrations. It is a wrapper around Alembic, a popular migration package.

* flask\_marshmallow
* marshmallow\_sqlalchemy



Marshmallow is a project that allows you to create REST Apis. flask\_marshmallow allows the easy integration of marshmallow with Flask and marshmallow\_sqlalchemy is a required package that goes along.

* flask\_script



Though deprecated by Flask's official command line utitlity, flask\_script allows you to create scripts to manage your Flask app easily.

* flask\_login



Flask login allows you to add authentication to your app.

* Flask-WTF



A package that allows you to create forms. We use it to prevent CSRF (pronounced sea surf) attacks. It basically ensures that you don't tamper with a webpage then try to send it to someone else expecting it to work

* requests



A package to make web requests and pull in urls easily. You can view a tutorial about it [here](https://dmerej.info/blog/post/requests-what-you-need-to-build-useful-apps/)
Terms Explained
===============


![](https://images.unsplash.com/photo-1507668077129-56e32842fceb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80)
model
-----



A model defines your table


```python
class Settings(db.Model):
    __tablename__ = 'settings'
    setting = db.Column(db.String(100), primary_key=True)
    value = db.Column(db.String(100))

```


creates a table named settings with fields named setting and value

template
--------



A template is an html file with spaces left for values. `{%` and `{{` have special meaning. `{{1 + 1}}` will display 2 when rendered. Similarly `{{x + 1}}` will evaluate the expression before rendering.


```python
{% extends "base/main_base.html" %}

{% set active_page ='settings' %}

{% block pagehead %}
<title>Settings</title>
<style>
  .hidden{
    display: none;
  }
  .show{
    display: inline-block;
  }
</style>
{% endblock %}

{% block content %}
<script type="text/javascript">
$(function() {

  });
</script>

<table class="table">
  <thead>
    <tr>
      <th scope="col">Settings</th>
      <th scope="col">Value </th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody>
{% for setting in settings %}
    <tr>
      <td>{{setting.setting}}</td>
      <td>{{setting.value}} </td>
      <td><a href="/settings/edit/{{setting.setting}}" class="btn btn-info" role="button"><i class="fas fa-pencil-alt"></i></a></td>
    </tr>
{%endfor%}
  </tbody>
</table>

{% endblock %}


```


let's take this snippet


```python
{% extends "base/main_base.html" %}

```


Tells that we are inheriting from [base.html](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/templates/base/main_base.html)

This eases our life by not copying whole `<link>` or `<script>` codes for example or not recopying the header/footer


```python
{% block pagehead %}
...
{% endblock %}


{% block content %}
...
{% endblock %}

```


allows us to define our head and body respectively.

Views and blueprint
===================


![](https://images.unsplash.com/photo-1565886593760-8e80f074d1f7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=739&q=80)

A view file has lots of routes and what happens when such a route is found. This is the settings view file for example


```python
from flask import (
    Blueprint, render_template, request, redirect, url_for, jsonify
    )

from addon import db
from views.settings.models import Settings
from flask_marshmallow import Marshmallow
from flask_login import login_required, current_user

from project_api import base_context


settings_blueprint = Blueprint('settings', __name__, url_prefix='/settings')

@settings_blueprint.route("/")
@login_required
def settings_main():
    context = base_context()

    settings =  Settings.query.all()

    context['settings'] = settings
    return render_template('settings/index.html', **context)

...

```


Here is a breaking down:


```python
from flask import (
    Blueprint, render_template, request, redirect, jsonify
    )

```

* Blueprint



Allows us to create blueprints. More on that further on

* render\_template



return render\_template(filename) returns the rendered html

* request



refers to the incoming web request by which we can check for GET or POST methods

* redirect



redirects to another url

* jsonify



returns a string or dictionary as JSON response


```python
from addon import db

```

[addon](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/addon.py) contains the following:


```python
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()

```


```python
from views.settings.models import Settings

```


Tells us to go to views folder -> settings folder -> models file


```python
...
from project_api import base_context

```

[project\_api.py](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/project_api.py) contains base\_context which returns just a dictionary


```python
def base_context():
    base_context = {
        'APP_NAME': get_setting('APP_NAME'),
        'SECTION_NAME': get_setting('SECTION_NAME'),
        'SECTION_ITEMS': get_setting('SECTION_ITEMS')
    }
    return base_context.copy()

```


We copy so as not to let additions be global. Render templates accepts the variables to be rendered as keywords. But those 3 variables are rendered everywhere so, instead of copy paste each time, we just added them beforehand to the dictionary.


```python
settings_blueprint = Blueprint('settings', __name__, url_prefix='/settings')

```


This tells that whatever urls starts with /settings will be dealt with in this file


```python
@settings_blueprint.route("/abc")

```


is actually for the url `/settings/abc`

```python
@settings_blueprint.route("/")
@login_required
def settings_main():
    context = base_context()

    settings =  Settings.query.all()

    context['settings'] = settings
    return render_template('settings/index.html', **context)

```


Context is just a dictionary


```python
context['settings'] = settings

```


passes the settings variable which the for loop in the template makes use of


```python
{% for setting in settings %}
    <tr>
      <td>{{setting.setting}}</td>
      <td>{{setting.value}} </td>
      <td><a href="/settings/edit/{{setting.setting}}" class="btn btn-info" role="button"><i class="fas fa-pencil-alt"></i></a></td>
    </tr>
{%endfor%}

```


By the way,


```python
context['settings'] = settings
return render_template('settings/index.html', **context)

```


is the same as


```python
return render_template('settings/index.html', 
    settings=settings,
    APP_NAME=get_setting('APP_NAME'),
    SECTION_NAME=get_setting('SECTION_NAME'),
    SECTION_ITEMS=get_setting('SECTION_ITEMS'))

```

Register blueprints
===================


![](https://images.unsplash.com/photo-1542621334-a254cf47733d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80)

in [app.py](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/app.py) you will see


```python
    from views.settings.settings_modif import settings_blueprint

    app.register_blueprint(settings_blueprint)

```


which adds the views of the settings folder to the app.

Configuration management
========================


![](https://images.unsplash.com/photo-1484191914255-a429e6f819b4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80)

in [config.py](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/config.py) we see


```python
class Config:
    """Parent configuration class."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'qow32ijjdkc756osk5dmck'  # Need a generator
    APP_NAME = 'Demo'
    SECTION_NAME = 'Manufacturer'
    SECTION_ITEMS = 'Products'
    HOMEPAGE_URL = '/manufac/'


class DevelopmentConfig(Config):
    """Configurations for development"""
    ENV = 'development'
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': Config,
}

```


then in [app.py](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/app.py)

```python
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    ...


```


then further down


```python
app = create_app('development')

```


so, if we put in 'production' it will load the production configs.

As info, creating apps this way (app = ...) is called the App Factory pattern

manage.py
=========


![](https://images.unsplash.com/photo-1509541206217-cde45c41aa6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=751&q=80)
[manage.py](https://github.com/Abdur-rahmaanJ/shopyo/blob/master/shopyo/manage.py)

```python
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

```


allows us to pass in normal Alembic migration commands

normal alembic commands run like:


```python
alembic db init
alembic db migrate
alembic db upgrade

```


but using the above code, we automatically get


```python
python manage.py db init
python manage.py db migrate
python manage.py db upgrate


```


similarly this:


```python
@manager.command
def runserver():
    app.run()


```


allows us to have


```python
python manage.py runserver

```

Conclusion
==========



This was written as part of the Shopyo docs but makes a nice Flask post by the way!

If you did not understand something, please ping me at


```python
arj.python at gmail dot com


```

