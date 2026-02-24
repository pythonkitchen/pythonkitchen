title: Python EFL: Building Custom Elementary Widgets (2026)
slug: python-efl-9
pub: 2026-02-24 18:00:00
authors: arj
tags: efl, enlightenment, gui series, custom widgets, oop, python tutorial
category: gui development
related_posts: python-efl-8,python-efl-7,python-efl-1

Want to create unique UI components tailored to your app's needs? This Python EFL tutorial teaches you how to build **Custom Widgets** by subclassing existing Elementary components. By encapsulating multiple widgets into a single class, you can create reusable, maintainable UI elements for any Enlightenment-based application.

### TL;DR: Custom Widget Summary
- **Encapsulation**: Grouping multiple widgets (like a Frame and an Image) into a single object.
- **Subclassing**: Inheriting from base classes like `Frame`, `Box`, or `Button`.
- **Reusability**: Write the widget logic once and reuse it across multiple windows or projects.
- **Best For**: Creating specialized components like custom media players, dashboard cards, or complex form fields.

---

## Defining Custom Widgets in EFL
A **Custom Widget** in Python EFL is simply a Python class that inherits from a standard Elementary widget class. By overriding the `__init__` method, you can add internal sub-widgets, set default properties, and define new methods. This object-oriented approach is the best practice for building scalable and professional GUI applications.

---

## Code Example: The PictureFrame Widget
This example demonstrates a custom `PictureFrame` widget that automatically includes an `Image` inside a `Frame`, with a helper method to update the image file.

```python
'''
Abdur-Ramaan Janhangeer
Updated from Jeff Hoogland's tutos
for Python3.9 and Python-elf 1.25.0

https://www.toolbox.com/tech/operating-systems/blogs/py-efl-tutorial-9-custom-elementary-widgets-020116/
'''

import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.frame import Frame
from efl.elementary.image import Image


from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class PictureFrame(Frame):
    def __init__(self, parent_widget, ourText=None, image=None, *args, **kwargs):
        Frame.__init__(self, parent_widget, *args, **kwargs)

        self.text = ourText

        self.our_image = Image(self)
        self.our_image.size_hint_weight = EXPAND_BOTH

        if image:
            self.our_image.file_set(image)

        self.content_set(self.our_image)

    def file_set(self, image):
        self.our_image.file_set(image)

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex12", "Custom Widget", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        our_picture_frame = PictureFrame(self)
        our_picture_frame.size_hint_weight = EXPAND_BOTH
        our_picture_frame.text = "A Custom Picture Frame"
        our_picture_frame.file_set("image.png")
        our_picture_frame.show()

        self.resize_object_add(our_picture_frame)

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    GUI.show()
    elm.run()
    elm.shutdown()
```

---

## Frequently Asked Questions (FAQ)

### Should I inherit from `Box` or `Table` for my custom widget?
If your widget is a container for many smaller widgets, inherit from **Box** (for linear layouts) or **Table** (for grids). If you just want to add a border and title around a single widget, inherit from **Frame**.

### Can I define custom callbacks?
Yes. You can use standard Python event patterns or use the `callback_add` system to define new signals that other parts of your application can listen to.

### Is there a performance hit for custom widgets?
No. Because these are standard Python classes and the sub-widgets are native C-based objects, the overhead is negligible. It is actually more efficient than manually recreating the same layout multiple times.

---

### Key Takeaways
- **Inheritance** allows you to extend the functionality of base EFL widgets.
- **`content_set`** is used by containers like Frame to hold their primary child widget.
- Custom widgets make your GUI code cleaner and more modular.