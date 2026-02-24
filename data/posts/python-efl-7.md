title: Python EFL: Building Standard and Searchable Lists (2026)
slug: python-efl-7
pub: 2026-02-24 16:00:00
authors: arj
tags: efl, enlightenment, gui series, lists, widgets, python tutorial
category: gui development
related_posts: python-efl-6,python-efl-8,python-efl-9

Need to display a large amount of selectable data in your app? This Python EFL tutorial covers the `List` widget and the `SearchableList` extension. Lists are foundational for navigation menus, file browsers, and settings panels in any GUI application.

### TL;DR: List Widget Summary
- **Basic List**: A simple vertical scrollable container for text items.
- **Searchable List**: An extended widget that adds a filter bar to find items quickly.
- **Interactivity**: Use the `activated` callback to detect when a user clicks an item.
- **Best For**: Menus or data sets with fewer than 100 items.

---

## Defining the List Widget
The **Elementary List** is a widget used to display a sequence of items. It supports scrolling, multiple selection modes, and various styles. While the basic list is perfect for simple choices, the `SearchableList` from the Elm Extensions library adds an integrated entry widget to filter results in real-time.

---

## Example 1: Creating a Standard List
This code initializes a list, populates it with a variety of grocery items, and shows a popup when an item is selected.

```python
'''
Abdur-Ramaan Janhangeer
Updated from Jeff Hoogland's tutos
for Python3.9 and Python-elf 1.25.0

https://www.toolbox.com/tech/operating-systems/blogs/pyefl-tutorial-7-lists-111115/
'''

import efl.elementary as elm
from efl.elementary.window import StandardWindow
from efl.elementary.list import List

from elmextensions import StandardPopup
from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL

EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL
list_items = ["Apples",
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


class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex9", "List", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        our_list = List(self)
        our_list.size_hint_weight = EXPAND_BOTH
        our_list.callback_activated_add(self.list_item_selected)

        list_items.sort()

        for it in list_items:
            our_list.item_append(it)

        our_list.go()
        our_list.show()

        self.resize_object_add(our_list)

    def list_item_selected(self, our_list, our_item):
        our_popup = StandardPopup(self, "You selected %s"%our_item.text, "ok")
        our_popup.show()

if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Example 2: Adding Search Functionality
By using the `SearchableList` extension, you can allow users to filter the list instantly as they type.

```python
import efl.elementary as elm
from efl.elementary.window import StandardWindow

from elmextensions import SearchableList
from elmextensions import StandardPopup
from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL


EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL
list_items = ["Apples",
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


class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "ex10", "Searchable List", size=(300, 200))
        self.callback_delete_request_add(lambda o: elm.exit())

        search_list = SearchableList(self)
        search_list.size_hint_weight = EXPAND_BOTH
        search_list.lst.callback_activated_add(self.list_item_selected)

        list_items.sort()

        for it in list_items:
            search_list.item_append(it)

        search_list.show()

        self.resize_object_add(search_list)

    def list_item_selected(self, ourList, our_item):
        our_popup = StandardPopup(self, "You selected %s"%our_item.text, "ok")
        our_popup.show()

if __name__ == "__main__":
    elm.init()
    gui = MainWindow()
    gui.show()
    elm.run()
```

---

## Frequently Asked Questions (FAQ)

### When should I use `List` vs `Genlist`?
Use **List** for simple collections of strings or basic icons. Use **Genlist** (Generic List) when you have thousands of items or need custom complex layouts for each row, as Genlist uses data-object virtualization for better performance.

### How do I enable multiple selection?
You can set `our_list.multi_select_set(True)` to allow users to select more than one item at a time.

### Can I add images to list items?
Yes. The `item_append` method can take an image object as an argument to display an icon next to the text.

---

### Key Takeaways
- Lists are the most efficient way to handle sequential user choices.
- `our_list.go()` is required after appending items to trigger the layout update.
- Use extensions like `SearchableList` to improve UX for larger data sets.