title: Securing Flask: Preventing Open Redirect Vulnerabilities
slug: how-prevent-open-redirect-vulnerab-flask
pub: 2021-02-24 08:24:00
authors: arj
tags: flask, security, python, web-development, owasp
category: flask, security

If your Flask application uses a `next` parameter to redirect users after login, you might be vulnerable to **Open Redirects**.

This is a subtle but dangerous vulnerability where an attacker manipulates your site to redirect users to a malicious phishing page. Because the link starts with *your* trusted domain, users are more likely to click it.

## The Vulnerability Explained

Imagine your login logic looks like this:

```python
# VULNERABLE CODE
@app.route('/login', methods=['POST'])
def login():
    # ... verify credentials ...
    next_page = request.args.get('next')
    return redirect(next_page or url_for('home'))
```

An attacker can craft a URL like:
`https://yoursite.com/login?next=http://malicious-site.com/steal-credentials`

When the user logs in, your server happily redirects them to `malicious-site.com`. The user, thinking they are still in your trusted workflow, might re-enter their password on the fake site.

---

## The Fix: Validating the Target URL

To prevent this, we must ensure that the `next` URL is safe. A "safe" URL is either:
1.  **Relative:** Starts with a `/` (e.g., `/dashboard`).
2.  **Internal:** Has the same host/domain as your application.

We can write a robust helper function using Python's `urllib.parse`.

### The `is_safe_url` Helper

```python
from urllib.parse import urlparse, urljoin
from flask import request

def is_safe_url(target):
    """
    Ensures a redirect target is safe (internal).
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    
    return (
        test_url.scheme in ('http', 'https') and 
        ref_url.netloc == test_url.netloc
    )
```

### Implementing the Secure Redirect

Now, update your view function to use this check:

```python
@app.route('/login', methods=['POST'])
def login():
    # ... verify credentials ...
    
    next_page = request.args.get('next')
    
    # SECURITY CHECK
    if not next_page or not is_safe_url(next_page):
        next_page = url_for('home')
        
    return redirect(next_page)
```

---

## How It Works

1.  **`urljoin`:** We use `urljoin` to handle relative paths correctly. If `target` is just `/dashboard`, it resolves to `http://yoursite.com/dashboard`.
2.  **`urlparse`:** This breaks the URL into components (scheme, netloc, path).
3.  **`netloc` Check:** We compare the network location (domain) of the request with the target. If they don't match, it's an external link, and we block it.

## Summary

The "Open Redirect" is a classic OWASP vulnerability that is easy to introduce but also easy to fix.

**Rule of Thumb:** Never trust user input, especially when it dictates where the browser should go next. Always validate the `next` parameter against your own domain whitelist.