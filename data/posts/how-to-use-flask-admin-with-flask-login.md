title: How to use Flask-admin with Flask-login
slug: how-to-use-flask-admin-with-flask-login
pub: 2021-02-24 07:16:19
authors: arj
tags: 
category: flask

Steps:

* 1. Have a login route accept a next parameter
* 2. Define your model view and admin index view
* 3. Register models



In the example below, auth.login is the login route. See [this article](https://www.pythonkitchen.com/how-to-correctly-use-the-next-parameter-in-login-and-logout-in-flask/) for how to set it up. The snippet below is taken from the [Shopyo web framework](https://github.com/Abdur-rahmaanJ/shopyo)

```python
from flask_admin import Admin
from flask_admin.contrib import sqla as flask_admin_sqla
from flask_admin import AdminIndexView
from flask_admin import expose
from flask_admin.menu import MenuLink


class DefaultModelView(flask_admin_sqla.ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))

    @expose('/')
    def index(self):
        if not current_user.is_authenticated and current_user.is_admin:
            return redirect(url_for('auth.login'))
        return super(MyAdminIndexView, self).index()

# further in app.py
admin = Admin(
        app,
        name='My App',
        template_mode='bootstrap4',
        index_view=MyAdminIndexView()
    )
    admin.add_view(DefaultModelView(MyModelHere, db.session))
    admin.add_link(MenuLink(name='Logout', category='', url='/auth/logout?next=/admin'))

```

