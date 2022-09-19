title: Mastering Python's Regex - part 1 : Basics
slug: mastering-pythons-regex-part-1-basics
pub: Fri, 03 Aug 2018 20:04:02 +0000

Python regular expressions is often an overlooked topic in the python apprentice path due to it's seemingly mingled nature. If programming was new enough, you don't need those bizarre symbols to complicate your life further. However, if you understand it, you can use it. Regex is easy ... if you get the right tutorial !
What are Regular Expressions in the first place?
================================================


Regular expressions is a language used to define a search pattern. Beyond searching, regular expressions has deep links with Compiler Theory (The study of building programming languages). It is used to define formal languages (computer languages can be described by formal languages, as opposed to natural speech). There are notations to describe formal languages such as BNF (Backus-Naur form), but they can also be described using ... regular expressions. If you did not understand this much, move on, it does not matter, one day it'll click in.
Other names for Regular Expressions
===================================


regex, regexp
The need for functional demos
=============================


Completely theoretical explanations serve it's purpose, but, the delight of the enlightened member is confusion, darkness and apprehension for the novice. Basic workable examples illustrate a basic block. The learner can then assemble his bricks to build walls, houses, towers and forts.
The starting point
==================


The first thing is to import the regex module

```python
import re
```

then we search for a word in a phrase, something so simple that we would not have needed the regex module at all, something that could have been achieved using python's in

```python
lookup1 = re.search('road', 'the path is at the end of the road')
```

if we print it, we'll get <\_sre.SRE\_Match object; span=(30, 34), match='road'>

but if we check it's boolean value

```python
>>> bool(lookup1)
```

we get

```python
True
```

as road is in the sentence as opposed to :

```python
>>> lookup2 = re.search('cat', 'the path is at the end of the road')

>>> bool(lookup2)

False

```

What can we do with this much?
we can check if a word is in a sentence by

```python
if lookup1:

    # do something

else:

    # do something else

```

as a side note, if lookup1 is same as if lookup1 == True
The sequence
============


you'll do three things :
1. declare your string as a raw string literal
2. compile
3. match


What are raw string literals?
=============================


a normal string looks like that

```python
'normal string'
```

but a raw string literal looks like that

```python
r'normal string'
```

prefixing the r allows characters to remain as they are

example:

```python
>>> print('a\nbc')

a

bc
```

where \n was treated as a characted telling to put what come next on a new line but

```python
>>> print( r'a\nbc')

a\nbc
```

the \n was taken litterally as it is

let us see backslashes more carefully

```python
>>> print(r'\')

*error*
```

but

```python
>>> print('\\')

\
```

as expected, trying with

```python
>>> print(r'\\')

\\
```

The use of raw string literals in regular expressions
=====================================================


it simply saves you lots of escaping

see

```python
>>> print(r'\\')

\\
```

and

```python
>>> print('\\\\')

\\
```

would you rather type 2 or 4 slashes? regular expressions juggles with enough symbols for us to overload some \\
Wetting your feet : the three steps and the \* operator
=======================================================



```python
import re

pattern = re.compile(r'aa*') # see our r''

texts = ['aaab', 'baa', 'ab', 'a']

for text in texts:

    match = re.match(pattern, text)

    if match:

        print('passed')

    else:

        print('failed')
```

outputs

```python
passed
failed
passed
passed
```

before we continue, let us list the rules

*Rule 1: characters are interpreted as they are when not near symbols*

that explains why we could match road in our string in the previous example

*Rule 2: \* tells to match 0 or more times*

so aa\* means match a and then see if there is another a zero or more

```python
aaaaa -> a aaaa -> ok

baa -> b aa -> no

aaab -> a aa b -> ok
```

in the next post we'll dive in more
