title: How to implement notification in Flask
slug: how-implement-notification-flask
pub: Wed, 24 Feb 2021 09:29:14 +0000
authors: Abdur-RahmaanJ

Implementing notifications in Flask goes way beyond using flash. You have to add this snippet in your templates:


```html
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
