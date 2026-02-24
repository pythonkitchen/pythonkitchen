title: Python EFL Tutorial: Creating Your First Window (2026)
slug: python-efl-1
pub: 2026-02-24 10:00:00
authors: arj
tags: efl, enlightenment, gui development, python tutorial, desktop apps
category: gui development
related_posts: python-efl-2,python-efl-3,how-to-install-python-efl-on-ubuntu-or-linux-mint

Looking to build desktop applications with the Enlightenment Foundation Libraries? This Python EFL tutorial provides a step-by-step guide to creating your first GUI window using the Elementary module. Python EFL is a powerful wrapper around the Enlightenment GUI kit, known for its performance and low resource usage.

### TL;DR: Quick Start Guide
- **Prerequisite**: Install Python EFL on your system.
- **Goal**: Create a standard window with a "Hello World" label.
- **Key Modules**: `efl.elementary` for high-level widgets.
- **Best For**: Lightweight, high-performance desktop applications.

---

## What is Python EFL?
**Python EFL** is a set of Python bindings for the Enlightenment Foundation Libraries (EFL). It allows developers to create visually rich and high-performance graphical user interfaces (GUIs) using Python. Unlike heavier frameworks, EFL is designed to be efficient on everything from mobile devices to high-end desktops.

### Comparison: Python EFL vs. Other Frameworks

| Feature | Python EFL | Tkinter | PyQt/PySide |
| :--- | :--- | :--- | :--- |
| **Performance** | High (C-based) | Low/Moderate | Moderate/High |
| **Visuals** | Rich/Themable | Basic/Native | Modern/Native |
| **Resource Usage** | Very Low | Low | Moderate/High |
| **Best For** | IoT & Desktops | Simple Tools | Complex Apps |

---

## Building Your First Window

Before diving into the code, ensure you have the environment ready. If you haven't installed the libraries yet, check our guide on [How to install Python-efl on Ubuntu or Linux Mint](https://www.pythonkitchen.com/how-to-install-python-efl-on-ubuntu-or-linux-mint/).

### The Code
The following example demonstrates how to initialize Elementary, create a `StandardWindow`, and add a `Label` widget.

```python
import efl.elementary as elm
from efl.elementary.label import Label
from efl.elementary.window import StandardWindow
from efl.evas import EVAS_HINT_EXPAND

# Utility constant for widget expansion
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND

class MainWindow(StandardWindow):
    def __init__(self):
        # Create a standard window with name, title, and size
        StandardWindow.__init__(self, "ex1", "Hello Elementary", size=(300, 200))
        
        # Set exit callback when the window is closed
        self.callback_delete_request_add(lambda o: elm.exit())
        
        # Add a Label widget
        label = Label(self)
        label.size_hint_weight = EXPAND_BOTH
        label.text = "Hello Elementary!"
        label.show()
        
        # Add the label to the window's internal resize list
        self.resize_object_add(label)

if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

### Key Components Explained
1.  **`elm.init()`**: Initializes the Elementary library.
2.  **`StandardWindow`**: A high-level window class that provides common features like a title bar.
3.  **`callback_delete_request_add`**: Connects the window's close button to the exit function.
4.  **`size_hint_weight`**: Determines how the widget expands within its container.
5.  **`elm.run()`**: Starts the main event loop.

---

## Common Errors & Fixes
- **Error**: `ModuleNotFoundError: No module named 'efl'`
  - **Fix**: Ensure Python EFL is installed via your package manager (e.g., `apt install python3-efl`).
- **Error**: Window opens and immediately closes.
  - **Fix**: Verify that `elm.run()` is called at the end of your script.

---

## Frequently Asked Questions (FAQ)

### Is Python EFL better than Tkinter?
Python EFL offers better performance and more advanced theming capabilities, making it ideal for resource-constrained systems or custom-designed interfaces. Tkinter is better for simple, native-looking internal tools.

### Do I need to call `elm.shutdown()`?
As of version 1.14, the Python module automatically handles cleanup on exit. You no longer need to call `elm.shutdown()` manually, though doing so carries no penalty.

### Can I run Python EFL on Windows?
While primarily developed for Linux and BSD systems, it is possible to run EFL on Windows via WSL or specific ports, though the Linux experience is significantly more stable.

---

### Key Takeaways
- Python EFL provides a high-performance alternative to traditional GUI frameworks.
- The `elementary` module is the recommended way to build modern interfaces.
- Always use `elm.init()` and `elm.run()` to manage the application lifecycle.