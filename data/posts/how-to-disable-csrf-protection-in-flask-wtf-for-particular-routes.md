title: How to disable csrf protection for particular routes in Flask-wtf
slug: how-to-disable-csrf-protection-in-flask-wtf-for-particular-routes
pub: 2021-02-24 07:52:33
authors: arj
tags: flask, wtforms, csrf
category: security
related_posts: how-prevent-open-redirect-vulnerab-flask,how-to-correctly-use-the-next-parameter-in-login-and-logout-in-flask,run-flask-linux-only-windows-afpy

Flask-wtf recommends using `@csrf.exempt` to disable csrf protection for particular routes as in the case of APIs.

Now this is pretty confusing. What does csrf refers to?

If you inspect Flask-wtf you do see a csrf attribute


```python
>>> import flask_wtf
>>> dir(flask_wtf)
['CSRFProtect', 'CsrfProtect', 'FlaskForm',
'Form', 'Recaptcha', 'RecaptchaField', 
'RecaptchaWidget', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__p
ath__', 
'__spec__', '__version__', '_compat', 
'absolute_import', 'csrf', 'fields', 
'form', 'recaptcha', 'validators', 
'widgets']
>>>

```


But it does not mean the above. It means what you defined as csrf.


```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

@some_blueprint.route("/myendpoint", methods=['POST'])
@csrf.exempt
def myfunc():
    pass

```

