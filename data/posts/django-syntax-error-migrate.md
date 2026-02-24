title: How To Solve Django Syntax Error On Migrating
slug: how-solve-django-syntax-error-migrate
pub: 2024-03-14 16:50:00
authors: arj
tags: django, migrations, debugging
category: web development
related_posts: how-to-have-django-packages-in-flask,why-choose-flask-over-fastapi,run-flask-linux-only-windows-afpy

The Django syntax error on migrating is very annoying, specially when you don't find any error when looking for one. This post contains a working solution.

Table of contents
=================

* I get a syntax error when trying to migrate in Django
* The solution

I get a syntax error when trying to migrate in Django
====

When using the migrate commands in Django

```
$ python manage.py makemigrations
$ python manage.py migrate
```

You might get this ugly error:

```
File "/my/path/lib/python3.11/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers return executor(sql, params, many, context) 
File "/my/path/lib/python3.11/site-packages/django/db/backends/utils.py", line 100, in _execute with self.db.wrap_database_errors: 
File "/my/path/lib/python3.11/site-packages/django/db/utils.py", line 91, in exit_ raise dj_exc_value.with_traceback(traceback) from exc_value 
File "/my/path/lib/python3.11/site-packages/django/db/backends/utils.py", line 105, in _execute return self,cursor.execute(sq1,2arams) 
File "/my/path/lib/python3.11/site-packages/django/db/backends/sqlite3/base.py" , line 329, in execute return super().execute(queryparams) 
django.db.utils.OperationalError: near ")": syntax error 
```

You can confirm using a tool like ruff or copy pasting online in a syntax checker to ensure that there are actually no syntax error. This is troubling.

Apparently, the error is caused by a bad model which got integrated in one of the migrations.

The solution
===

To solve a syntax error on using the migrate comamnds,

1. delete all files in all migrations folder except `__init__.py`
2. delete the sqlite database if need be

Bit hard, but it solves the issue.