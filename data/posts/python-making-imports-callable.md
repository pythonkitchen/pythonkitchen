title: Python: Making Imports Callable
slug: python-making-imports-callable
pub: 2021-10-21 17:19:06
authors: arj
tags: 
category: snippets

I wanted to do


```python
import module
module()

```


I thought this did not exist in Python but [Chris Angelico](https://github.com/Rosuav), a Python core dev showed me it existed!


```python
# importme.py
import sys, types
class Module(types.ModuleType):
    def __call__(self):
        print("You called me!")
sys.modules[__name__].__class__ = Module

# other_file.py
import importme
importme()

```


Mind boggling!
