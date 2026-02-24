title: How to implement notification in Flask
slug: how-implement-notification-flask
pub: 2021-02-24 09:29:14
authors: arj
tags: flask, backend, messaging
category: web development
related_posts: how-implement-beautiful-notifications-flask,integrate-tinymce-5-with-flask,p5js-with-flask-socket-io

Implementing notifications in Flask goes way beyond using flash. You have to add this snippet in your templates:


```python
<div id="flashed-messages">
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      {% for message in messages %}
        {{ message | safe}}
      {% endfor %}
    {% endif %}
  {% endwith %}
</div>

```


then


```python
from flask import flash

@app.route('/')
    flash('Oho')
    return render_template('mytemplate.html')

```


In [shopyo](https://github.com/Abdur-rahmaanJ/shopyo) this is situated at box\_\_default/base/templates/base/blocks/flashed\_messages.html. Used with `{% include 'base/blocks/flashed_messages.html'%}`
