title: a fix to tkinter output not showing
slug: a-fix-to-tkinter-output-not-showing
pub: Sun, 29 Apr 2018 21:08:30 +0000
authors: Abdur-RahmaanJ, tthuma1

tkinter is fine once you understand it. let us see what problem user vikas was having and how to fix it!

[caption id="attachment\_85" align="aligncenter" width="168"]![tkinter no output](https://www.pythonmembers.club/wp-content/uploads/2018/04/IMG-20180429-WA0001-168x300.jpg) tkinter no output[/caption]
the fix
=======


a basic tkinter skeleton is

```python
import tkinter as tk

root = tk.Tk()

root.mainloop()
```

now we see that the user has it in place, so no output means the label he defined is not showing.

now the syntax for elements is :

Element(window, ...

we see that the user did not specify the window in which the element is to be placed

so, the fix is simple !

```python
title = tk.label(window, text='hello')


```

 
