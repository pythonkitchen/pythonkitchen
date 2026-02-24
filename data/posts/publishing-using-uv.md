title: Publishing a Python Package with uv and a PyPI Token
slug: publish-python-package-using-uv-pypi-token
pub: 2026-02-09 10:30:00
authors: abdur-rahmaan-janhangeer
tags: package management, uv, publishing
category: devops
related_posts: rye-package-manager,upload-your-package-to-pypi,python-running-makefile-on-windows

Publishing a Python package used to feel like a small battle: setup.py rituals, half-forgotten twine commands, and the anxiety of accidentally pushing a broken release to PyPI. Thankfully, modern tooling has cleaned all of this up.

With **uv**, publishing a Python package is fast, minimal, and refreshingly boring. In this article, we’ll walk through how to publish a Python package using **uv** and a **PyPI API token**, end to end, without unnecessary ceremony.

If you already know Python and want a clean, modern publishing flow, this guide will feel right at home.

Table of Contents
=================

* What is uv and Why Use It?
* Prerequisites
* Project Structure
* Configuring pyproject.toml
* Creating a PyPI API Token
* Publishing with uv
* Common Pitfalls
* Key Takeaways
* Conclusion


## What is uv and Why Use It?

uv is a modern Python toolchain written in Rust that replaces a whole collection of traditional tools like pip, virtualenv, pip-tools, and parts of setuptools.

Why uv is gaining serious traction:

- Extremely fast dependency resolution
- First-class support for pyproject.toml
- Clean build and publish workflows
- Fewer configuration files and fewer surprises

In short: less tooling drama, more shipping.


## Prerequisites

Before publishing your package, make sure you have:

- Python 3.8 or newer
- A PyPI account
- uv installed on your system
- A package that actually imports and runs

To install uv:

```
curl -Ls https://astral.sh/uv/install.sh | sh
```


## Project Structure

A clean project structure avoids confusion and keeps PyPI happy. A minimal recommended layout looks like this:

```
my_package/
├── src/
│ └── my_package/
│ ├── init.py
│ └── core.py
├── README.md
├── pyproject.toml
└── LICENSE
```

Important notes:

- Use the src layout to avoid import bugs
- The package name must be importable
- README.md becomes your PyPI project description


## Configuring pyproject.toml

The pyproject.toml file is the single source of truth for modern Python packaging. A minimal and solid configuration looks like this:

```
[project]
name = "my-package"
version = "0.1.0"
description = "A small but useful Python package"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [
{ name = "Your Name", email = "you@example.com" }
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

This setup avoids legacy tooling and works perfectly with uv.


## Creating a PyPI API Token

Uploading with a username and password is deprecated. PyPI strongly recommends using API tokens instead.

Steps:

1. Log in to PyPI
2. Go to Account Settings → API tokens
3. Create a new token
4. Choose either full-account access or project-specific access
5. Copy the token immediately

The token will look something like this:

pypi-AgEIcHlwaS5vcmcCJ...



## Publishing with uv

Build your package:

`uv build`


This generates both a source distribution and a wheel.

Finally, publish to PyPI:

`uv publish`

Create a token in pypi.

Add your username as `__token__` and your actual token as the password.


If everything is configured correctly, your package will be live within seconds.


## Common Pitfalls

Even with great tooling, a few mistakes still show up often:

- Forgetting to bump the version number
- Choosing a package name that already exists on PyPI
- Broken Markdown in the README
- Missing `__init__`.py files in the package

Catching these early saves a lot of frustration.


## Key Takeaways

- uv simplifies Python packaging dramatically
- pyproject.toml is all you need for configuration
- PyPI API tokens are safer and automation-friendly
- Publishing can be boring, fast, and reliable


## Conclusion

Publishing Python packages no longer needs to feel fragile or ceremonial. With uv, the workflow is fast, modern, and predictable. You write code, declare metadata, run two commands, and ship.

Once you’ve used this flow a few times, going back to older tooling feels unnecessary.

Happy packaging.