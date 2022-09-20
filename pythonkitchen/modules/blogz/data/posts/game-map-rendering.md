title: game map rendering
slug: game-map-rendering
pub: Tue, 29 May 2018 05:20:26 +0000
authors: Abdur-RahmaanJ


game map rendering or simply map rendering is a nice technique that is used to generate worlds.

explanations follow suit :
demo
----


explanations
------------


 

```python
game_map = [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    ]

```

 

first we initialise our world as a 2d array, we distinguished patterns by using 0 and 1

 

```python
tile_width = 50

```

 

next we initialised the width of a tile. the formula for tile placement is x\*tile\_width

 

```python
def green_tile(x, y):
    fill(0,255,0)
    rect(x, y, tile_width, tile_width)
    
def white_tile(x, y):
    fill(255)
    rect(x, y, tile_width, tile_width)

```

 

next we separated our tile rendering in two functions, for now it's just colored squares

 

```python
    for r in range(map_length):
        for c in range(map_length):

```

 

we loop or the array twice, one for the row and one for the column to get the index to accesss our map by game\_map[x][y]

 

```python
            if game_map[c][r] == 0: # inversed for viewing as is in variable
                green_tile(r*tile_width, c*tile_width)
            elif game_map[c][r] == 1:
                white_tile(r*tile_width, c*tile_width)

```

here we render according to predefined symbols, it could have been 'g' and 'p' for grass and path
