title: generating unintelligent random maps on mouse press
slug: generating-unintelligent-random-maps
pub: 2018-06-01 05:32:02
authors: arj
tags: 
category: canvas theory,processing.py

this code generates random maps on mouse press. it is really just a simple 2d array value filling. a modification of [this article](https://www.pythonmembers.club/2018/05/29/game-map-rendering/).
demo
----


explanations
------------


 

```python
def random_map():
    for r in range(map_length):
        for c in range(map_length):
            game_map[c][r] = random.randint(0,1)

```

 

here we generated a random map by looping and assigning a random value. randint returns a value betwen 1 and 0. the advantage of a function is that we just need to call it each time a random map is needed

 

```python
def mousePressed():
    random_map()

```

 

each time the mouse is pressed, random\_map() is called
