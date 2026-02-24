title: How to Import Tkinter in Python 2 and 3: A Cross-Compatibility Guide
slug: tkinter-tackling-import-for-python-2-and-3
pub: 2018-04-25 11:52:45
authors: arj
tags: tkinter, compatibility, legacy
category: gui development
related_posts: a-fix-to-tkinter-output-not-showing,tkinter-text-widget-tags,packaging-an-sqlite-db-included-crud-pyqt5-app-using-pyinstaller

Tkinter is the standard GUI (Graphical User Interface) package that comes bundled with most Python installations. However, if you are working on a codebase that needs to support both Python 2 and Python 3, or if you are porting an older project, you will quickly run into a common stumbling block: the import naming change.

In this guide, we'll look at why this change happened and how to write code that works seamlessly across both versions of Python.

## The Naming Shift

The main difference between the two versions is a simple case change:

*   **In Python 2**, the module is named `Tkinter` (capital 'T').
*   **In Python 3**, the module was renamed to `tkinter` (lowercase 't') as part of a larger effort to standardize module naming conventions (PEP 8).

### Python 2 Syntax
```python
import Tkinter
root = Tkinter.Tk()
```

### Python 3 Syntax
```python
import tkinter
root = tkinter.Tk()
```

This tiny difference is enough to cause an `ImportError` that crashes your program if you try to run Python 2 code in a Python 3 environment.

---

## The Universal Fix: Try/Except Block

The most robust way to handle this without requiring external libraries is to use a `try...except` block. This allows your script to attempt the Python 3 import first and fall back to Python 2 if it fails.

```python
try:
    # Attempt Python 3 import
    import tkinter as tk
except ImportError:
    # Fallback for Python 2
    import Tkinter as tk

# Now you can use 'tk' regardless of the Python version
root = tk.Tk()
root.title("Cross-Platform Tkinter")
root.mainloop()
```

### Why use `as tk`?
By aliasing the module to `tk`, you ensure that the rest of your code remains identical. You don't have to keep checking which version of the module you are using; you just call `tk.Button()`, `tk.Label()`, etc.

---

## Handling Submodules (Advanced)

Sometimes you need specific submodules like `messagebox` or `filedialog`. These also changed significantly in Python 3. In Python 2, they were often separate modules like `tkMessageBox`.

Here is how you handle them for cross-compatibility:

```python
try:
    # Python 3
    from tkinter import messagebox
    from tkinter import filedialog
except ImportError:
    # Python 2
    import tkMessageBox as messagebox
    import tkFileDialog as filedialog

# Example usage
messagebox.showinfo("Hello", "This works in both versions!")
```

## Conclusion

Tackling the Python 2 and 3 divide in Tkinter is easy once you know the `try/except` pattern. By using this approach, you can write modern GUI applications that are accessible to users on older systems while remaining fully compatible with the latest Python releases.

If you're starting a brand new project, we highly recommend sticking exclusively to Python 3, as Python 2 has reached its end-of-life (EOL). However, for maintenance and porting, these tips are essential tools in your Python developer toolkit.