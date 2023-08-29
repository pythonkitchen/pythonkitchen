title: How to correctly use the next parameter in login and logout in Flask
slug: how-to-correctly-use-the-next-parameter-in-login-and-logout-in-flask
pub: 2021-02-24 07:05:45
authors: arj
tags: 
category: flask,shopyo

Here is a sample login and logout route taken from [the shopyo web framework](https://github.com/Abdur-rahmaanJ/shopyo). You can learn [here](https://www.pythonkitchen.com/how-prevent-open-redirect-vulnerab-flask/) how is get\_safe\_redirect defined and why it is important


```python
@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    context = {}
    login_form = LoginForm()
    context["form"] = login_form
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter(
            func.lower(User.email) == func.lower(email)
        ).first()
        if user is None or not user.check_password(password):
            flash(notify_danger("please check your user id and password"))
            return redirect(url_for("auth.login"))
        login_user(user)
        if 'next' not in request.form:
            next_url = url_for('dashboard.index')

        else:
            if request.form['next'] == '':
                next_url = url_for('dashboard.index')
            else:
                next_url = get_safe_redirect(request.form['next'])
        return redirect(next_url)
    return render_template("auth/login.html", **context)


@auth_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash(notify_success("Successfully logged out"))

    if 'next' not in request.args:
        next_url = url_for('dashboard.index')
    else:
        if request.args.get('next') == '':
            next_url = url_for('dashboard.index')
        else:
            next_url = get_safe_redirect(request.args.get('next'))
    return redirect(next_url)

```


The trick is adding this html snippet in your login form


```python
<input
    type="hidden"
    name="next"
    value="{{ request.args.get('next', '') }}"
/>

```

