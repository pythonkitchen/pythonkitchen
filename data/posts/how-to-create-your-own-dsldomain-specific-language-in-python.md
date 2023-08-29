title: how to create your own DSL(Domain Specific Language) in python
slug: how-to-create-your-own-dsldomain-specific-language-in-python
pub: 2018-09-03 05:50:09
authors: arj
tags: 
category: compiler theory

Sometimes you need more than a cli program. You need more flexibility and control. A Domain Specific Language (DSL) is the right fit for specialised tasks. This post shows how you can build your own.

Some rough notes/planning :

```python
aim : calculate cost of houses

input :
num of houses
price of house

output :
price of houses

technical tasks :
show to screen

--- file ---

house num 1,000
house price 250,000
calculate sum

--- output ---

$ 250 000 000
```

the code
--------



```python
# py 3.7
import locale

source = '''
# calculates price of houses
house num 100
house price 250,000
calculate price
'''

def calculate(houses, unit_price):
    calc_price = houses * unit_price
    return calc_price

def output(price):
    # $ 250 000
    locale.setlocale(locale.LC_ALL, '')
    return f'{locale.currency(price, grouping=True)}'

def sanitise_price(price):
    # 250,000 -> 250 000
    return int(price.replace(',', ''))

def parse(source):
    houses = 0
    unit_price = 0
    calc_price = 0
    lines = [i for i in source.split('\n') if i]
    for line in lines:
        # simplification
        tokens = line.split()
        # comment
        if tokens[0] == '#':
            continue
        # commands
        elif tokens[0] == 'house':
            if tokens[1] == 'num':
                houses = sanitise_price(tokens[2])
            elif tokens[1] == 'price':
                unit_price = sanitise_price(tokens[2])
        elif tokens[0] == 'calculate' and tokens[1] == 'price':
            calc_price = calculate(houses, unit_price)
            print(output(calc_price))

parse(source)

```

you must  modify it to read from file
last words
----------


it might seem simple (it is) but at corporate level, the future await those who dare. a script might be simple, but if it does the job, no prob.
