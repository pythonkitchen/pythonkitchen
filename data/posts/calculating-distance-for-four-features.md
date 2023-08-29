title: calculating distance for four features
slug: calculating-distance-for-four-features
pub: 2018-07-22 03:37:21
authors: arj
tags: maths
category: data science,machine learning

if you want to calculate the distance between 4 features coordinates, you do it like that :

A (1,2,5,1)

B (7, 1, 3, 0)

```python
import math

dist = math.sqrt((7-1)**2+(1-2)**2+(3-5)**2+(0-1)**2)

print(dist)

>>> 6.4807 ...


```

