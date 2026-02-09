title: Mastering Python's Regex: Part 1 - The Basics
slug: mastering-pythons-regex-part-1-basics
pub: 2018-08-03 20:04:02
authors: arj
tags: python, regex, programming, search, patterns
category: regex

Regular Expressions, or **Regex**, are often seen as a "dark art" by beginning programmers. At first glance, they look like a jumble of bizarre symbols and incomprehensible strings. However, once you understand the basic logic, Regex becomes one of the most powerful tools in your coding arsenal.

Whether you're cleaning data, building a compiler, or just searching for a specific string in a large text file, Regex is the right tool for the job.

---

## What is a Regular Expression?

A regular expression is a sequence of characters that forms a **search pattern**. You can use this pattern to:
1.  Check if a string contains a specific pattern.
2.  Extract specific parts of a string.
3.  Replace parts of a string with something else.

In Python, all regex functionality is contained in the `re` module.

---

## The Core Functions

### 1. `re.search()`
This function searches the entire string for a match and returns a match object if found.

```python
import re

text = "The quick brown fox jumps over the lazy dog"
match = re.search(r"fox", text)

if match:
    print(f"Found '{match.group()}' at index {match.start()}")
```

### 2. `re.match()`
Unlike `search`, `match()` only checks if the pattern matches from the **beginning** of the string.

```python
# This will return None because "fox" is not at the start
print(re.match(r"fox", text)) 

# This will match
print(re.match(r"The", text))
```

### 3. `re.findall()`
If you want to find every occurrence of a pattern, use `findall()`. It returns a simple list of strings.

```python
emails = "Contact us at support@example.com or sales@example.org"
# A simple pattern to find emails (simplified)
found = re.findall(r"[\w\.-]+@[\w\.-]+", emails)
print(found) # ['support@example.com', 'sales@example.org']
```

---

## The Secret Ingredient: Raw Strings (`r""`)

You’ll notice that most regex patterns in Python are prefixed with an `r`, like `r"\n"`. This stands for **Raw String**.

In a normal string, `\n` means "newline." In Regex, backslashes are used for many special commands (like `\d` for digits). By using a raw string, you tell Python: "Don't interpret these backslashes; pass them directly to the Regex engine."

---

## Your First Special Characters

Regex uses "metacharacters" to define complex patterns. Here are the most common ones to get you started:

*   **`.` (Dot):** Matches any single character except a newline.
*   **`*` (Star):** Matches 0 or more occurrences of the preceding character.
*   **`+` (Plus):** Matches 1 or more occurrences.
*   **`?` (Question):** Matches 0 or 1 occurrence.
*   **`^` (Caret):** Matches the start of the string.
*   **`$` (Dollar):** Matches the end of the string.

### Example: The Star Operator
```python
# Pattern: 'ab*' means 'a' followed by zero or more 'b's
print(re.findall(r"ab*", "a ab abb abbbbb b")) 
# Output: ['a', 'ab', 'abb', 'abbbbb']
```

## Summary

Regex might seem intimidating, but it follows a strict and logical set of rules. By starting with these basic functions and characters, you can already perform complex search-and-replace tasks that would be nearly impossible with standard string methods.

In Part 2, we’ll dive into **Character Sets** and **Grouping**!

### Related Posts:
*   [Building a Lexer from Scratch in Python](https://www.pythonkitchen.com/building-a-lexer-in-python-tutorial/)
*   [How to Create Your Own DSL in Python](https://www.pythonkitchen.com/how-to-create-your-own-dsldomain-specific-language-in-python/)