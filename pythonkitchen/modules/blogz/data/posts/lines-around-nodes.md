title: polygon drawer implementation (processing.py)
slug: lines-around-nodes
pub: Mon, 28 May 2018 18:26:55 +0000
authors: Abdur-RahmaanJ

if ever you wanted to implement a polygon drawer, here it is :


explanations
------------


 

```python
nodes = [
    [50,40],
    [40,50]
  ]

```

 

first we added some coordinates as 2d arrays

 

```python
for i,node in enumerate(nodes):
    try:
        line(nodes[i][0], nodes[i][1], nodes[i+1][0], nodes[i+1][1])
    except:
        pass

```

 

then for each coordinate we drew a line from it to the next, the try pass is a bad and lazy practise to prevent out of index error. the proper way is to add an if

 

```python
        line(nodes[0][0], nodes[0][1], nodes[len(nodes)-1][0], nodes[len(nodes)-1][1])

```

 

then after the try catch we drew a line from the first coordinate to the last coordinate

 

```python
def mousePressed():
    nodes.append([mouseX, mouseY])

```

 

then upon mouse press, we added a new coord to the array
