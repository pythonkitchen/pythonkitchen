title: building a lexer in python - a tutorial
slug: building-a-lexer-in-python-tutorial
pub: Tue, 01 May 2018 11:48:58 +0000
authors: Abdur-RahmaanJ


knowing how to build a lexer allows you to extend your applications and opens up a whole new world. You can write your own DSLs or your own language or just better separate symbols: in other words, it allows you to have more control over a string




what is a lexer?
================




from user input to code execution there are three main steps either for interpreters or compilers:




1. lexical analysis (1)
2. parsing (2)
3. code generation (example: to machine code or bytecode)
4. execution (3)




a lexer is a tool that performs lexical analysis




difference between lexical analysis and scanning
================================================




in the beginning, scanning and lexical analysis were two different steps but due to the increased speed of processors, they now refer to one and the same process and are used interchangeably.




what is scanning?
=================




scanning means to pass over / scan a string character by character (char by char).




what is lexical analysis?
=========================




it is the process whereby the scanned characters are turned into lexemes




what is a lexeme?
=================




a lexeme is a recognised piece of string




let us take:




ac




we might build a parser that outputs the following lexemes :




* lexeme 1: **the**
* lexeme 2: **quick**
* lexeme 3: **brown**
* lexeme 4: **fox**




now let us take a simili code:




**for(i; i<arr.length; i++){ }**




* lexeme 1: **for**
* lexeme 2: **(**
* lexeme 3: **i**
* lexeme 4: ;
* lexeme 5: i
* lexeme 6: **<**
* lexeme 7: **arr**
* lexeme 8: **.**
* lexeme 9: **length**
* lexeme 10: ;
* lexeme 11: **i**
* lexeme 12: **++**
* lexeme 13: **)**
* lexeme 14: **{**
* lexeme 15: **}**




so our task for this post will  be to build a program that can separate those pieces




[sc name="lexer"]


what does a lexer needs as input?
=================================




a lexer needs two things : the source code and keywords




what is a keyword?
==================




a keyword is a lexeme that has a special meaning to the lexer




