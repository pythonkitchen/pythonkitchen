title: Building a Dynamic Polygon Drawer in Processing.py
slug: lines-around-nodes
pub: 2018-05-28 18:26:55
authors: arj
tags: python, processing.py, creative-coding, geometry, algorithms
category: canvas theory, processing.py

Have you ever wondered how vector drawing tools allow you to click and create complex shapes? In this tutorial, we will build a simple **Polygon Drawer** using Processing.py. This project is a great way to understand how to manage dynamic lists of coordinates and draw connected paths.

## The Goal
We want an application where every time the user clicks, a new "node" (point) is created, and a line is automatically drawn to connect it to the previous point. To complete the shape, a line will also connect the last point back to the first one.

---

## Core Logic: Storing Coordinates

We need a way to remember every point the user has clicked. A simple 2D list (a list of lists) is perfect for this:

```python
nodes = []

def mousePressed():
    # Every click adds a new [x, y] pair to our list
    nodes.append([mouseX, mouseY])
```

---

## Drawing the Connections

To draw the polygon, we iterate through our list of nodes. For every node at index `i`, we draw a line to the node at index `i+1`.

### The "Off-by-One" Challenge
A common mistake is trying to draw a line from the last element to `i+1`, which doesn't exist. We must handle this carefully.

```python
def draw_polygon():
    # We need at least 2 points to draw a line
    if len(nodes) < 2:
        return
        
    for i in range(len(nodes) - 1):
        # Draw line from current node to next node
        line(nodes[i][0], nodes[i][1], nodes[i+1][0], nodes[i+1][1])
        
    # Closing the loop: Connect last node to the first node
    last = len(nodes) - 1
    line(nodes[last][0], nodes[last][1], nodes[0][0], nodes[0][1])
```

---

## The Full Code

Here is the complete Processing.py script:

```python
nodes = []

def setup():
    size(600, 400)
    stroke(0)
    strokeWeight(2)

def draw():
    background(255)
    
    # Draw instructions
    fill(150)
    text("Click to add nodes and create a polygon", 20, 30)
    
    # Draw lines between nodes
    if len(nodes) >= 2:
        for i in range(len(nodes) - 1):
            line(nodes[i][0], nodes[i][1], nodes[i+1][0], nodes[i+1][1])
        
        # Close the loop
        line(nodes[-1][0], nodes[-1][1], nodes[0][0], nodes[0][1])
        
    # Draw the nodes themselves as small circles
    for node in nodes:
        fill(255, 0, 0)
        ellipse(node[0], node[1], 8, 8)

def mousePressed():
    nodes.append([mouseX, mouseY])

def keyPressed():
    # Press 'c' to clear the canvas
    if key == 'c':
        global nodes
        nodes = []
```

## Why this matters

This simple algorithm is the foundation for:
1.  **Pathfinding Visualizers:** Showing a path between nodes.
2.  **Vector Graphics:** How SVG paths are stored and rendered.
3.  **Collision Detection:** Determining if a point is inside a custom-shaped area.

## Conclusion

Managing a dynamic list of points is a fundamental skill in creative coding. From here, you could try adding the ability to drag existing nodes or calculate the area of the polygon you've created!