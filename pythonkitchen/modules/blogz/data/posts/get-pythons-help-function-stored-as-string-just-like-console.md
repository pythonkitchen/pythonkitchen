title: Get Python's help() function stored as string just like console
slug: get-pythons-help-function-stored-as-string-just-like-console
pub: Wed, 24 Jul 2019 19:36:53 +0000


Python's help function lets you see the help message written for you by the developer. It is particularly useful in IDLE / shell to inspect modules and explore.




Here is a sample shell demo





```python
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```



Now if we want to store that text in a string, if we try x = help(print), we get not a string, but a surprise:





```python
>>> x = help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> x
>>> x
>>> type(x)
<class 'NoneType'>
>>>

```



Ugh. How the to get the doctring as a string?




![](https://images.unsplash.com/photo-1541807120430-f3f78c281225?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80)


In Enters Pydoc
---------------




[Pydoc](https://docs.python.org/3/library/pydoc.html) is used to generate documentations




Here is the snippet to store the docstring as a variable





```python
from pydoc import render_doc
doctring = render_doc(print)
```



Simple isn't it?




instead of print, add any module.



