title: Oreiller: A Python Pillow Alternative
slug: oreiller-pillow-alternative 
pub: 2024-03-06 09:00:00
authors: arj 
tags: category: pillow

Really, oreiller is the french word for a pillow.

I always heard about the PIL fork, Pillow but never used it. When I finally used it, I found it to be tedious sometimes. Like including emojis in text and the general programming. I finally got around to create a small library WIP called oreiller.

[https://pypi.org/project/oreiller/](https://pypi.org/project/oreiller/)


Code demo:

```py
from oreiller import Oreiller as orey

w, h = 220, 190

img = orey.new("RGB", (w, h)) 
orey.fill(None)
orey.oline(40, 40, w-10, h-10, width=0) # use .line for normal
orey.otext(40, 60, "👋 Good to see ya")
img.show() 

orey.cleanup()
```
