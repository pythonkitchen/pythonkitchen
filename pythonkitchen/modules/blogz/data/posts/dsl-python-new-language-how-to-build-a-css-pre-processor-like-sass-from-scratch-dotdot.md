title: DSL / Python / New Language: How to build a CSS pre-processor (like SASS) from scratch (DotDot)
slug: dsl-python-new-language-how-to-build-a-css-pre-processor-like-sass-from-scratch-dotdot
pub: Thu, 18 Jul 2019 15:02:53 +0000


If you are in web development, maybe you've heard of [Sass](https://sass-lang.com/documentation/syntax/comments), [Less](http://lesscss.org), Pug, [Stylus](http://stylus-lang.com) etc. All these are pre-processors. In this tutorial we're going to build nothing less than a functional css pre-processor from scratch with variables and functions. This type of new language is called source-to-source compiled. If you are thrilled, i hope not to disappoint you.




![Mesh drilling](https://images.unsplash.com/photo-1516562309708-05f3b2b2c238?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80)


### Charting The Routes




First let's see what we'll be doing. We'll call the language DotDot with extention .dot




When designing a new language, it's good to spend sometimes on design. If you have something that really flows, you can start coding.




Here is a DotDot snippet:





```python

x = 1
y = 5
x-y-z = 6
col-z = berry

@f{
    border: 10px solid black;
    border-radius: 50%;
}

.add{
    color:white;
    background-color: rgb(3, 4, 5);
}

#ad{
    color: rgb(x, 4, 5);
}

.a div a{
    color: ..col-z;
    @f
}

```



which compiles to this:





```python

.add{
    color: white;
    background-color: rgb(3,4,5);
}

#ad{
    color: rgb(1,4,5);
}

.a div a{
    color: berry;
    border: 10px solid black;
    border-radius: 50%;
}

```



### Dissecting Design




Let's see what features we included




#### **Variables**





```python

x = 1
y = 5
x-y-z = 6
col-z = berry

```



We see that 




* we don't need to specify a specifier like $ or var in Js.
* we can add - in the variable name




We can call variables in function values





```python

rgb(x, 4, 5);

```



And in attribute values





```python

color: ..col-z;

```



Where .. denotes a variable call in attribute directly.




#### **Functions**





```python

@f{
    border: 10px solid black;
    border-radius: 50%;
}

```



Functions are denoted by an @ sign. These are called as in the following case where it expands into the properties it contains





```python

.a div a{
    color: ..col-z;
    @f
}

```



That is enough complexity to deal with. Let's start!





```python
import copy # we have just one import
```



We also add our source as a variable





```python
source = '''

x = 1
y = 5
x-y-z = 6
col-z = berry

@f{
    border: 10px solid black;
    border-radius: 50%;
}

.add{
    color:white;
    background-color: rgb(3, 4, 5);
}

#ad{
    color: rgb(x, 4, 5);
}

.a div a{
    color: ..col-z;
    @f
}
'''
```



### Defining Constants




We've bundled our constants in a class.





```python

class SYM:
    LEFT_BRACE = '{'
    RIGHT_BRACE = '}'
    LEFT_ROUND = '('
    RIGHT_ROUND = ')'
    NEW_LINE = '\n'
    TAB = '    '
    COLON = ':'
    SEMI_COLON = ';'
    SPACE = ' '
    COMMA = ','
    EQUAL = '='
    UNION = '-'
    DOT = '.'
    AT = '@'

```



We then define our keywords





```python

KEYWORDS = (SYM.LEFT_BRACE, SYM.RIGHT_BRACE, SYM.NEW_LINE, SYM.TAB, SYM.COLON, 
    SYM.SEMI_COLON, SYM.SPACE, SYM.RIGHT_ROUND, SYM.LEFT_ROUND, SYM.COMMA, SYM.EQUAL)

```



### Building the Lexer




The code for the lexer is from our [lexer tutorial](https://www.pythonmembers.club/2018/05/01/building-a-lexer-in-python-tutorial/). Please go over it if you feel the need to. Here we converted the code into a class with a get\_lexeme method. The metho gives us a list. The dotdot snippet above gets converted to the list held in lexemes variable below.




Here is our lexer class:





```python

class Lexer:
    def __init__(self, source: str, KEYWORDS: list):
        self.white_space = SYM.SPACE
        self.KEYWORDS = KEYWORDS
        self.lexeme = ''
        self.lexemes = []
        self.string = source

    def get_lexemes(self) -> list:
        for i, char in enumerate(self.string):
            if char != self.white_space and char != SYM.NEW_LINE:
                self.lexeme += char  # adding a char each time
            if (i+1 < len(self.string)):  # prevents error
                if self.string[i+1] == self.white_space or self.string[i+1] in KEYWORDS or self.lexeme in KEYWORDS or self.string[i+1] == SYM.NEW_LINE: # if next char == ' '
                    if self.lexeme != '':
                        self.lexemes.append(self.lexeme)
                        self.lexeme = ''
        return self.lexemes

```



Then we declare our basic variables:





```python

v = Lexer(source, KEYWORDS)
lexemes = v.get_lexemes()

lexemes.append('') # appending an unused last element to properly dump all values

```



lexemes is now equal to





```python

['x', '=', '1', 'y', '=', '5', 'x-y-z', '=', '6', 'col-z', 
'=', 'berry', '@f', '{', 'border', ':', '10px', 'solid', 
'black', ';', 'border-radius', ':', '50%', ';', '}', '.add', 
'{', 'color', ':', 'white', ';', 'background-color', ':', 
'rgb', '(', '3', ',', '4', ',', '5', ')', ';', '}', '#ad', 
'{', 'color', ':', 'rgb','(', 'x', ',', '4', ',', '5', ')', 
';', '}', '.a', 'div', 'a', '{', 'color', ':', '..col-z', 
';', '@f', '}', '']

```



With such separated data, it's much easier to proceed!




### The Concept of Memory




Next we define a dictionary to hold all our variables.





```python

memory = {}

```



where 





```python

x = 1

```



will become this later on:





```python

{'x':'1'}

```



to retrieve it we'll just do 





```python

memory['x']

```



### The Concept of Tree




We'll have a dictionary called tree





```python

tree = {}

```



which will hold the converted code as





```python

{
    '@f': {
        'border': '10px solid black', 
        'border-radius': '50%'
    }, 
    '.add': {
        'color':'white', 
        'background-color': 'rgb ( 3 , 4 , 5 )'
    }, '#ad': {
        'color': 'rgb ( x ,4 , 5 )'
    }, 
    '.a div a': {
        'color': '..col-z', 
        '@f': ''
    }
}

```



Our next step will exactly be this: converting the lexemes list into this dictionary




### Generating The Tree




To keep track of where we are, we'll have a series of variables taking True/False values (on/off)




#### Setting up holders





```python

id_string = ''
last_id_string = ''
last_attribute = ''

current_attribute = ''
current_value = ''

len_lexemes = len(lexemes)

```



id string will hold like #add, .x a div etc




the last\_ variables just hold variables that are not emptied upon leaving the sub section




#### Setting up flags




We'll have 3 flags.




One when we are starting a block, which will become true when encountering a { and false when encountering a }




An attribute is color in color:black;




The attribute ongoing will become true when passing over { and ; and will become false when passing over :




value\_ongoing will become true when going over : and false when going over ;





```python

block_ongoing = False
attribute_ongoing = False
value_ongoing = False

```



We'll start looping over the list and implement what we described of the flags above





```python

for i, lex in enumerate(lexemes):

    if i+1 < len_lexemes:
        next_lexeme = lexemes[i+1]
    prev_lexeme = lexemes[i-1]

    if lex == SYM.LEFT_BRACE:
        block_ongoing = True
        attribute_ongoing = True
        continue
    elif lex == SYM.RIGHT_BRACE:
        block_ongoing = False
        statement_ongoing = False
        attribute_ongoing = False
        value_ongoing = False
        continue
    if lex == SYM.COLON:
        value_ongoing = True
        attribute_ongoing = False
        continue
    elif lex == SYM.SEMI_COLON:
        value_ongoing = False
        statement_ongoing = False
        attribute_ongoing = True
        continue

```



Continue is needed as once we have activated a flag, we have no work to do, we move on.




### Dealing with variables




To assign variables, we just wait for the = sign then continue.




Then when going over a variable name or a value we just prevent the loop from continuing by using continue





```python

    if lex == SYM.EQUAL:
        memory[prev_lexeme] = next_lexeme
        continue
    elif next_lexeme == SYM.EQUAL or prev_lexeme == SYM.EQUAL:
        continue

```



### Where The Tree Builds




Now we'll make use of the flags





```python

    if not block_ongoing:
        id_string += lex + ' '
    elif block_ongoing:
        if id_string:
            tree[id_string.strip()] = {}
            last_id_string = id_string.strip()
            id_string = ''

```



Here we are dealing with the block id, example #add in #add {}. We did 





```python

tree[id_string.strip()] = {}

```



here is an example tree at this point





```python

{
'.add': {}
}

```



Using the same principle, we'll do so for the attribute





```python

    if attribute_ongoing:
        current_attribute += lex
    elif not attribute_ongoing:
        if current_attribute:
            tree[last_id_string][current_attribute] = ''
            last_attribute = current_attribute
            current_attribute = ''

```



Here is an example tree at this point





```python

{
'.add': {
        'color':''
    }
}

```



and value





```python
    if value_ongoing:
        current_value += lex + ' '
    elif not value_ongoing:
        if current_value:
            tree[last_id_string][last_attribute] = current_value.strip()
            last_value = current_value.strip()
            current_value = ''
```



Here is an example tree at this point





```python

{
'.add': {
        'color':'white'
    }
}

```



That snippet ends our tree-building block




### Replacing Values




Now let us see how to replace variable names in functions like rgb() and rgba()





```python

def parseFunc(f):
    v = f.split(SYM.LEFT_ROUND)
    name = v[0]
    vals = v[1][:-1].replace(SYM.SPACE, '')
    values = vals.split(SYM.COMMA)
    for i, v in enumerate(values):
        if not v.isnumeric():
            values[i] = memory[v]
    return '{}({})'.format(name.strip(), ','.join(values))

```



Here we replace rgb(x, 4, 5) to rgb(1, 4, 5) by replacing the x by 1 in the memory dictionary. To build a CSS pre-processor from scratch, we have to take all cases, which we'll do after.




### Transforming The Tree Into It's Final Form




Now we need to pass over the tree once again and expand functions, replace values, including the use of our defined function above.




Technically we can't change a dictionary while iterating over it. We have to copy it to break references to it. We have to deepcopy it.





```python

ntree = copy.deepcopy(tree)

```




```python

for block_name in ntree:
    properties = ntree[block_name]
    if block_name[0] == SYM.AT:
        continue
    
```



Now, if we get the first symbol of the id as a @, we just skip it as we don't need to expand the definition.





```python

    for element in properties:
        value = properties[element]
        if SYM.LEFT_ROUND in value:
            tree[block_name][element] = parseFunc(value)

```



Next we say if there is a ( in the value, it denotes a function like rgb(). In that case we use our function parseFunc.





```python

        if SYM.DOT in value:
            tree[block_name][element] = memory[value.strip(SYM.DOT)]

```



Next we see a . in the value, we go see in the memory dictionary and replace it





```python

        if SYM.AT in element:
            del tree[block_name][element]
            tree[block_name].update(tree[element])

```



Next we we see the @ symbol in as key in a block, we just add the dictionaries in it to the dictionaries in that block (Done by update in Python) .




That also shows the advantage of using a data structure over plain strings.




### Compiling To Normal Css




Now we can compile it to normal CSS, we'll just print it for now (you can file= in print btw)





```python

for key in tree:
    if key[0] == SYM.AT:
        continue
    print(key, '{', sep='')
    for elem in tree[key]:
        print('{}{}: {};'.format(SYM.TAB, elem, tree[key][elem]))
    print('}\n')

```



which produces





```python

.add{
    color: white;
    background-color: rgb(3,4,5);
}

#ad{
    color: rgb(1,4,5);
}

.a div a{
    color: berry;
    border: 10px solid black;
    border-radius: 50%;
}


```



### The Future of It




This was done without a safety net and lacking lot of cool features but it is done to demonstrate that with some normal programming logic, you can set up something cool. It was my usual linkedIn Project of The Week.




If you want to build a CSS pre-processor from scratch based on indentation (like stylus), use [this tutorial](https://www.pythonmembers.club/2018/05/04/building-an-indentation-analyser-in-python-tutorial/).




Github Link: <https://github.com/Abdur-rahmaanJ/dotdot>




Pictures from unsplash.




-- Abdur-Rahmaan Janhangeer



