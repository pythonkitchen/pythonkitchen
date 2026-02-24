title: Python EFL: Managing Views with Naviframe (2026)
slug: python-efl-5
pub: 2026-02-24 14:00:00
authors: arj
tags: efl, enlightenment, gui series, navigation, naviframe, python tutorial
category: gui development
related_posts: python-efl-4,python-efl-6,python-efl-7

Need to manage multiple views or screens in your Python application? This Python EFL tutorial introduces the `Naviframe` widget, a powerful layout manager that acts like a stack of screens. It is the standard way to handle "forward" and "backward" navigation in modern Enlightenment-based interfaces.

### TL;DR: Navigation Summary
- **Naviframe**: A container that holds a stack of "items" (widgets).
- **Push Logic**: Add a new screen to the top of the stack using `item_simple_push()`.
- **Pop Logic**: Remove the current screen to go back to the previous one.
- **Best For**: Multi-step forms, wizards, and mobile-style application flows.

---

## Defining the Naviframe Entity
The **Naviframe** is one of the most versatile widgets in the Elementary toolkit. It handles the transition between different pieces of content, often automatically providing a title bar and a "back" button depending on how it is configured. This makes it ideal for building complex applications that need to stay organized within a single window.

---

## Code Example: Pushing Multiple Views
In this tutorial, we create a basic interface with buttons that "push" different widgets (an image and a label) onto the Naviframe stack.

```python
'''
Abdur-Ramaan Janhangeer
Updated from Jeff Hoogland's tutos
for Python3.9 and Python-elf 1.25.0

https://www.toolbox.com/tech/operating-systems/blogs/py-efl-tutorial-5-naviframe-070115/
'''

import efl.elementary as elm 
from efl.elementary.window import StandardWindow 
from efl.elementary.image import Image 
from efl.elementary.label import Label 
from efl.elementary.button import Button 
from efl.elementary.box import Box 
from efl.elementary.naviframe import Naviframe  
from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL 

EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND 
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0 
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL   

class MainWindow(StandardWindow):    
    def __init__(self):        
        StandardWindow.__init__(self, "ex7", "Naviframe", size=(300, 200))        
        self.callback_delete_request_add(lambda o: elm.exit())          
        static_image = static_image = Image(self)        
        static_image.size_hint_weight = EXPAND_BOTH        
        static_image.file_set("image.png")        
        static_image.tooltip_text_set("A picture!")        
        static_image.show() 

        our_label = our_label = Label(self)        
        our_label.size_hint_weight = EXPAND_BOTH        
        our_label.text = "Hey look some text!"        
        our_label.show()           

        self.nf = Naviframe(self)        
        self.nf.size_hint_weight = EXPAND_BOTH        
        self.nf.size_hint_align = FILL_BOTH        
        self.nf.show()

        button_one = Button(self)        
        button_one.size_hint_weight = EXPAND_BOTH        
        button_one.text = "Show image"        
        button_one.callback_clicked_add(self.button_pressed, static_image)        
        button_one.show()

        button_two = Button(self)        
        button_two.size_hint_weight = EXPAND_BOTH        
        button_two.text = "Show label"        
        button_two.callback_clicked_add(self.button_pressed, our_label)        
        button_two.show() 

        button_box = Box(self)        
        button_box.size_hint_weight = EXPAND_HORIZ        
        button_box.horizontal_set(True)        
        button_box.pack_end(button_one)        
        button_box.pack_end(button_two)        
        button_box.show()

        main_box = Box(self)        
        main_box.size_hint_weight = EXPAND_BOTH        
        main_box.pack_end(self.nf)        
        main_box.pack_end(button_box)        
        main_box.show()    

        self.nf.item_simple_push(static_image)                
        self.resize_object_add(main_box)            
    def button_pressed(self, btn, our_object):        
        self.nf.item_simple_push(our_object)   

if __name__ == "__main__":    
    elm.init()    
    gui = MainWindow()    
    gui.show()    
    elm.run()
```

---

## Frequently Asked Questions (FAQ)

### Can I pop items from the Naviframe programmatically?
Yes. You can use `self.nf.item_pop()` to remove the top item from the stack and return to the previous view.

### Does Naviframe support transitions?
By default, Naviframe uses the theme's standard transition (often a slide or fade). You can customize this by changing the Elementary theme or using specific transition hints.

### Can a widget belong to more than one Naviframe item?
No. A widget can only have one parent. If you try to push a widget that is already in the Naviframe (or elsewhere), it will be moved from its current location to the top of the stack.

---

### Key Takeaways
- Use **Naviframe** for screen-based navigation.
- `item_simple_push()` is the easiest way to add content.
- It automatically manages visibility, so you don't have to call `hide()` or `show()` on individual screens.
