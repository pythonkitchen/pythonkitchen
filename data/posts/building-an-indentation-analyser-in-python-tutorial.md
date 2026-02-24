title: Building an Indentation Analyser in Python: A Comprehensive Guide
slug: building-an-indentation-analyser-in-python-tutorial
pub: 2018-05-04 08:31:13
authors: arj
tags: static analysis, indentation, parser theory
category: programming languages
related_posts: building-a-lexer-in-python-tutorial,how-to-create-your-own-dsldomain-specific-language-in-python,dsl-python-new-language-how-to-build-a-css-pre-processor-like-sass-from-scratch-dotdot

In many programming languages, like C or Java, scope is defined by curly braces `{}`. However, languages like **Python**, **Pug**, and **Haskell** use a different approach: **Indentation**. 

Using indentation to define scope is not just a stylistic choice; it forces readable code. In this tutorial, we will build a Python script that can analyze code snippets and detect whether the indentation is correct or if it has been mixed inconsistently.

---

## The Challenge of Indentation

To a computer, a space is just another character. To turn that space into a "scope level," we need a lexer that is **whitespace-sensitive**.

If you haven't already, we recommend reading our [Introductory Lexer Tutorial](https://www.pythonkitchen.com/building-a-lexer-in-python-tutorial/) first, as we will be building upon those concepts.

### 1. Defining the Keywords
We need to treat newlines and spaces as significant characters:

*   **Symbols:** `(`, `)`, `:`, `.`, `,`, ` ` (space), `\n` (newline)
*   **Keywords:** `def`, `return`

---

## How the Indentation Analyser Works

The logic follows these rules:
1.  After a colon `:` followed by a newline `\n`, we expect an increased indentation level.
2.  We count the number of spaces at the start of each new line.
3.  The first indented line we find sets the "standard" indent level (e.g., 4 spaces).
4.  Every subsequent indented line must have a space count that is a multiple of that standard level.

### Implementation Logic

```python
def analyze_indentation(source_code):
    lines = source_code.split('\n')
    standard_level = 0
    line_number = 0
    
    for line in lines:
        line_number += 1
        # Skip empty lines
        if not line.strip():
            continue
            
        # Count leading spaces
        count = 0
        for char in line:
            if char == ' ':
                count += 1
            else:
                break
        
        # Determine the standard level from the first indented line
        if count > 0 and standard_level == 0:
            standard_level = count
            print(f"Standard indent level detected: {standard_level} spaces")
            
        # Check for inconsistent indentation
        if standard_level > 0 and count > 0:
            if count % standard_level != 0:
                print(f"Error: Inconsistent indentation on line {line_number}")
                print(f"Expected multiple of {standard_level}, but found {count} spaces.")
                return False
                
    print("Indentation check passed!")
    return True

# Test Snippet
code_snippet = '''
def my_function():
    print("Level 1")
    if True:
        print("Level 2")
      print("Error here!") # Only 6 spaces instead of 4 or 8
'''

analyze_indentation(code_snippet)
```

---

## Deep Dive: The Multi-Pass Lexer Approach

In a real-world compiler, we don't just split by lines. We use a **state machine**. 

When the lexer encounters a newline followed by spaces, it generates special tokens:
*   **INDENT:** Generated when the space count increases.
*   **DEDENT:** Generated when the space count decreases.

This allows the parser to treat indentation exactly like it would treat curly braces. 

### Why is this better?
Using `INDENT` and `DEDENT` tokens allows you to handle complex scenarios, such as when a single function contains multiple nested loops and conditional statements.

---

## Exercises for the Reader

1.  **Tab Support:** Modify the script to detect and prevent the mixing of tabs and spaces (a common Python error!).
2.  **Scope Detection:** Can you modify the script to tell you which function a specific line belongs to?
3.  **Visualizer:** Create a function that prints the code but replaces leading spaces with visual markers like `|---`.

## Conclusion

Building an indentation analyser is a great way to understand the "hidden" logic behind the languages we use every day. Whether you prefer curly braces or clean whitespace, knowing how the computer interprets your code makes you a more effective developer.

Stay tuned for our next post where we'll look at building a complete **Tokenizer**!