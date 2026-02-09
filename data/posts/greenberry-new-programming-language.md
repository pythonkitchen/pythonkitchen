title: Case Study: Building greenBerry, a New Programming Language in Python
slug: greenberry-new-programming-language
pub: 2018-05-01 10:38:55
authors: tim
tags: python, programming-languages, greenBerry, software-development, projects
category: projects

What does it take to create a programming language from scratch? While many think of complex C++ compilers, you can actually build a functional (though simple) language using Python. This is the story of **greenBerry**.

## What is greenBerry?

**greenBerry** (or **gb** for short) is a brand new, one-line statement programming language. It started as a fun experiment to explore the boundaries of string parsing and command execution in Python. While it's not meant to replace Python or Java, it serves as a fantastic educational tool for understanding how interpreters work.

Technically, greenBerry is an interpreted language written in Python. Its files use the `.gb` extension and feature an extremely minimalist syntax.

---

## Simple and Readable Syntax

The philosophy behind greenBerry is absolute readability. There are no curly braces, semi-colons, or complex indentations for basic commands.

Here is the classic "Hello World" in greenBerry:

```python
print string Hello world!
```

Wait, that's it? Yes! The interpreter reads the `print` keyword, identifies the type as `string`, and then outputs everything that follows.

For a full breakdown of the syntax, check out the [official syntax documentation](https://abdur-rahmaanj.github.io/greenBerry/syntax.html).

---

## Under the Hood: How it Works

The project is split into several modular components, making it easy for contributors to dive in and add features. You can explore the source code on [GitHub](https://github.com/Abdur-rahmaanJ/greenBerry).

### 1. The Engine (`greenBerry.py`)
This is the "brain" of the language. It contains the logic for parsing the `.gb` files and deciding which Python functions to execute based on the keywords found.

### 2. The REPL (`greenBerry_REPL.py`)
Short for **Read-Eval-Print Loop**, this allows you to write gb code line-by-line and see the output immediately—much like the standard Python interactive shell.

### 3. The IDE (`greenBerry_IDE.py`)
To make the experience complete, we developed a simple IDE specifically for greenBerry. It allows you to write, save, and run your code in a single environment without touching the terminal.

---

## Why Build a Language?

Building a language like greenBerry is the ultimate exercise in **string manipulation** and **logic design**. It forces you to think about how a computer perceives instructions.

If you're interested in building your own language, we recommend starting with our foundational tutorials:
*   [Building a Lexer in Python: A Step-by-Step Guide](https://www.pythonkitchen.com/building-a-lexer-in-python-tutorial/)
*   [Building an Indentation Analyser for Custom Syntax](https://www.pythonkitchen.com/building-an-indentation-analyser-in-python-tutorial/)

## Get Involved!

greenBerry is an open-source project, and we have big plans for its future. Whether you want to add new keywords, improve the IDE, or just play around with the code, we'd love to see what you create. 

Go ahead, download the source, and start your journey into language design today!