normally words like print, from, to are known as keywords, however, symbols such as ( , { can also be considered as keywords




types of keywords
=================




there are single character keywords e.g. whitespace




there are multi-char  keywords such as print




ignoring keywords
=================




there are cases where we might want to ignore keywords as in the case where they appear between " " or in comments




what are ids?
=============




ids are user-defined names, like the names of namespaces, variables, classes and functions. functions in the standard library are only predefined ids. normally keyword names are banned from being used as ids




some observations
=================




let us compare :




**the quick brown fox**




and




**for(i; i<arr.length; i++){ }**




for both of the strings, lexing could be carried out. the first case is simple





```python
lexeme = ''
add characters to lexeme variable until next char is a white space
if next is a white space
    print lexeme
    lexeme = ''
```



but for the next case we observe a general rule. we break if the next character is a keyword be it a special word or symbol





```python
lexeme = ''
add characters to lexeme variable until next char is a white space (single-char keyword)
if next is a white space single-char keyword
    print lexeme
    lexeme = ''
```



in reality we also add the condition of if the element itself is a keyword




special cases
=============




now let us take the case of ++, + is a keyword and ++ too but how do we differenciate between them or ==?




that's when we use flags to determine which context are we in




flags are just variables that act like switches e.g.




x = 0




if ... : x = 1




if x == 1 : ...




or use some checks !




writing the scanner
===================




basically we just need a program that outputs a char at one time. in python it is easy :





```python
string = 'i am coming'

for char in string:
    print(char)
```



which outputs:





```python
i
 
a
m
 
c
o
m
i
n
g
```



just some fancy modifications :





```python
string = 'i am coming'

for i, char in enumerate(string): # i gives us index and char the element
    print('char', str(i+1).rjust(3, ' '), ':', char)
```



outputting:





```python
char   1 : i
char   2 :  
char   3 : a
char   4 : m
char   5 :  
char   6 : c
char   7 : o
char   8 : m
char   9 : i
char  10 : n
char  11 : g

```



writing the basic lexer
=======================




now that we can read a string char by char, we can now check if next char is a keyword




let us do it for the phrase:




**the beautiful white moon**




where white space is a keyword, referring to above :





```python
lexeme = ''
add characters to lexeme variable until next char is a white space
if next is a white space
    print lexeme
    lexeme = ''
```



we implement something similar to it i.e checking if next char is a white space:





```python
string = 'the beautiful white moon'
white_space = ' '

lexeme = ''
for i,char in enumerate(string):
    lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space: # if next char == ' '
            print(lexeme)
            lexeme = ''
```



which outputs :





```python
the
 beautiful
 white

```



moon is missing as there is no white space after it, we fix this edge case by printing the lexeme after the loop :





```python
string = 'the beautiful white moon'
white_space = ' '

lexeme = ''
for i,char in enumerate(string):
    lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space: # if next char == ' '
            print(lexeme)
            lexeme = ''
print(lexeme)
```



output :





```python
the
 beautiful
 white
 moon

```



### fixing whitespace addition




now white space got added to our lexeme, to fix we just add a character if the current char is not a whitespace :





```python
string = 'the beautiful white moon'
white_space = ' '

lexeme = ''
for i,char in enumerate(string):
    if char != white_space:
        lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space: # if next char == ' '
            print(lexeme)
            lexeme = ''
print(lexeme)


```



output :





```python
the
beautiful
white
moon
```



running on a real piece of code
===============================




let us take this piece of java code taken from tutorialspoint:





```python
public class Test {
   // main function
   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};

      for(int x : numbers ) {
         System.out.print( x );
         System.out.print(",");
      }
      /* printing new line
      */
      System.out.print("\n");
      String [] names = {"James", "Larry", "Tom", "Lacy"};

      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
```



our first task is to identify single-char and multi-char keywords




MULTI-CHAR KEYWORDS :




public, class, static, void, main, string, int, for




SINGLE-CHAR KEYWORD :




{ } ( ) ; [ ] : . \ " \*




we did not consider System as a keyword as in the language, System is the name of an id (user-defined name)




now we can feed those keywords to our lexer




### preassumption on whitespace




since whitespace still separates between like public and class:





```python
public class Test {
```



we'll keep the if next == whitespace rule





> source codes are just pieces of strings
> 
> 




we could have ignored newline was it not for single line comments




a first attempt:





```python
string = '''
public class Test {

   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
      // printing !
      for(int x : numbers ) {
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names = {"James", "Larry", "Tom", "Lacy"};
      /*
      looping over 
      */
      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
'''

symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ','] # single-char keywords
other_symbols = ['\\', '/*', '*/'] # multi-char keywords
keywords = ['public', 'class', 'void', 'main', 'String', 'int']
KEYWORDS = symbols + other_symbols + keywords

white_space = ' '
lexeme = ''

for i,char in enumerate(string):
    if char != white_space:
        lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
            if lexeme != '':
                print(lexeme.replace('\n', '<newline>'))
                lexeme = ''

```



the added conditions test if the next char is a single-char keyword or if what we already have at hand after adding a char is a keyword, if so, we then check if our variable is not empty else we'll print an empty lexeme. we also replaced newline by <newline> to better distinguish it




the above code outputs in:





```python
<newline>
public
class
Test
{
<newline>
<newline>
public
static
void
main
(
String
args
[
]
)
{
<newline>
int
[
]
numbers
=
{
10
,
20
,
30
,
40
,
50
}
;
<newline>
//
printing
!
<newline>
for
(
int
x
:
numbers
)
{
<newline>
System
.
out
.
print
(
x
)
;
<newline>
System
.
out
.
print
(
"
,
"
)
;
<newline>
}
<newline>
System
.
out
.
print
(
"
<newline>
"
)
;
<newline>
String
[
]
names
=
{
"
James
"
,
"
Larry
"
,
"
Tom
"
,
"
Lacy
"
}
;
<newline>
/
*
<newline>
looping
over
<newline>
*
/
<newline>
for
(
String
name
:
names
)
{
<newline>
System
.
out
.
print
(
name
)
;
<newline>
System
.
out
.
print
(
"
,
"
)
;
<newline>
}
<newline>
}
<newline>
}
```



see how it magically separates 10 and , System and . , String and name ... all perfect but : we have  a glitch




a glitch and the introduction the next step!
============================================




see at /\* and \*/, it considered them as / then \* and not as a single entity. that is because we defined \* as a keyword, though we did not use it here but we use it in multiplication like : 12 \* 12




so, our basic lexer has a confusion at this junction, we can for the time being tackle it like :




we modify only the loop :





```python
for i,char in enumerate(string):
    if char == '*':
        if string[i-1] == '/':
            lexeme += '/*'
        elif string[i+1] == '/':
            lexeme += '*/'
        else:
            lexeme += '*'
    elif char == '/':
        if string[i+1] != '*' and string[i-1] != '*':
            lexeme += '/'
        else:
            continue
    else:
        if char != white_space:
            lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
            if lexeme != '':
                print(lexeme.replace('\n', '<newline>'))
                lexeme = ''


```



we just added some checks to make things clear with the result that now the comments are recognised as such :





```python
/*
<newline>
looping
over
<newline>
*/
```



conclusion
==========




we built a lexer by voluntarily leaving out regex given that some lookaheads is a breeze in py. we'll move on next time to the tokeniser.




in this post, brevity was voluntarily left out, favouring a more complete approach, more programming than jargon usage!



