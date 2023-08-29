title: How to prevent the Open Redirect vulnerability with the next parameter in Flask
slug: how-prevent-open-redirect-vulnerab-flask
pub: 2021-02-24 08:24:00
authors: arj
tags: 
category: flask,security

Let's say someone codes a url like this:


```python
http://domain.com/do/something?next=http://domain.com/homepage

```


Now an attacker can craft the url like that:


```python
http://domain.com/do/something?next=http://evildomain.com/homepage

```


If you don't sanitise the next, your user will be taken to the evil site. This is the Open Redirect vulnerability.

That's why you must make sure urls are safe. You do it like that:


```python
from flask import request, g, redirect
from urllib.parse import urlparse, urljoin

def is_safe_redirect_url(target):
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return (
        redirect_url.scheme in ("http", "https")
        and host_url.netloc == redirect_url.netloc
    )


def get_safe_redirect(url):

    if url and is_safe_redirect_url(url):
        return url

    url = request.referrer
    if url and is_safe_redirect_url(url):
        return url

    return "/"


```


Just pass your url to get\_safe\_redirect.

The above is a courtesy of the shopyoapi.security from the [Shopyo](https://github.com/Abdur-rahmaanJ/shopyo) project.
