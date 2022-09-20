title: building an indentation lexer in python - a tutorial
slug: building-an-indentation-analyser-in-python-tutorial
pub: Fri, 04 May 2018 08:31:13 +0000
authors: Abdur-RahmaanJ

scope by indentation is an alternative to curly braces and is used by languages like python and pug. it certainly is more human-friendly as experience gathered tends to produce more and more friendly syntaxes (like livecode). we'll in this post build an indentation analyser that correctly tells us when we mixed indentation level; just like python does. in fact, we'll analyse python code snippets




this article requires [this one](https://www.pythonmembers.club/2018/05/01/building-a-lexer-in-python-tutorial/) on lexer




bonus : exercises included !




analysing indented codes
========================




let us take a python code snippet taken from sqlite3, dbapi2.py, python version 3.4





```python
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()

    def adapt_datetime(val):
        return val.isoformat(" ")

    def convert_date(val):
        return datetime.date(*map(int, val.split(b"-")))
```



the first step when using a lexer is keyword definitions. here, do we take whitespace into consideration or no t? here we must




### whitespace sensitivity




as indentations are based on whitespace or tab in python, we must include them as keywords. in this article, we'll ignore tabs to keep things simple




a basic run of a lexer with keywords :




SINGLE




( ) : . " " \* , <whitespace> <newline>




MULTI




def return




### running the analysis




our code :





```python
string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()

    def adapt_datetime(val):
        return val.isoformat(" ")

    def convert_date(val):
        return datetime.date(*map(int, val.split(b"-")))
'''

# single-char keywords
symbols = ['(', ')', '.', '"', '*', '\n', ':', ',', ' ']
# multi-char keywords
keywords = ['def', 'return']
KEYWORDS = symbols + keywords

white_space = ' '
lexeme = ''

for i,char in enumerate(string):
    #if char != white_space: ## now whitespace treated as a lexeme !
    lexeme += char           # adding a char each time
    if (i+1 < len(string)):  # prevents error
        if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
            if lexeme != '':
                print(lexeme.replace('\n', '**newline**').replace(' ', '**whitespace**'))
                lexeme = ''
```



outputs (we replaced whitespace with <whitespace> and newlines with <newline>) :





```python
**newline**
def
**whitespace**
register_adapters_and_converters
(
)
:
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
def
**whitespace**
adapt_date
(
val
)
:
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
return
**whitespace**
val
.
isoformat
(
)
**newline**
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
def
**whitespace**
adapt_datetime
(
val
)
:
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
return
**whitespace**
val
.
isoformat
(
"
**whitespace**
"
)
**newline**
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
def
**whitespace**
convert_date
(
val
)
:
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
return
**whitespace**
datetime
.
date
(
*
map
(
int
,
**whitespace**
val
.
split
(
b
"
-
"
)
)
)
```



but let us take for a single level :
------------------------------------





```python
**newline**
def
**whitespace**
register_adapters_and_converters
(
)
:
**newline**
**whitespace**
**whitespace**
**whitespace**
**whitespace**
def
```



notice that **after a semicolon there is a newline after that there are 4 whitespaces then a non-whitespace**




<:> <\n> <\s> <\s> <\s> <\s> <def>




the basic rule
==============




so after <:> if there is a newline we'll get an indentation level ending at a non-whitespace char




but there is a problem. suppose we get




<:> **<\s> <\s> <\s>** <\n> <\s> <\s> <\s> <\s> <def>




where a user puts lots of spaces after a semicolon, so, we **must maintain whitespace sensitivity but not treat it as a lexeme**. then we just check if when passing over <\n> if the last lexeme was <:>




we'll have a last lexeme variable. reminder: we'll keep whitespace as keyword as it separates def and  function\_name etc




### defining indentation level




indentation level is just a whitespace counter. we'll have a whitespace counter and indentation level variable




getting indentation level
=========================




pseudocode :





```python
if char \n and last_lexeme was <:> then
    indent_on = True
if indent_on True and char white_space then
    indent_space_count += 1
if indent_on and next_char != white_space then
    indent_on = False
    indent_level = indent_space_count
    space_count = 0
﻿
```



explanations
------------




with **indent\_on** we check if we should count whitespace for indentation level or not




**our code :**





```python
string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()

    def adapt_datetime(val):
        return val.isoformat(" ")
'''

# single-char keywords
symbols = ['(', ')', '.', '"', '*', '\n', ':', ',', ' ']
# multi-char keywords
keywords = ['def', 'return']
KEYWORDS = symbols + keywords

white_space = ' '
lexeme = ''
last_lexeme = ''

indent_on = False
indent_space_count = 0
indent_level = 0

for i,char in enumerate(string):
    if char != white_space: # just not good for strings between '' but not needed now !
        lexeme += char      # adding a char each time
        
    if (i+1 < len(string)): # prevents error
        next_char = string[i+1]      # added for readability
        
        if char == '\n' and last_lexeme == ':':
            indent_on = True
        if indent_on and char == white_space:
            indent_space_count += 1
        if indent_on and next_char != white_space:
            indent_on = False
            indent_level = indent_space_count
            indent_space_count = 0
            
        if next_char == white_space or next_char in KEYWORDS or lexeme in KEYWORDS:
            if lexeme != '':
                print( '{} level {}'.format(' '*10, indent_level) )
                print(lexeme.replace('\n', '**newline**'))
                last_lexeme = lexeme # before clearing
                lexeme = ''
```



**output:**





```python
           level 0
**newline**
           level 0
def
           level 0
register_adapters_and_converters
           level 0
(
           level 0
)
           level 0
:
           level 0
**newline**
           level 4
def
           level 4
adapt_date
           level 4
(
           level 4
val
           level 4
)
           level 4
:
           level 4
**newline**
           level 8
return
           level 8
val
           level 8
.
           level 8
isoformat
           level 8
(
           level 8
)
           level 8
**newline**
           level 8
**newline**
           level 8
def
           level 8
adapt_datetime
           level 8
(
           level 8
val
           level 8
)
           level 8
:
           level 8
**newline**
           level 8
return
           level 8
val
           level 8
.
           level 8
isoformat
           level 8
(
           level 8
"
           level 8
"
           level 8
)
```



see the numbers represent our indentation level but there is a glitch: our indent level once detected, should remain constant as compared to this that we can say that subsequent indents don't match! we'll do that by having a first pass flag





```python
if char \n and last_lexeme == <:> then
    indent_on = True
if indent_on True and char white_space then
    indent_space_count += 1
if char whitespace and indent_on and next_char != white_space then
    indent_on = False
    if first_pass == True then
        indent_level = indent_space_count
        first_pass = False # only once
﻿
```



### resetting count and a general case




not only after <:> <\n> do we get indentations but also after <\n> and next char white space




if char \n and next\_char == whitespace then




we start checking for indentations and reset counts




code :





```python
string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()

    def adapt_datetime(val):
        return val.isoformat(" ")
'''

# single-char keywords
symbols = ['(', ')', '.', '"', '*', '\n', ':', ',', ' ']
# multi-char keywords
keywords = ['def', 'return']
KEYWORDS = symbols + keywords

white_space = ' '
lexeme = ''
last_lexeme = ''

indent_on = False
indent_space_count = 0
indent_level = 0
first_pass_on = True

for i,char in enumerate(string):
    if char != white_space: # just not good for strings between '' but not needed now !
        lexeme += char      # adding a char each time
        
    if (i+1 < len(string)): # prevents error
        next_char = string[i+1]      # added for readability
            
        if indent_on and char == white_space:
            indent_space_count += 1
            
        if char == white_space and indent_on and next_char != white_space:
            indent_on = False
            if first_pass_on == True:
                indent_level = indent_space_count
                first_pass_on = False
                
        if char == '\n' and next_char == ' ':
            indent_space_count = 0
            indent_on = True
        
        if next_char == white_space or next_char in KEYWORDS or lexeme in KEYWORDS:
            if lexeme != '':
                print(lexeme.replace('\n', '**newline**'))
                last_lexeme = lexeme # before clearing
                lexeme = ''
                print( '{} level: {} | count: {} | indent_on: {} | first_pass: {}'.format(
                ' '*10, indent_level, indent_space_count, indent_on, first_pass_on) )
```



output:





```python
**newline**
           level: 0 | count: 0 | indent_on: False | first_pass: True
def
           level: 0 | count: 0 | indent_on: False | first_pass: True
register_adapters_and_converters
           level: 0 | count: 0 | indent_on: False | first_pass: True
(
           level: 0 | count: 0 | indent_on: False | first_pass: True
)
           level: 0 | count: 0 | indent_on: False | first_pass: True
:
           level: 0 | count: 0 | indent_on: False | first_pass: True
**newline**
           level: 0 | count: 0 | indent_on: True | first_pass: True
def
           level: 4 | count: 4 | indent_on: False | first_pass: False
adapt_date
           level: 4 | count: 4 | indent_on: False | first_pass: False
(
           level: 4 | count: 4 | indent_on: False | first_pass: False
val
           level: 4 | count: 4 | indent_on: False | first_pass: False
)
           level: 4 | count: 4 | indent_on: False | first_pass: False
:
           level: 4 | count: 4 | indent_on: False | first_pass: False
**newline**
           level: 4 | count: 0 | indent_on: True | first_pass: False
return
           level: 4 | count: 8 | indent_on: False | first_pass: False
val
           level: 4 | count: 8 | indent_on: False | first_pass: False
.
           level: 4 | count: 8 | indent_on: False | first_pass: False
isoformat
           level: 4 | count: 8 | indent_on: False | first_pass: False
(
           level: 4 | count: 8 | indent_on: False | first_pass: False
)
           level: 4 | count: 8 | indent_on: False | first_pass: False
**newline**
           level: 4 | count: 8 | indent_on: False | first_pass: False
**newline**
           level: 4 | count: 0 | indent_on: True | first_pass: False
def
           level: 4 | count: 4 | indent_on: False | first_pass: False
adapt_datetime
           level: 4 | count: 4 | indent_on: False | first_pass: False
(
           level: 4 | count: 4 | indent_on: False | first_pass: False
val
           level: 4 | count: 4 | indent_on: False | first_pass: False
)
           level: 4 | count: 4 | indent_on: False | first_pass: False
:
           level: 4 | count: 4 | indent_on: False | first_pass: False
**newline**
           level: 4 | count: 0 | indent_on: True | first_pass: False
return
           level: 4 | count: 8 | indent_on: False | first_pass: False
val
           level: 4 | count: 8 | indent_on: False | first_pass: False
.
           level: 4 | count: 8 | indent_on: False | first_pass: False
isoformat
           level: 4 | count: 8 | indent_on: False | first_pass: False
(
           level: 4 | count: 8 | indent_on: False | first_pass: False
"
           level: 4 | count: 8 | indent_on: False | first_pass: False
"
           level: 4 | count: 8 | indent_on: False | first_pass: False
)
           level: 4 | count: 8 | indent_on: False | first_pass: False

```



see how the count goes from 4 to 8 then back




some tests
----------




testing





```python
string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()
            def adapt_datetime(val):
                return val.isoformat(" ")
    def 
'''
```



gives out (lexemes omitted)





```python
           level: 0 | count: 0 | indent_on: False | first_pass: True
           level: 0 | count: 0 | indent_on: False | first_pass: True
           level: 0 | count: 0 | indent_on: False | first_pass: True
           level: 0 | count: 0 | indent_on: False | first_pass: True
           level: 0 | count: 0 | indent_on: False | first_pass: True
           level: 0 | count: 0 | indent_on: False | first_pass: True
           level: 0 | count: 0 | indent_on: True | first_pass: True
           level: 4 | count: 4 | indent_on: False | first_pass: False
           level: 4 | count: 4 | indent_on: False | first_pass: False
           level: 4 | count: 4 | indent_on: False | first_pass: False
           level: 4 | count: 4 | indent_on: False | first_pass: False
           level: 4 | count: 4 | indent_on: False | first_pass: False
           level: 4 | count: 4 | indent_on: False | first_pass: False
           level: 4 | count: 0 | indent_on: True | first_pass: False
           level: 4 | count: 8 | indent_on: False | first_pass: False
           level: 4 | count: 8 | indent_on: False | first_pass: False
           level: 4 | count: 8 | indent_on: False | first_pass: False
           level: 4 | count: 8 | indent_on: False | first_pass: False
           level: 4 | count: 8 | indent_on: False | first_pass: False
           level: 4 | count: 8 | indent_on: False | first_pass: False
           level: 4 | count: 0 | indent_on: True | first_pass: False
           level: 4 | count: 12 | indent_on: False | first_pass: False
           level: 4 | count: 12 | indent_on: False | first_pass: False
           level: 4 | count: 12 | indent_on: False | first_pass: False
           level: 4 | count: 12 | indent_on: False | first_pass: False
           level: 4 | count: 12 | indent_on: False | first_pass: False
           level: 4 | count: 12 | indent_on: False | first_pass: False
           level: 4 | count: 0 | indent_on: True | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 16 | indent_on: False | first_pass: False
           level: 4 | count: 0 | indent_on: True | first_pass: False
           level: 4 | count: 4 | indent_on: False | first_pass: False
```



meaning it successfully detected our indentation level changes




detecting mixed indentation levels
==================================




correct indentation level check is





> indent\_count % indent\_level == 0
> 
> 




in other words, if at reaching the end of an indent, the whitespace count is exactly divisible by the level first detected, our check passes




implementation
--------------





```python
if char == white_space and indent_on and next_char != white_space:
    indent_on = False
    if first_pass_on == True:
        indent_level = indent_space_count
        first_pass_on = False
    # prevents div by zero error on indent_level
    if indent_level != 0: 
        if indent_space_count%indent_level == 0:
            print('good indentation level detected')
        else:
            print('bad indentation')
```



if we try to run it on this piece of text :





```python
string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()
 def adapt_datetime(val):
     return val.isoformat(" ")
'''
```



on the bad levels it outputs :





```python
           level: 4 | count: 0 | indent_on: True | first_pass: False
bad indentation
           level: 4 | count: 1 | indent_on: False | first_pass: False
           level: 4 | count: 1 | indent_on: False | first_pass: False
           level: 4 | count: 1 | indent_on: False | first_pass: False
           level: 4 | count: 1 | indent_on: False | first_pass: False
           level: 4 | count: 1 | indent_on: False | first_pass: False
           level: 4 | count: 1 | indent_on: False | first_pass: False
           level: 4 | count: 0 | indent_on: True | first_pass: False
bad indentation
           level: 4 | count: 5 | indent_on: False | first_pass: False
```



knowing on which line error occurred
====================================




on error occurred, we'll break and give a message to the user :





```python
mixed indentation detected on line X
```



for that we'll implement a line counter :





```python
if char == \n
    line_count += 1
```



### complete code :





```python
string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()
 def adapt_datetime(val):
     return val.isoformat(" ")
'''

# single-char keywords
symbols = ['(', ')', '.', '"', '*', '\n', ':', ',', ' ']
# multi-char keywords
keywords = ['def', 'return']
KEYWORDS = symbols + keywords

white_space = ' '
lexeme = ''
last_lexeme = ''

indent_on = False
indent_space_count = 0
indent_level = 0
first_pass_on = True

line_count = 1 # as we start counting from one

for i,char in enumerate(string):
    if char == '\n':
        line_count += 1
        
    if char != white_space: 
        lexeme += char      # adding a char each time
        
    if (i+1 < len(string)): # prevents error
        next_char = string[i+1]      # added for readability
            
        if indent_on and char == white_space:
            indent_space_count += 1
            
        if char == white_space and indent_on and next_char != white_space:
            indent_on = False
            if first_pass_on == True:
                indent_level = indent_space_count
                first_pass_on = False
            # prevents div by zero error on indent_level
            if indent_level != 0: 
                if indent_space_count%indent_level == 0:
                    print('good indentation level detected')
                else:
                    print('bad indentation on line {}'.format(line_count))
                    break
                
        if char == '\n' and next_char == ' ':
            indent_space_count = 0
            indent_on = True
        
        if next_char == white_space or next_char in KEYWORDS or lexeme in KEYWORDS:
            if lexeme != '':
                # print(lexeme.replace('\n', '**newline**'))
                last_lexeme = lexeme # before clearing
                lexeme = ''
                print( '{} level: {} | count: {} | indent_on: {} | first_pass: {}'.format(
                ' '*10, indent_level, indent_space_count, indent_on, first_pass_on) )
```



how to detect mixed indentations and tabs?
==========================================




we'll have an indentation character variable detected on first pass. then when checking for indentation (when indent\_on is true) if the char is not equal to that variable we raise an error




---




hope you enjoyed the article! the debug print logs were voluntarily added.




Exercises
=========




1] implement the above using classes (implement a lexer class)




2] implement tabs and whitespace detection




3] how would you know when a function starts and end? implement it!



