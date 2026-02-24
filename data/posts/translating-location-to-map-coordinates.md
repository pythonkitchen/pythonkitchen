title: Coordinate Systems: Converting Screen Space to Map Space
slug: translating-location-to-map-coordinates
pub: 2018-06-06 06:10:46
authors: arj
tags: gis, graphics, logic
category: game development
related_posts: game-map-rendering,generating-unintelligent-random-maps,plotting-hotspots-in-mauritius-with-python-and-folium

When building a tile-based game, you constantly need to translate between two different worlds:
1.  **Screen Space:** The actual pixel coordinates on your monitor (e.g., the mouse is at `x: 342, y: 156`).
2.  **Map Space:** The grid coordinates in your data array (e.g., the player is standing on tile `row: 3, col: 6`).

Knowing how to convert between these two is essential for handling clicks, collision detection, and character movement.

---

## The Secret: Floor Division

The math for this conversion is surprisingly simple, thanks to a feature in Python called **Floor Division** (`//`).

Floor division divides two numbers and rounds the result **down** to the nearest whole integer. This is exactly what we need to determine which "box" a specific pixel falls into.

### The Formula
If your tiles are 50 pixels wide:
*   `Map Column = Screen X // 50`
*   `Map Row = Screen Y // 50`

---

## Practical Example in Processing.py

Imagine you want to highlight the tile that the user is currently hovering over with their mouse.

```python
TILE_SIZE = 50

def draw():
    background(255)
    render_map() # Draw your grid
    
    # Calculate map coordinates from mouse position
    map_c = mouseX // TILE_SIZE
    map_r = mouseY // TILE_SIZE
    
    # Display the coordinates on screen
    fill(255, 0, 0)
    text("Tile: Column {}, Row {}".format(map_c, map_r), 20, 20)
    
    # Visual feedback: Highlight the hovered tile
    noFill()
    stroke(255, 0, 0)
    rect(map_c * TILE_SIZE, map_r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
```

---

## Why is this useful?

### 1. Handling Clicks
If a user clicks on the screen, you don't care that they clicked at pixel 143. You care that they clicked on the "Chest" object located at grid position (2, 3). By converting the click coordinates immediately, your logic becomes much simpler.

### 2. Efficient Collision Detection
Instead of checking your player against every single object in the game, you can simply check the tile they are currently "inside." If `game_map[player_row][player_col]` is a "Wall" tile, you stop the player from moving.

### 3. Tooltips and UI
Showing the name of a terrain or an item when the mouse hovers over it requires this constant translation from the cursor's pixel position to the underlying data grid.

## Conclusion

Understanding the relationship between pixels and grid cells is a "lightbulb moment" for many beginning game developers. Once you can move freely between these two coordinate systems, you have the power to create interactive, data-driven game worlds.

### Related Posts:
*   [Tile-Based Game Map Rendering](https://www.pythonkitchen.com/game-map-rendering/)
*   [Procedural Generation Basics](https://www.pythonkitchen.com/generating-unintelligent-random-maps/)