title: Daily Coding Problem Solution 5
slug: daily-coding-problem-solution-5
pub: Mon, 22 Mar 2021 20:02:41 +0000
authors: Abdur-RahmaanJ

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b): 
 def pair(f): 
 return f(a, b) 
 return pair

Implement car and cdr.



---



I managed to get a solution from none other than a Python Core Developer, Mr Cameron Simpson. Begin:

These look like implementations of Lisp operators, which I've never
found easy to remember. So I'll do this from first principles, but
looking at the (uncommented) code.

This is some gratuitiously tricky code. Maybe that's needed for these
operators. But there's a lot here, so let's unpick it:


> 
>  def cons(a, b):
>  def pair(f):
>  return f(a, b)
>  return pair
> 



Cons returns "pair", a function which itself accepts a function "f",
calls it with 2 values "a, b" and returns the result. For ultra
trickiness, those 2 values "a, b" are the ones you passed to the initial
call to cons().

This last bit is a closure: when you define a function, any nonlocal
variables (those you use but never assign to) have the defining scope
available for finding them. So the "pair" function gets "a" and "b" from
those you passed to "cons".

Anyway, cons() returns a "pair" function hooked to the "a" and "b" you
called it with.


> 
>  def car(c):
>  return c(lambda a, b: a)
> 



The function accepts a function, and calls that function with "lambda a,
b: a", which is itself a function which returns its first argument. You
could write car like this:


```python
    def car(c):
        def first(a, b):
            return a
        return c(first)

```


The lambda is just a way to write a simple single expression function.


> 
>  print(cons(1, 2)(lambda a, b: a))
> 



What is "cons(1,2)". That returns a "pair" function hooked up to the a=1
and b=2 values you supplied. And the pair function accepts a function of
2 variables.

What does this do?


```python
    cons(1, 2)(lambda a, b: a)

```


This takes the function returns by cons(1,2) and *calls* that with a
simple function which accepts 2 values and returns the first of them.

So:


```python
    cons(1,2) => "pair function hooked to a=1 and b=2"

```


Then call:


```python
    pair(lambda a, b: a)

```


which sets "f" to the lambda function, can calls that with (a,b). So it
calls the lambda function with (1,2). Which returns 1.


> 
>  print(car(cons(1, 2)))
> 



The "car" function pretty much just embodies the call-with-the-lambda.


> 
>  but i don't understand how lambda achieves this
> 



If you rewite the lambda like this:


```python
    def a_from_ab(a,b):
        return a

```


and then rewrite the first call to cons() like this:


```python
    cons(1,2)(a_from_ab)

```


does it make any more sense?

Frankly, I think this is a terrible way to solve this problem, whatever
the problem was supposed to be - that is not clear.

On the other hand, I presume it does implement the Lisp cons and car
functions. I truly have no idea, I just remember these names from my
brief brush with Lisp in the past.
