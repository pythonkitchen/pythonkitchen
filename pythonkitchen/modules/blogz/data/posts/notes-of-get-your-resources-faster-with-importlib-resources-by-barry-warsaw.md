title: Notes of Get your resources faster, with importlib.resources by Barry Warsaw
slug: notes-of-get-your-resources-faster-with-importlib-resources-by-barry-warsaw
pub: Sun, 12 Dec 2021 17:53:11 +0000
authors: Abdur-RahmaanJ

[Talk](https://www.youtube.com/watch?v=ZsGFU2qh73E) notes


```python
thepkg/ # is a package since has __init__.py
    __init__.py
    a.py
    b.py
    data/
        sample.dat

```


You need to get data files (templates, certifs etc) from your package

You do


```python
import thepkg
from pathlib import Path

pkg = Path.(thepkg.__file__).parent
path = pkg / 'data' / 'sample.dat'

```


Problem as `__file__` not necessarily a real file on system

Package: pkg\_resources: import-time side effects

goes over syspath, if you have many, takes time.

Solution:

Use 'new' in-built python thing


```python
from importlib.resources import read_binary
contents = read_binary('thepkg,data', 'sample.data')
# or read_binary(thepkg,data, 'sample.data')

```


in case error


```python
thepkg/ 
    __init__.py
    a.py
    b.py
    data/
        __init__.py # add this
        sample.dat

```


Pakage? Any importable module with a `__path__` attribute.

Resource? Any readable object inside package, like files

subdirs and subpackages not resources

namespace packages cannot contain resources

importlib.resources

read\_text -> str

open\_binary -> BinaryIO (use with open\_b...)

open\_text -> TextIO

path(package, resource) -> `Iterator[path]`

with path ... as lib

contents(package) -> `list[str]`

is\_resource(package, name: str) # use with contents

loader.get\_resource\_reader

abc # means abstract base class
