title: Python EFL: Scalable GUIs with Generic List (Genlist) (2026)
slug: python-efl-8
pub: 2026-02-24 17:00:00
authors: arj
tags: efl, enlightenment, gui series, genlist, performance, python tutorial
category: gui development
related_posts: python-efl-7,python-efl-9,python-efl-1

Handling thousands of UI elements without slowing down your app? This Python EFL tutorial introduces the **Genlist** (Generic List) widget. Unlike the standard List widget, Genlist is designed for massive datasets using a virtualization pattern that only renders items currently visible on the screen.

### TL;DR: Genlist Summary
- **Genlist**: A high-performance, virtualized list widget.
- **GenlistItemClass**: A template class that defines how items look and behave.
- **GenlistItem**: The data object that populates the list.
- **Best For**: Large data sets (1,000+ items), custom row layouts, and complex mobile-style lists.

---

## Defining the Genlist Widget
The **Genlist** is the "heavy duty" list widget in the Elementary toolkit. It works by decoupling the data from the UI representation. Instead of creating 5,000 widgets for 5,000 items, Genlist creates only enough widgets to fill the screen and reuses them as the user scrolls. This makes it incredibly efficient for system memory and CPU.

---

## Code Example: Implementing a Basic Genlist
This example shows how to create a `GenlistItemClass` to define row text and how to populate the `Genlist` container.

```python
'''
Abdur-Ramaan Janhangeer
Updated from Jeff Hoogland's tutos
for Python3.9 and Python-elf 1.25.0

https://www.toolbox.com/tech/programming/blogs/pyefl-tutorial-8-genlist-120215/
'''

import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.genlist import Genlist, GenlistItem, GenlistItemClass

from elmextensions import StandardPopup

ListItems = ["Apples",
            "Bananas",
            "Cookies",
            "Fruit Loops",
            "Milk",
            "Apple Juice",
            "BBQ Sauce",
            "Nesquik",
            "Trail Mix",
            "Chips",
            "Crackers",
            "Cheese",
            "Peanutbutter",
            "Jelly",
            "Ham",
            "Turkey",
            "Potatos",
            "Stuffing",
            "Tomato Sauce",
            "Pineapple",
            "Hot Dog Chili Sauce",
            "Stewed Tomatoes",
            "Creamed Corn",
            "Cream of Mushroom Soup",
            "Peaches",
            "Chilies and Tomatoes",
            "Cream of Chicken Soup",    
            "Cherry Pie Filling",   
            "Canned Beans (various)",
            "Cream of Tomato Soup", 
            "Apple Pie Filling",
            "Canned Peas",
            "Green Beans"
            ]

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL

class GLIC(GenlistItemClass):
    def __init__(self):
        GenlistItemClass.__init__(self, item_style="default")

    def text_get(self, gl, part, data):
        return data["itemName"]

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex11", "Genlist List", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        our_list = Genlist(self)
        our_list.size_hint_weight = EXPAND_BOTH
        our_list.callback_activated_add(self.list_item_selected)

        ListItems.sort()

        for it in ListItems:
            li = GenlistItem(item_data={"itemName":it}, item_class=GLIC())
            li.append_to(our_list)

        our_list.show()

        self.resize_object_add(our_list)

    def list_item_selected(self, our_list, our_item):
        our_popup = StandardPopup(self, "You selected %s"%our_item.data["itemName"], "ok")
        our_popup.show()

if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Frequently Asked Questions (FAQ)

### Is Genlist hard to use compared to List?
It has a slightly steeper learning curve because you must define a "class" for the items, but this structure makes your code much more maintainable and scalable in the long run.

### Can I have different styles of items in the same list?
Yes. You can create multiple `GenlistItemClass` instances (e.g., one for headers, one for content) and assign them to different `GenlistItem` objects as you append them.

### Does Genlist support swipe gestures?
Yes. EFL was designed with mobile interfaces in mind (it powers the Tizen OS), so Genlist has built-in support for kinetic scrolling and flick gestures.

---

### Key Takeaways
- Use **Genlist** for any list that might grow significantly in size.
- The **GenlistItemClass** is where you define logic for labels, icons, and state.
- Always prefer Genlist over standard List for professional-grade Python applications.