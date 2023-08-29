title: Fixing an issue of tkinter tags overlapping
slug: tkinter-text-widget-tags
pub: 2018-06-19 12:00:31
authors: tim
tags: syntax highlighting,tkinter
category: editors and ides,gui,oop

If you've worked with tkinter's Text widget, you may notice that when you add many tags to it sometimes things get messed. So let's dive right into this. We will use syntax highlighting as an example.
Explaining our goal
-------------------


Consider we have the following code,

```python
from tkinter import *

class Files(Frame):

    def \_\_init\_\_(self, parent):
        Frame.\_\_init\_\_(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

root = Tk()
top = Frame(root)
top.pack(fill=BOTH, expand=0)

bottom = Frame(root)
bottom.pack()

ex = Files(root)
ex.pack(side="bottom")

root.geometry("600x500-600-150")
root.mainloop()

```

which gives us a simple Text widget.

[caption id="attachment\_259" align="alignnone" width="300"]![tkinter window](https://www.pythonmembers.club/wp-content/uploads/2018/06/Screenshot-7-300x266.png) The output of our code[/caption]

Let's say we want to highlight some specific words. And let's do it every time a user enters something.

We will be highlighting word "Hello" with red and "world" with blue. So all we must do is make a function that will run every time a key is pressed and will highlight the words.

```python
[...]
    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        self.bind_all("<Key>", self.highlight) #this runs 'highlight' function every time a key is pressed

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def highlight(self, event=0):

        file_text = self.txt.get("1.0", END+"-1c") + " " #a blank space at the end is for easier separating words
        words = [] #we will store words along with their starting point
        line = 1    #}
        column = -1 #}these are starting points that will help us in the following 'for' loop
        word = ""   #}

#now we have to find words and assign them their line and column
        for char in file_text:
            word += char
            column += 1

            if char == "\n": #here a word stops
                words.append(word[:-1] + " : " + str(line) + "." + str(column))
                word = ""
                line += 1
                column = -1

            if char == " ": #here a word stops
                words.append(word[:-1] + " : " + str(line) + "." + str(column))
                word = ""
        print(words)
[...]

```

This code will produce the following result as we start typing:

[video width="1920" height="1028" webm="https://www.pythonmembers.club/wp-content/uploads/2018/06/highlighting\_video1.webm"][/video]

Now you can see, every time we push a key it gives us the list of all words with it's starting points combined in a format similar to dictionary.

So we have the words, we have the points now we have to use them.
Highlighting words
------------------


For this we will have to see if the word is "Hello" or "world" and add a tag that will highlight it. Now we add this to our "highlight" function:

```python
[...]
        for i in words:
            i = i.split() #this splits an element to i = ["word", ":", "starting point"]

            if len(i) < 3: #we need this in case user types double white space which results in i = [":", "starting point"]
                i.insert(0, " ")

            if i[0] == "Hello": #i[0] stands for "word"
                self.txt.tag_config("hlight1", foreground="red") #we named this tag hlight1
                self.txt.tag_add("hlight1", str(i[2].split(".")[0]) + "." + str(int(i[2].split(".")[1])-len(i[0])), i[2])

            if i[0] == "world":
                self.txt.tag_config("hlight2", foreground="blue") #we named this tag hlight2
                self.txt.tag_add("hlight2", str(i[2].split(".")[0]) + "." + str(int(i[2].split(".")[1])-len(i[0])), i[2])
[...]

```

And if we run it:

[video width="1920" height="1028" webm="https://www.pythonmembers.club/wp-content/uploads/2018/06/highlighting\_video2.webm"][/video]

Looks like we don't have any problems here, right! But we do.
Explaining our issue
--------------------


If you experiment a bit more, you can see that in cases like this, the word "Hello" or any other word gets colored blue:

[video width="1920" height="1028" webm="https://www.pythonmembers.club/wp-content/uploads/2018/06/highlighting\_video3.webm"][/video]

So how to fix this? To know how to fix it, we must first find out why did it happen!

It happens because two tags are overlapping, in our case hlight2 is overlapping hlight1. When the for loop runs the hlight1 tag is already there and hlight2 is over it, giving it the priority. And if we want our code to work, we must remove the tag hlight2 (or hlight1, it works vice versa to) every time it gets over a word that isn't "world". So what we will do is "refresh" the tags every time we run highlight function...
Fixing the issue
----------------


To achieve this, all we have to do is delete all of the tags and then let them be reassigned.

So to delete them we just add this before our 'for' loop in 'highlight' function:

```python
[...]
        for tag in self.txt.tag_names():
            self.txt.tag_delete(tag)

        for i in words:
            i = i.split()......
[...]
```

And that's it! As simple as that! Here's a look into our new **working** output:

[video width="1920" height="1028" webm="https://www.pythonmembers.club/wp-content/uploads/2018/06/highlighting\_video4.webm"][/video]

I hope this article was helpful for you and keep coding!
Complete code
-------------



```python
from tkinter import * 

class Files(Frame):

    def \_\_init\_\_(self, parent):
        Frame.\_\_init\_\_(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        self.bind_all("<Key>", self.highlight)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def highlight(self, event=0):

        file_text = self.txt.get("1.0", END+"-1c") + " " #a blank space at the end is for easier separating words
        words = [] #we will store words along with their starting point
        line = 1    #}
        column = -1 #}these are starting points that will help us in the following 'for' loop
        word = ""   #}

#now we have to find words and assign them their line and column
        for char in file_text:
            word += char
            column += 1

            if char == "\n": #here a word stops
                words.append(word[:-1] + " : " + str(line) + "." + str(column))
                word = ""
                line += 1
                column = -1

            if char == " ": #here a word stops
                words.append(word[:-1] + " : " + str(line) + "." + str(column))
                word = ""
        print(words)

        for tag in self.txt.tag_names(): #deletes all tags so it can refresh them later
            self.txt.tag_delete(tag)

        for i in words:
            i = i.split() #this splits an element to i = ["word", ":", "starting point"]

            if len(i) < 3: #we need this in case user types double white space which results in i = [":", "starting point"]
                i.insert(0, " ")

            if i[0] == "Hello": #i[0] stands for "word"
                self.txt.tag_config("hlight1", foreground="red") #we named this tag hlight1
                self.txt.tag_add("hlight1", str(i[2].split(".")[0]) + "." + str(int(i[2].split(".")[1])-len(i[0])), i[2])

            if i[0] == "world": #i[0] stands for "word"
                self.txt.tag_config("hlight2", foreground="blue") #we named this tag hlight2
                self.txt.tag_add("hlight2", str(i[2].split(".")[0]) + "." + str(int(i[2].split(".")[1])-len(i[0])), i[2])

root = Tk()
top = Frame(root)
top.pack(fill=BOTH, expand=0)

bottom = Frame(root)
bottom.pack()

ex = Files(root)
ex.pack(side="bottom")

root.geometry("600x500-600-150")
root.mainloop()

```

