title: How to implement beautiful notifications in Flask
slug: how-implement-beautiful-notifications-flask
pub: Wed, 24 Feb 2021 09:40:49 +0000
authors: Abdur-RahmaanJ

Since you already know [how to implement notifications](https://www.pythonkitchen.com/how-implement-notification-flask/), let's see how to implement beautiful notifications in Flask.

Using boostrap, we can do:


```python
# shopyoapi.html
def notify(message, alert_type="primary"):
    """
    Used with flash
        flash(notify('blabla'))

    Parameters
    ----------
    message: str
        message to be displayed

    alert_type: str
        bootstrap class

    Returns
    -------
    None
    """
    alert = """
    <div class="shopyo-alert alert alert-{alert_type} alert-dismissible fade show" role="alert"
        style="opacity: 0.98;">
      {message}

      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">×</span>
      </button>
    </div>
    """.format(
        message=message, alert_type=alert_type
    )

    scriptFade = """ 
    <script>
          setTimeout(function() {
            $('#flashed-messages').fadeOut('fast');
        }, 5000); // <-- time in milliseconds (5 secs)
    </script>
    """
    return alert + scriptFade


def notify_success(message):
    return notify(message, alert_type="success")


def notify_danger(message):
    return notify(message, alert_type="danger")


def notify_warning(message):
    return notify(message, alert_type="warning")


def notify_info(message):
    return notify(message, alert_type="info")


```


so that 
```flash(notify\_success('Good'))``` will give you a green alert. But, be sure to include the bootstrap links in your page's head. Part of the [Shopyo](https://github.com/Abdur-rahmaanJ/shopyo) internals series.
