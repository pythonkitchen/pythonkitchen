title: Python EFL: Layouts, Weight Hints, and Callbacks (2026)
slug: python-efl-2
pub: 2026-02-24 11:00:00
authors: arj
tags: efl, enlightenment, gui series, layouts, callbacks, python tutorial
category: gui development
related_posts: python-efl-1,python-efl-3,python-efl-4

Mastering widget alignment and user interaction is crucial for any GUI application. This Python EFL tutorial explains how to use **Weight Hints**, **Boxes**, and **Callbacks** to create responsive layouts and interactive buttons. If you're new to the series, start with our [first window tutorial](https://www.pythonkitchen.com/python-efl-1/).

### TL;DR: Layout & Interaction Summary
- **Box Widget**: A container used to pack multiple widgets (labels, buttons) together.
- **Weight Hints**: Tell EFL how to distribute space among widgets.
- **Callbacks**: Functions that trigger when a user interacts with a widget (e.g., clicking a button).
- **Core Goal**: Create a window with a label and a button that exits the app.

---

## Understanding EFL Layout Logic
In Python EFL, widgets don't just sit on the screen; they belong to containers. The most common container is the **Box**, which can arrange items horizontally or vertically.

### What are Weight Hints?
Weight hints (`size_hint_weight`) are values ranging from 0.0 to 1.0. They define how much extra space a widget should take up. Using `EVAS_HINT_EXPAND` (which equals 1.0) ensures the widget expands to fill the available area.

---

## Implementation Example: Labels and Buttons
This script demonstrates packing a Label and a Button into a Box, then connecting the button to an exit callback.

```python
import efl.elementary as elm
from efl.elementary.box import Box
from efl.elementary.button import Button
from efl.elementary.label import Label
from efl.elementary.window import StandardWindow
from efl.evas import EVAS_HINT_EXPAND

# Expansion constant for cleaner code
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex2", "Interaction Demo", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        # 1. Create a Label
        our_label = Label(self)
        our_label.size_hint_weight = EXPAND_BOTH
        our_label.text = "Hello Elementary!"
        our_label.show()

        # 2. Create a Button with a Callback
        our_button = Button(self)
        our_button.size_hint_weight = EXPAND_BOTH
        our_button.text = "Click to Exit"
        our_button.callback_clicked_add(self.button_pressed)
        our_button.show()

        # 3. Create a Box container and pack widgets
        our_box = Box(self)
        our_box.size_hint_weight = EXPAND_BOTH
        our_box.pack_end(our_label)
        our_box.pack_end(our_button)
        our_box.show()

        # 4. Add the Box to the window
        self.resize_object_add(our_box)

    def button_pressed(self, btn):
        # This function runs when the button is clicked
        print("Exit button clicked!")
        elm.exit()

if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Structured Data: Layout Options

| Component | Description | Usage |
| :--- | :--- | :--- |
| **Box** | Linear container | `our_box.pack_end(widget)` |
| **Weight Hint** | Expansion logic | `widget.size_hint_weight = 1.0, 1.0` |
| **Alignment** | Positioning logic | `widget.size_hint_align = 0.5, 0.5` |
| **Callback** | Event handling | `widget.callback_clicked_add(func)` |

---

## Frequently Asked Questions (FAQ)

### What is the difference between `pack_start` and `pack_end`?
`pack_start` adds the widget to the beginning of the list (top or left), while `pack_end` adds it to the end (bottom or right).

### Why doesn't my widget fill the whole window?
Make sure you have set the `size_hint_weight` to `EXPAND_BOTH` and added the widget (or its container) to the window using `resize_object_add`.

### Can I nest Boxes inside Boxes?
Yes. You can pack a horizontal Box inside a vertical Box to create complex grid-like layouts without using a formal Grid widget.

---

### Key Takeaways
- Use **Boxes** for simple linear layouts.
- **Weight hints** are essential for responsive resizing.
- **Callbacks** bridge the gap between the UI and your Python logic.
