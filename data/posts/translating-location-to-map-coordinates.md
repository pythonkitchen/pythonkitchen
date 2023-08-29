title: translating location to map coordinates
slug: translating-location-to-map-coordinates
pub: 2018-06-06 06:10:46
authors: arj
tags: 
category: canvas theory,processing.py

let us say you have a character moving across the screen, and you want to have it's location in terms of the map coordinate like (0,0), (3,2) instead of the actual location, like if you want to generate some obstacles in his path, here's how you do it :
demo
----


move the mouse and see the text updates


explanations
------------


 

```python
    fill(255, 0, 0)
    # text <text here> <x> <y>
    text( '{} {}'.format(mouseY//tile_width, mouseX//tile_width),
         20, 20)

```

 

the only required explanation is that we divide the actual location by the tile width, here both x and y size same.

// in python is floor division, it rounds it to the lower nearest whole number

in case you miss map rendering, [here it is](https://www.pythonmembers.club/2018/05/29/game-map-rendering/).
