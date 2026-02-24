title: Python EFL: Advanced Align Hints and Weight Control (2026)
slug: python-efl-3
pub: 2026-02-24 12:00:00
authors: arj
tags: efl, enlightenment, gui series, layouts, alignment, python tutorial
category: gui development
related_posts: python-efl-2,python-efl-4,python-efl-5

Positioning widgets precisely is the difference between a amateur tool and a professional application. This Python EFL tutorial dives deep into **Align Hints** and **Weight Control**, showing you how to anchor widgets to specific parts of a window.

### TL;DR: Alignment Summary
- **Weight**: Determines if a widget *wants* extra space.
- **Align**: Determines where the widget *sits* within that space (0.0 to 1.0).
- **FILL**: A special align hint that forces the widget to stretch across the available space.
- **Core Goal**: Learn to center, anchor, or stretch buttons using Evas hints.

---

## Weight vs. Align: The Core Difference
In the Enlightenment Foundation Libraries (EFL), layout is a two-step process:
1.  **Weight (`size_hint_weight`)**: The container asks, "Does this widget need more room?"
2.  **Align (`size_hint_align`)**: If there is extra room, the container asks, "Where should I put the widget?"

### Common Alignment Values

| Value | Effect |
| :--- | :--- |
| **(0.5, 0.5)** | Centered (Horizontal, Vertical) |
| **(0.0, 0.0)** | Top-Left corner |
| **(1.0, 1.0)** | Bottom-Right corner |
| **EVAS_HINT_FILL** | Stretches to fill the entire cell |

---

## Code Example: Mastering Hints
This example shows three buttons with different weight and align configurations to demonstrate how they interact.

```python
import efl.elementary as elm
from efl.elementary.box import Box
from efl.elementary.button import Button
from efl.elementary.window import StandardWindow
from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL

# Constants
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex3", "Weight & Align Demo", size=(300, 400))
        self.callback_delete_request_add(lambda o: elm.exit())

        # Button 1: No expansion, but fills its narrow row
        btn1 = Button(self)
        btn1.size_hint_weight = (0, 0)
        btn1.size_hint_align = FILL_BOTH
        btn1.text = "Fixed Size (Fill)"
        btn1.show()

        # Button 2: Fully expands and fills the window
        btn2 = Button(self)
        btn2.size_hint_weight = EXPAND_BOTH
        btn2.size_hint_align = FILL_BOTH
        btn2.text = "Expanding (Fill)"
        btn2.show()

        # Button 3: Anchored to the bottom-right
        btn3 = Button(self)
        btn3.size_hint_weight = EXPAND_BOTH
        btn3.size_hint_align = (1.0, 1.0) # Bottom Right
        btn3.text = "Anchored Corner"
        btn3.show()

        # Container
        our_box = Box(self)
        our_box.size_hint_weight = EXPAND_BOTH
        our_box.pack_end(btn1)
        our_box.pack_end(btn2)
        our_box.pack_end(btn3)
        our_box.show()

        self.resize_object_add(our_box)

if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Frequently Asked Questions (FAQ)

### What happens if I set `align` without `weight`?
If `weight` is 0, the container won't give the widget any extra space. Therefore, the `align` hint will have no visible effect because there is no room to "move" or "fill" within.

### How do I perfectly center a button?
Set `size_hint_weight` to `EXPAND_BOTH` and `size_hint_align` to `(0.5, 0.5)`. This gives the button all available space but forces it to sit exactly in the middle of that space.

### Is `EVAS_HINT_FILL` a specific number?
Yes, in the underlying C library, `EVAS_HINT_FILL` is usually represented as `-1.0`. It acts as a flag to tell the layout engine to ignore margins and stretch the object.

---

### Key Takeaways
- **Weight** creates space; **Align** uses it.
- Use `(0.0, 0.0)` to `(1.0, 1.0)` for fractional positioning.
- Combine these hints to create complex, responsive interfaces that look great on any screen size.
