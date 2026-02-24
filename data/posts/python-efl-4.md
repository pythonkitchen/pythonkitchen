title: Python EFL: Displaying and Selecting Images (2026)
slug: python-efl-4
pub: 2026-02-24 13:00:00
authors: arj
tags: efl, enlightenment, gui series, images, python tutorial, desktop apps
category: gui development
related_posts: python-efl-3,python-efl-5,python-efl-6

Looking for a high-performance way to display images in a Python GUI? This Python EFL tutorial covers the `Image` widget and the `FileselectorButton`, allowing you to build applications that can view and change images dynamically. Python-EFL is a wrapper around the Enlightenment GUI kit, designed for speed and visual richness.

### TL;DR: Image Handling Summary
- **Image Widget**: Used to display static or dynamic image files.
- **File Selector**: A built-in button that opens a native file picker.
- **Key Methods**: `file_set()` to load images and `tooltip_text_set()` for metadata.
- **Supported Formats**: Common formats include PNG, JPG, and GIF.

---

## What is Python EFL?
**Python EFL** is a set of Python bindings for the Enlightenment Foundation Libraries. It is particularly well-suited for developers who need to build "modern" looking applications that are extremely light on system resources, making it a favorite for Linux desktop and IoT development.

---

## Example 1: Simple Image Display
This first example shows the most basic way to load and display a PNG file in a standard window.

```python
'''
Abdur-Ramaan Janhangeer
Updated from Jeff Hoogland's tutos
for Python3.9 and Python-elf 1.25.0

https://www.toolbox.com/tech/operating-systems/blogs/py-efl-tutorial-4-displaying-images-042415/

Needs one image called image.png
'''

import efl.elementary as elm
from efl.elementary.image import Image
from efl.elementary.label import Label
from efl.elementary.window import StandardWindow
from efl.evas import EVAS_HINT_EXPAND

EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND


class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex1", "Hello Elementary", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())
        our_image = Image(self)
        our_image.size_hint_weight = EXPAND_BOTH
        our_image.file_set("image.png")
        our_image.tooltip_text_set("A picture!")
        our_image.show()
        self.resize_object_add(our_image)


if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()

```

---

## Example 2: Interactive Image Selection
In this version, we add a `FileselectorButton` that allows the user to browse their computer and update the displayed image.

```python
import os
import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.image import Image
from efl.elementary.box import Box
from efl.elementary.fileselector_button import FileselectorButton
from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL

EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL


class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex6", "Selected Image", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())
        self.our_image = our_image = Image(self)
        our_image.size_hint_weight = EXPAND_BOTH
        our_image.size_hint_align = FILL_BOTH
        our_image.file_set("image.png")
        our_image.tooltip_text_set("A picture!")
        our_image.show()

        our_button = FileselectorButton(self)
        our_button.size_hint_weight = EXPAND_HORIZ
        our_button.text = "Select new Image"
        our_button.callback_file_chosen_add(self.file_selected)
        our_button.show()

        our_box = Box(self)
        our_box.size_hint_weight = EXPAND_BOTH
        our_box.pack_end(our_image)
        our_box.pack_end(our_button)
        our_box.show()
        self.resize_object_add(our_box)

    def file_selected(self, fsb, selected_file):
        if selected_file:
            valid_extensions = [".png", ".jpg", ".gif"]
            file_name, file_extension = os.path.splitext(selected_file)
            if file_extension in valid_extensions:
                self.our_image.file_set(selected_file)


if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Frequently Asked Questions (FAQ)

### What image formats does Python EFL support?
EFL uses the Evas library, which supports common formats like PNG, JPEG, GIF, SVG, and TIFF. It can also support specialized formats depending on the loader modules installed on your system.

### How do I scale an image?
By default, the `Image` widget will respect the `size_hint_weight` and `size_hint_align` of its container. You can use `our_image.fill_outside_set(True)` or `aspect_fixed_set(True)` to control how the image scales within its allocated space.

### Can I load images from a URL?
While the `file_set` method is typically used for local files, you can use the `requests` library to download an image to a temporary file and then load it into the widget.

---

### Key Takeaways
- The **Image** widget is the primary way to handle graphics in EFL.
- **FileselectorButton** simplifies user-driven file interactions.
- Always validate file extensions before attempting to load a new image into the UI.
