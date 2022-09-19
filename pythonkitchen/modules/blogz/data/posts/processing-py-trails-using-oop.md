title: processing.py : trails using oop
slug: processing-py-trails-using-oop
pub: Thu, 26 Apr 2018 05:13:45 +0000

[caption id="attachment\_77" align="aligncenter" width="300"]![trails in processing.py](https://www.pythonmembers.club/wp-content/uploads/2018/04/trail-300x300.png) trails in processing.py[/caption]

in this post, we'll explain how to add trails using an oop approach.

a trail is basically objects that appear where the primary objects passed

in nature, trails are made by particles of the primary object but in programming, one simple approach is to draw other shapes albeit more small
the full code
=============


there is the full processing.py code :

```python
# github.com/abdur-rahmaanj

```


```python
class MouseTrail:
    def \_\_init\_\_(self):
        self.history = []
        
    def update(self):
        self.history.append([mouseX, mouseY])
        if len(self.history)  > 200:
            self.history.pop(0)
            
    def display_mouse(self):
        fill(100, 100, 100, 100)
        ellipse(mouseX, mouseY, 50, 50)
        
    def display_trail(self):
        beginShape()
        stroke(0)
        strokeWeight(1)
        noFill()
        for v in self.history:
            vertex(v[0], v[1])
        endShape()
        
    def run(self):
        self.update()
        self.display_mouse()
        self.display_trail()

trail = None

def **setup**():
    global trail
    trail = MouseTrail()
    size(500, 500)
    
def **draw**():
    global trail
    background(255)
    trail.run()

```

explanations
============


in the constructor,

```python
        self.history = []
```

is basically a simple list

we added to the list on each call of the update method. then if there are more than 200 elements in the list, we remove one element

```python
        self.history.append([mouseX, mouseY])
        if len(self.history)  > 200:
            self.history.pop(0)

```

for the shapes, we just draw vertices (hey lines) joining all the points in the list

```python
    def display_trail(self):
        beginShape()
        stroke(0)
        strokeWeight(1)
        noFill()
        for v in self.history:
            vertex(v[0], v[1])
        endShape()
```

finally the run method is included for convenience so that we need to only call one method !

```python
    def run(self):
        self.update()
        self.display_mouse()
        self.display_trail()
```

in setup, we just define a new object

```python
    trail = MouseTrail()
```

then in draw we call the run method

```python
    trail.run()

```

conclusion
==========


adding oop allows for much more flexibility than hardcoding it all !

here it is in action :

[video width="500" height="500" mp4="https://www.pythonmembers.club/wp-content/uploads/2018/04/mouse\_trail.mp4"][/video]
