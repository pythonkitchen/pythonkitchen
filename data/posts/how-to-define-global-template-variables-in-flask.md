title: How to define global template variables in Flask
slug: how-to-define-global-template-variables-in-flask
pub: 2021-02-24 08:10:13
authors: arj
tags: 
category: flask

Let's say you want to have some variables available in all templates by default. There's how you do it:


```python
@app.context_processor
    def inject_global_vars():
        return {'x': 1}

```


Now x is available everywhere. You can see it in action [here](https://github.com/Abdur-rahmaanJ/shopyo)
