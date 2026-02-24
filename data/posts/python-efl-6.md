title: Python EFL: Extending UI with Elm Extensions (2026)
slug: python-efl-6
pub: 2026-02-24 15:00:00
authors: arj
tags: efl, enlightenment, gui series, extensions, popup, python tutorial
category: gui development
related_posts: python-efl-5,python-efl-7,python-efl-8

Want to speed up your Python EFL development? This tutorial introduces **Elm Extensions**, a library that provides simplified versions of common widgets like buttons, popups, and about windows. By using these extensions, you can write less boilerplate code while maintaining the high performance of the Enlightenment Foundation Libraries.

### TL;DR: Extensions Summary
- **StandardButton**: A wrapper that handles common click events with less code.
- **StandardPopup**: A quick way to show alert messages to the user.
- **Dependency**: Requires the `python3-elm-extensions` library.
- **Best For**: Rapid prototyping and consistent UI components.

---

## What are Elm Extensions?
**Elm Extensions** (Elementary Extensions) are a set of helper classes built on top of the standard `efl.elementary` widgets. They are designed to automate repetitive tasks, such as setting up callbacks or managing basic popup logic, making Python EFL more accessible for developers used to higher-level frameworks.

### Prerequisite
To follow this tutorial, you need to install the extensions library:
```bash
# Clone and install
git clone https://github.com/BodhiDev/python3-elm-extensions
cd python3-elm-extensions
pip install .
```

---

## Code Example: Buttons and Popups
This example demonstrates how to use the `StandardButton` to trigger a `StandardPopup` with just a few lines of code.

```python
'''
Abdur-Ramaan Janhangeer
Updated from Jeff Hoogland's tutos
for Python3.9 and Python-elf 1.25.0

https://www.toolbox.com/tech/operating-systems/blogs/py-efl-tutorial-6-elmextensions-110115/
'''

'''
extentions
'''

AUTHORS = """
<br>
<align=center>
<hilight>Jeff Hoogland (Jef91)</hilight><br>
<link><a href=http://www.jeffhoogland.com>Contact</a></link><br><br>
</align>
"""

LICENSE = """
<align=center>
<hilight>
GNU GENERAL PUBLIC LICENSE<br>
Version 3, 29 June 2007<br><br>
</hilight>
This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or 
(at your option) any later version.<br><br>
This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details.<br><br>
You should have received a copy of the GNU General Public License 
along with this program. If not, see<br>
<link><a href=http://www.gnu.org/licenses>http://www.gnu.org/licenses/</a></link>
</align>
"""

INFO = """
<align=center>
<hilight>Elementary Python Extensions</hilight> are awesome!<br> 
<br>
<br>
</align>
"""
import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.box import Box

from elmextensions import StandardButton
from elmextensions import StandardPopup
from elmextensions import AboutWindow


from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex8", "ElmEx - Button and Popup", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        our_button = StandardButton(self, "Show Popup", cb_onclick=self.button_pressed)
        our_button.size_hint_weight = EXPAND_HORIZ
        our_button.size_hint_align = FILL_BOTH
        our_button.show()


        main_box = Box(self)
        main_box.size_hint_weight = EXPAND_BOTH
        main_box.size_hint_align = FILL_BOTH
        main_box.pack_end(our_button)
        main_box.show()

        self.resize_object_add(main_box)

    def button_pressed(self, btn):
        ourPopup = StandardPopup(self, "Press OK to close this message.", "ok")
        ourPopup.show()


if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Frequently Asked Questions (FAQ)

### Are Elm Extensions part of the official Python EFL package?
No, they are a community-maintained library (originally by Jeff Hoogland) that provides a higher-level abstraction layer. You must install them separately.

### Can I mix standard Elementary widgets with Extensions?
Yes. Extensions are subclasses of standard widgets, so they are fully compatible with any other EFL component.

### Is there an extension for complex layouts?
The library includes an `AboutWindow` class which is a pre-configured template for application credits, but for general layouts, you should still use standard `Box`, `Grid`, or `Table` widgets.

---

### Key Takeaways
- **Efficiency**: Extensions reduce the amount of code needed for standard UI patterns.
- **Standardization**: They help maintain a consistent look and feel across your application.
- **Modernized**: This updated 2026 version ensures support for the latest Python distributions.