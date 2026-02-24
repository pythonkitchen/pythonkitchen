title: Building a Lexer in Python: A Step-by-Step Tutorial
slug: building-a-lexer-in-python-tutorial
pub: 2018-05-01 11:48:58
authors: arj
tags: compilers, lexing, tokenization
category: programming languages
related_posts: building-an-indentation-analyser-in-python-tutorial,how-to-create-your-own-dsldomain-specific-language-in-python,simple-json-parser

Understanding how to build a **lexer** (lexical analyzer) is a rite of passage for many programmers. It opens up a world of possibilities, from creating your own Domain Specific Languages (DSLs) to writing custom configuration parsers. 

In this tutorial, we will break down the theory and implementation of a basic lexer using pure Python.

---

## What is a Lexer?

From the moment you type code to the moment it executes, it undergoes several transformations. The journey typically follows these steps:

1.  **Lexical Analysis (The Lexer):** Converts the raw string of code into a list of "tokens" or "lexemes."
2.  **Parsing (The Parser):** Takes the tokens and builds a structure (like an Abstract Syntax Tree) to understand the logic.
3.  **Code Generation:** Converts that structure into machine code or bytecode.
4.  **Execution:** The computer runs the code.

**A lexer is the tool that performs step 1.** It’s the eyes of the compiler; it looks at a messy string and identifies the meaningful parts.

---

## Key Terminology

*   **Scanning:** The process of reading the source code character by character.
*   **Lexeme:** A sequence of characters that matches a pattern (e.g., the word `for` or the symbol `{`).
*   **Token:** A categorized lexeme. For example, the lexeme `123` might be tokenized as `(NUMBER, 123)`.
*   **Keyword:** A lexeme that has a special, predefined meaning (e.g., `if`, `while`, `print`).

---

## The Core Logic: How to Separate Code

Imagine we have this line of code:
`for(i; i < 10; i++){ }`

Our lexer needs to separate this into:
`for`, `(`, `i`, `;`, `i`, `<`, `10`, `;`, `i`, `++`, `)`, `{`, `}`

### The Strategy
We iterate through the string character by character. We accumulate characters into a `lexeme` variable until we hit a "boundary"—usually a whitespace or a special symbol.

```python
# Conceptual Pseudo-code
lexeme = ''
for char in source_code:
    if char is a whitespace or a special symbol:
        process(lexeme)
        process(char)
        lexeme = ''
    else:
        lexeme += char
```

---

## Implementation in Python

Let's build a simple lexer that can handle a snippet of Java-like code.

### 1. Defining our Keywords

```python
# Single-character symbols that act as boundaries
SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',', ';', '=', ' ', '\t']

# Multi-character keywords
KEYWORDS = ['public', 'class', 'static', 'void', 'main', 'String', 'int', 'for']
```

### 2. The Lexing Loop

```python
def simple_lexer(source_code):
    lexemes = []
    current_lexeme = ''
    
    # We use enumerate to easily peek at the next character
    for i, char in enumerate(source_code):
        # If it's not a whitespace, add to current lexeme
        if char not in [' ', '\t', '\n']:
            current_lexeme += char
            
        # Look ahead to see if we should "break" the current lexeme
        if (i + 1 < len(source_code)):
            next_char = source_code[i + 1]
            
            # Condition to break:
            # 1. Next char is a symbol/boundary
            # 2. Current char is a symbol/boundary
            # 3. We've just completed a known keyword
            if next_char in SYMBOLS or char in SYMBOLS or current_lexeme in KEYWORDS:
                if current_lexeme != '':
                    lexemes.append(current_lexeme)
                    current_lexeme = ''
                    
    # Handle the final lexeme
    if current_lexeme:
        lexemes.append(current_lexeme)
        
    return lexemes

# Test it out
code = 'public class Test { int x = 10; }'
print(simple_lexer(code))
```

---

## Challenges and Edge Cases

The basic lexer above is a great start, but it has some limitations:

1.  **Multi-character Operators:** How do we handle `++` or `==`? Usually, we add a "lookahead" check to see if the next character combines with the current one to form a single token.
2.  **Strings:** Everything inside `" "` should be treated as one single lexeme, even if it contains spaces or symbols.
3.  **Comments:** We need flags to identify when we enter a comment (`/*` or `//`) so we can ignore the content until the comment ends.

---

## Conclusion

Building a lexer manually is a fantastic way to learn the internals of programming languages. While libraries like `re` (Regular Expressions) can make this faster, doing it "by hand" gives you complete control over the parsing logic and a deeper appreciation for the tools we use every day.

In our next tutorial, we'll look at **Tokenization**—adding types and metadata to these lexemes!

### Further Reading:
*   [Building an Indentation Analyser in Python](https://www.pythonkitchen.com/building-an-indentation-analyser-in-python-tutorial/)
*   [How to Create Your Own DSL in Python](https://www.pythonkitchen.com/how-to-create-your-own-dsldomain-specific-language-in-python/)