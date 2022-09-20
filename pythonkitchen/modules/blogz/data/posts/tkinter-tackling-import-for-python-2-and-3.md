title: tkinter : tackling import for python 2 and 3
slug: tkinter-tackling-import-for-python-2-and-3
pub: Wed, 25 Apr 2018 11:52:45 +0000
authors: tthuma1

[caption id="" align="aligncenter" width="480"]![tkinter logo](https://i.ytimg.com/vi/QQv_e61sqxs/hqdefault.jpg) gui package for python[/caption]

tkinter is the integrated GUI package in python. It has had an import naming change in python 3. This is the main hindrance in making tkinter codes run on python 3 or vice versa. fortunately the fix is a simple one
Some syntax
-----------


in python 2 we imported as :

```python

import Tkinter


```

and in python 3 we import as :

```python

import tkinter


```

notice the T in py2
The fix
-------


Here is a tip for cross platforming :

```python
try:
 import tkinter
except ImportError:
 import Tkinter

```

What it does
------------


it imports the py3 version, if ok, it continues if no ... it imports the python2 version, simple !
