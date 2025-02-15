title: Simple JSON parser without knowing anything beforehands
slug: simple-json-parser
pub: 2025-02-15 15:40:00
authors: arj
tags: 
category: programming problems

Table of Content
================

1. Introduction
2. Scanning the text
3. Looking for specific characters
4. Identifying elements
5. Processing elements

## Introduction

Our goal in this post is to be able to transform this piece of json into a Python dictionary.
```
{"x":"y"}
```

Our Python dictionary should have key `x` and value `y`.

We aim to cover this without any previous compiler theory experience.

This was inspired by the Python Mauritius Usergroup's January challenge.

## Scanning the text

Our first task is to be able to go over the characters and print them.


```python
text = '''
{"x": "y", "z":"a"}
'''


def scan_text(text):
    go = True
    current = 0
    
    while go:
        char = text[current]
        print(current, char.replace('\n', '<new line>'))

        if char == '}':

            go = False

        current += 1


print(scan_text(text))
```


```
0 <new line> 
1 { 
2 " 
3 x 
4 " 
5 : 
6 
7 "
8 y 
...
```

## Looking for specific characters

Next, we want to be able to find the next occurance of a character, give us it's index. We provide it from what index we want to search.

```
abcdefghijih

ex. find(2, 'i') should return 8
```

```python
def look_for(from_i, char):
    go = True
    current = from_i+1
    while go:
        
        if text[current] == char:
            return current


        current += 1
        
text = 'abcdefghijih'
print(look_for(2, 'i')) # 8
```

We can also modify it to return the text between 2 and the index it found the first `i`.

```python
def look_for(from_i, char):
    chunks = []
    go = True
    current = from_i+1
    while go:
        
        if text[current] == char:
            return current, ''.join(chunks)
        else:
            chunks.append(text[current])


        current += 1

print(look_for(2, 'i')) # (8, 'defgh')
```

This will be useful when identifying strings. When we encounter a string. We find where it ends and identifies the string.

## Identifying elements

We modify the scan function to return identified text. 

Our goal is to convert 

```
text = '''
{"x": "y", "z":"a"}
'''
```

into `['{', 'x', ':', 'y', ',', 'z', ':', 'a', '}']`


We just add a list to hold the text named `chunks`.

```python
def scan_text(text):
    chunks = [] # added
    go = True
    current = 0
    
    while go:
        char = text[current]
        print(current, char)
        
        
        if char == '{': 
            chunks.append('{') # added
            
        elif char == '}':
            chunks.append('}') # added
            go = False
            
            
        elif char == '"':
            # TODO
     
        elif char == ":":
            chunks.append(':') # added
            
        if char == ',':
            chunks.append(',') # added
        
        current += 1
    return chunks 
```

For the `"` We just identify the next `"` and append the chars in  between to chunks.

```python
        elif char == '"':
            look  = look_for(current,  '"') # look from the current index till the next "
            string = look[1]
            index = look[0]
        
            chunks.append(string) # append identified string
            current = index # Start loop from next character. current is increased further down.
```


Our final function looks like this 


```python
def scan_text(text):
    chunks = []
    go = True
    current = 0
    
    while go:
        char = text[current]
        print(current, char)
        
        
        if char == '{':
            chunks.append('{')
            
        elif char == '}':
            chunks.append('}')
            go = False
            
            
        elif char == '"':
            look  = look_for(current,  '"')
            string = look[1]
            index = look[0]
        
            chunks.append(string)
            current = index
        elif char == ":":
            chunks.append(char)
            
        if char == ',':
            chunks.append(',')
        
        current += 1
    return chunks    
```

## Processing elements

Now that we have a list of items, we go over the list. The simple thing would be to find `:` and add the element before it as the key and the element after it as the value

```python
def process(chunks):
    go = True
    current = 0
    
    kv = {}
    while go:
        char = chunks[current]
        
        if char == ':':
            kv[chunks[current-1]] = chunks[current+1]
            current += 1 
            continue
        elif char == '}':
            go = False
        current += 1 
        
    return kv 
```
 Our final code 

```python
text = '''
{"x": "y", "z":"a"}
'''

def look_for(from_i, char):
    go = True
    current = from_i+1
    text_found = []
    while go:
        
        if text[current] == char:
            return current, ''.join(text_found)
        else:
            text_found.append(text[current])
        
        current += 1
        print(current)


def scan_text(text):
    chunks = []
    go = True
    current = 0
    
    while go:
        char = text[current]
        print(current, char)
        
        
        if char == '{':
            chunks.append('{')
            
        elif char == '}':
            chunks.append('}')
            go = False
            
            
        elif char == '"':
            look  = look_for(current,  '"')
            string = look[1]
            index = look[0]
        
            chunks.append(string)
            current = index
        elif char == ":":
            chunks.append(char)
            
        if char == ',':
            chunks.append(',')
        
        current += 1
    return chunks    
        
def process(chunks):
    go = True
    current = 0
    
    kv = {}
    while go:
        char = chunks[current]
        
        if char == ':':
            kv[chunks[current-1]] = chunks[current+1]
            current += 1 
            continue
        elif char == '}':
            go = False
        current += 1 
        
    return kv 

elements = scan_text(text)
print(elements)
kv = process(elements)
print(kv)
```

It goes from this

```
{"x": "y", "z":"a"}
```

to this

```
['{', 'x', ':', 'y', ',', 'z', ':', 'a', '}']
```

then to this

```
{'x': 'y', 'z': 'a'}
```

Hope you enjoyed it!