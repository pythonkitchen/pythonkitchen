title: Creating Smooth Mouse Trails in Processing.py using OOP
slug: processing-py-trails-using-oop
pub: 2018-04-26 05:13:45
authors: arj
tags: python, processing.py, oop, creative-coding, animation
category: oop, processing.py

In creative coding, adding a "trail" effect can transform a simple animation into something dynamic and visually appealing. A trail is essentially a visual history of where an object has been. In this post, we’ll explore how to implement this using an **Object-Oriented Programming (OOP)** approach in Processing.py.

## Why Use OOP for Trails?

While you could hardcode a list of coordinates in your main `draw()` loop, using a class makes your code:
1.  **Modular:** You can easily add multiple objects with their own independent trails.
2.  **Clean:** All logic related to the trail (updating, storing, and drawing) is contained in one place.
3.  **Reusable:** You can copy this class into any other Processing project.

---

## The Implementation

The strategy is simple: we maintain a "history" list of the mouse's past coordinates. Each frame, we add the current position and remove the oldest one if the list gets too long.

### The Full Code

```python
class MouseTrail:
    def __init__(self, max_length=100):
        # A list to store [x, y] coordinates
        self.history = []
        self.max_length = max_length
        
    def update(self):
        # Add current mouse position
        self.history.append([mouseX, mouseY])
        
        # Keep the history at a manageable length
        if len(self.history) > self.max_length:
            self.history.pop(0)
            
    def display_mouse(self):
        # Draw a circle at the current mouse position
        fill(100, 100, 100, 150)
        noStroke()
        ellipse(mouseX, mouseY, 40, 40)
        
    def display_trail(self):
        # Draw the trail as a continuous line
        beginShape()
        stroke(0, 100) # Semi-transparent black
        strokeWeight(2)
        noFill()
        for v in self.history:
            vertex(v[0], v[1])
        endShape()
        
    def run(self):
        # Wrapper method to execute everything
        self.update()
        self.display_trail()
        self.display_mouse()

# Global variable to hold our object
trail = None

def setup():
    global trail
    size(600, 400)
    # Create the trail object with a custom length of 150 points
    trail = MouseTrail(150)
    
def draw():
    background(255)
    trail.run()
```

---

## Breaking Down the Logic

### 1. Managing the History
In the `__init__` method, we define `self.history = []`. This list stores our coordinate pairs. In the `update` method, we use `append()` to add the new position. By using `pop(0)`, we ensure the trail doesn't grow infinitely, which would eventually slow down your computer.

### 2. Drawing with `beginShape()`
Instead of drawing hundreds of separate dots, we use `beginShape()` and `vertex()`. This tells Processing to connect all the points in our list into a single, smooth line. This is much more efficient and looks better than separate shapes.

### 3. Customization
By passing `max_length` to the constructor, you can control how "long" the trail appears. A small number like 10 creates a short, sharp tail, while 500 creates a long, sweeping path that fills the screen.

## Conclusion

Using OOP for visual effects like trails allows you to experiment freely. Try creating two `MouseTrail` objects, or perhaps modify the `display_trail` method to change the color of the line based on how fast the mouse is moving!

Processing.py is a fantastic playground for combining Python logic with visual art, and mastering OOP is the first step toward creating complex, interactive systems.