title: Procedural Generation Basics: Random Map Generation in Python
slug: generating-unintelligent-random-maps
pub: 2018-06-01 05:32:02
authors: arj
tags: procedural generation, maps, logic
category: game development
related_posts: game-map-rendering,translating-location-to-map-coordinates,plotting-hotspots-in-mauritius-with-python-and-folium

In game development, **Procedural Generation** is the technique of using algorithms to create game content automatically rather than manually. While complex games like *Minecraft* or *No Man's Sky* use sophisticated noise functions, we can start by learning the most basic form: **Random Value Filling**.

This tutorial builds upon our [Tile-Based Map Rendering](https://www.pythonkitchen.com/game-map-rendering/) guide.

---

## The "Unintelligent" Approach

The simplest way to generate a map is to iterate through every cell in your 2D grid and assign it a random tile type. 

We call this "unintelligent" because there is no logic to ensure that the tiles make sense together. For example, you might get a single water tile surrounded entirely by land, or a very "noisy" looking map that doesn't resemble real geography.

### Python Implementation

Using the `random` module, we can quickly fill our `game_map` with new data:

```python
import random

MAP_SIZE = 10
game_map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

def generate_random_map():
    for r in range(MAP_SIZE):
        for c in range(MAP_SIZE):
            # Assign 0 (Grass) or 1 (Water) randomly
            game_map[r][c] = random.randint(0, 1)

def mousePressed():
    # Generate a new map every time the user clicks
    generate_random_map()
    redraw()
```

---

## Improving the Randomness: Probability

Purely random (50/50) maps often look chaotic. We can improve this by introducing **weighted probabilities**. If we want a world that is mostly grass with only a few lakes, we can adjust our logic:

```python
def generate_weighted_map():
    for r in range(MAP_SIZE):
        for c in range(MAP_SIZE):
            # Generate a number between 0 and 100
            chance = random.random() * 100
            
            if chance < 80:
                game_map[r][c] = 0 # 80% chance for Grass
            else:
                game_map[r][c] = 1 # 20% chance for Water
```

---

## Random vs. Noise-Based Generation

While simple randomness is great for learning, professional games usually use **Perlin Noise** or **Simplex Noise**. 

*   **Random:** Every cell is independent. Result: "Static" or noisy look.
*   **Noise:** Each cell is related to its neighbors. Result: Smooth, natural-looking transitions (hills, valleys, and coastlines).

### Next Steps
Try modifying the `generate_random_map` function to include a third tile type, like "Mountain" or "Desert," and experiment with different probability weights to see how it changes the "feel" of your generated world.

Procedural generation is a deep and fascinating topic. Starting with simple random grids is the first step toward building infinite, ever-changing game universes!

### Related Posts:
*   [Tile-Based Game Map Rendering](https://www.pythonkitchen.com/game-map-rendering/)
*   [Converting Screen Space to Map Space](https://www.pythonkitchen.com/translating-location-to-map-coordinates/)