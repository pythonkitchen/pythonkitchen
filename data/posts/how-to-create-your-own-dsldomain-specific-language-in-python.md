title: Creating Your Own Domain Specific Language (DSL) in Python
slug: how-to-create-your-own-dsldomain-specific-language-in-python
pub: 2018-09-03 05:50:09
authors: arj
tags: python, dsl, compiler-theory, automation, programming
category: compiler theory

Sometimes, a standard CLI tool isn't enough, but a full-blown programming language is overkill. This is where a **Domain Specific Language (DSL)** shines. A DSL is a mini-language designed to solve a very specific problem—think SQL for databases or HTML for web structure.

In this tutorial, we’ll build a simple DSL to calculate the total cost of a real estate portfolio. This will combine concepts from our [Lexer](https://www.pythonkitchen.com/building-a-lexer-in-python-tutorial/) and [Indentation Analyser](https://www.pythonkitchen.com/building-an-indentation-analyser-in-python-tutorial/) guides into a practical application.

---

## The Vision: Our Custom Syntax

We want a language that looks like this:

```text
# Real Estate Calculator
house num 100
house price 250,000
calculate price
```

It’s readable, human-friendly, and perfectly tailored to our task.

---

## Implementation: The Parser

A simple way to build a DSL in Python is to read the source code line-by-line and split each line into "tokens."

```python
import locale

# Sample source code in our custom DSL
source_code = '''
# Property Analysis
house num 12
house price 350,000
calculate price
'''

def parse_dsl(source):
    num_houses = 0
    unit_price = 0
    
    lines = source.strip().split('\n')
    
    for line in lines:
        tokens = line.split()
        
        # 1. Ignore comments and empty lines
        if not tokens or tokens[0] == '#':
            continue
            
        # 2. Handle 'house' commands
        if tokens[0] == 'house':
            if tokens[1] == 'num':
                num_houses = int(tokens[2])
            elif tokens[1] == 'price':
                # Remove commas and convert to int
                unit_price = int(tokens[2].replace(',', ''))
                
        # 3. Handle 'calculate' commands
        elif tokens[0] == 'calculate':
            if tokens[1] == 'price':
                total = num_houses * unit_price
                print(f"Total Portfolio Value: {format_currency(total)}")

def format_currency(amount):
    # Standard Python formatting for currency
    return "${:,.2f}".format(amount)

# Run our DSL
parse_dsl(source_code)
```

---

## Why go through the trouble?

### 1. Empowerment
DSLs allow non-programmers (like accountants or researchers) to write complex logic using a syntax that makes sense to them. 

### 2. Validation
Because your DSL is specialized, your parser can catch errors that a general language wouldn't. For example, your parser can throw an error if someone tries to set a negative number of houses.

### 3. Maintainability
If the logic for calculating "total price" changes (e.g., adding a tax rate), you only need to change it in one place (the Python function), and all your DSL scripts will automatically use the new logic.

---

## Conclusion

Building a DSL is the ultimate form of automation. You aren't just writing a script; you're writing a tool that allows others to write their own scripts. 

If you want to take this further, check out the **`ply`** or **`lark`** libraries in Python—they are designed to help you build much more complex and powerful languages!

### Further Reading:
*   [Building a Lexer in Python](https://www.pythonkitchen.com/building-a-lexer-in-python-tutorial/)
*   [Building an Indentation Analyser](https://www.pythonkitchen.com/building-an-indentation-analyser-in-python-tutorial/)