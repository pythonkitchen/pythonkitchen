title: Tile-Based Game Map Rendering with Processing.py
slug: game-map-rendering
pub: 2018-05-29 05:20:26
authors: arj
tags: graphics, rendering, level design
category: game development
related_posts: generating-unintelligent-random-maps,translating-location-to-map-coordinates,display-most-frequent-words-python-pygame

Whether you're building a classic RPG or a puzzle game, **tile-based rendering** is one of the most efficient ways to create large, structured game worlds. Instead of drawing every pixel manually, we divide the world into a grid of "tiles."

In this tutorial, we'll learn how to translate a 2D Python list into a visual game map using Processing.py.

---

## The Concept: The Data Map

At its heart, a game level is just data. We can represent a grid of tiles using a 2D list (a list of lists). In this example:
*   `0` represents Grass (Green)
*   `1` represents Water (Blue)

```python
# Our 5x5 game map
game_map = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
```

---

## Rendering the Grid

To turn this data into a visual map, we need to loop through the rows and columns. The position of each tile on the screen is calculated by multiplying its grid index by the **tile size**.

### The Math
If a tile is at row `r` and column `c`, and our tiles are 50 pixels wide:
*   `x = c * 50`
*   `y = r * 50`

### The Python Implementation

```python
TILE_SIZE = 50

def setup():
    size(250, 250)
    noLoop() # We only need to draw the map once

def draw():
    background(255)
    
    # Iterate through rows
    for r in range(len(game_map)):
        # Iterate through columns in each row
        for c in range(len(game_map[r])):
            
            tile_type = game_map[r][c]
            
            # Determine color based on tile type
            if tile_type == 0:
                fill(34, 139, 34) # Forest Green
            elif tile_type == 1:
                fill(30, 144, 255) # Dodger Blue
            
            # Draw the tile
            # Notice x is column (c) and y is row (r)
            rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
```

---

## Why use Tile Maps?

1.  **Memory Efficiency:** You only need to store a few integers per tile, rather than high-resolution images of the entire world.
2.  **Easy Collision Detection:** If you know your character is at pixel (120, 85), you can easily calculate exactly which tile they are standing on by dividing by `TILE_SIZE`.
3.  **Level Editors:** It's very easy to create a tool that allows you to "paint" levels by changing numbers in a grid.

## Going Further

Once you have the basic grid working, you can replace the simple `rect()` calls with `image()` calls to use actual sprites for your grass and water. 

In our next post, we'll look at how to **generate these maps randomly** so you never play the same level twice!

### Related Posts:
*   [Generating Random Maps on the Fly](https://www.pythonkitchen.com/generating-unintelligent-random-maps/)
*   [Converting Screen Coordinates to Map Coordinates](https://www.pythonkitchen.com/translating-location-to-map-coordinates/)