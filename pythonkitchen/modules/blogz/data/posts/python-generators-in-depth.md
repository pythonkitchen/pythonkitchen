title: Python Generators:  The In-depth Article You've Always Wanted
slug: python-generators-in-depth
pub: Thu, 10 Dec 2020 06:37:27 +0000

Table of contents
=================


* Why were Python generators introduced?
* How do Python Generators differ from normal functions?
* Execution flow
* Immediate usefulness
* next and for loops
* Generators introduced for memory saving
* Generators for tasks
* The send method
* Deriving send
* What is yield from
* The last part
* The limit of generators: Infinity and Beyond



In Python, generators form part of the intermediate topics. Since it differs from conventional functions, beginners have to take sometimes to wrap their head around it. This article presents materials that will be useful both for beginners and advanced programmers. It attempts to give enough to understand generators in depth but don't cover all use cases.

### Why were Python generators introduced?



Before we present generators and it's syntax, it's important to know why in the first place were generators introduced. The yield keyword does not mean generators. One has to understand the concept behind. The original PEP introduced "the concept of generators to Python, as well as a new statement used in conjunction with them, the yield statement" [1].

The general use case of generators is as follows:


> 
>  When a producer function has a hard enough job that it requires maintaining state between values produced, [1]
> 



And more explicitly


> 
>  provide a kind of function that can return an intermediate result ("the next value") to its caller, but maintaining the function's local state so that the function can be resumed again right where it left off. [1]
> 



So we understand that a new kind of functions was needed that:

* 1. return intermediate values
* 2. save the state of functions


### How do Python Generators differ from normal functions?



Compared to normal functions, once you return from a function, you can go back to return more values. A normal function in contrast, once you return from it, there is no going back.

Normal function:


```python
def x():
    print('abc')
    return 
    print('def') # not reached
x()

```


In the above example, `def` will not be printed as the function exited before. Let's examine a basic generator example:


```python
def x():
  a = 0
  while 1:
    yield a

    a += 1

z = x()

print(z)
print(next(z))
print(next(z))

```


```python
<generator object x at 0x01ACB760>
0
1

```


From the example above, once we called next, it returned a value. **The purpose of next is to go to the next yield statement**. When we called next the first time, it went to the next yield since the beginning which is when `a` was initially at 0.

The second call of next started executing `a += 1` and went to the beginning of the loop where it encountered a yield statement and returned `a` with the updated value.

By `a` being updated we see that even when the function was exited the first time, when the program went back into it, it continued on the previous state when `a` was 0. This accomplishes the two aims of being able to resume functions and saving the previous state.

To understand it better, here are some more names that were proposed instead of yield [1] but were eventually rejected:

* return 3 and continue
* return and continue 3
* return generating 3
* continue return 3



Guido gives a summary of generators [1]:


> 
>  In practice (how you think about them), generators are functions, but with the twist that they're resumable.
> 


### Execution flow



The following snippet gives us an idea about the execution:


```python
def x():
  print('started')
  while 1:
    print('before yield')
    yield
    print('after yield')


z = x()

next(z)
print('-- 2nd call')
next(z)

```


```python
started
before yield
-- 2nd call
after yield
before yield

```


From it we confirm that the first call to next executes everything in the function until the first yield statement. We did not return any values but used yield purely to control the flow of execution in the same sense of return.

Yield needs not to be in infinite loops, you can use several at once in the same function body:


```python
def x():
  print('start')
  yield 
  print('after 1st yield')
  yield
  print('after 2nd yield')

z = x()
next(z)
next(z)
next(z)

```


```python
start
after 1st yield
after 2nd yield
Traceback (most recent call last):
  File "lab.py", line 11, in <module>
    next(z)
StopIteration

```


In case you called next more than there is yield statements, generator functions raise the `StopIteration`. In case you want to auto-handle `StopIteration` until there are no more left, use ... a for loop:


```python
def x():
  print('start')
  yield 
  print('after 1st yield')
  yield
  print('after 2nd yield')

z = x()
for _ in z:
  pass


```


In case you return a value, the loop variable will be equal to that value:


```python
def x():
  print('start')
  yield 1
  print('after 1st yield')
  yield 2
  print('after 2nd yield')

z = x()
for _ in z:
  print(_)

```


```python
start
1
after 1st yield
2
after 2nd yield

```

### Immediate usefulness



Since we saw that we can use yield with an infinite loop, this is extremely powerful. We can break infinity in steps. Consider this:


```python
def odd_till(number):
  n = 1
  while n < number:
    yield n
    n += 2

for odd_num in odd_till(10):
  print(odd_num)

```


We yield one number and the function exits, the for loop calls it again. It yields one number and exits. And so on. It goes about it in micro steps. The operations completed in one cycle is is just an increment `n += 2` and a check `n < number`.



---



> 
> `odd_till(10)` or `odd_till(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)` don't not cause memory errors
> 


### next and for loops



Two things might puzzle you:

* why was next used?
* how can a function with 2 yields work when a for loop is used with it?



The answer lies in in the fact that generators implement the iterator protocols, the same one used by lists. Here is a class customised to act as a generator [7]:


```python
# Using the generator pattern (an iterable)
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn(1000000))

```

### Generators introduced for memory saving



Consider a list comprehension:


```python
sum([x*x for x in range(10)])

```


A generator expression is much, much more efficicent [2]:


```python
sum(x*x for x in range(10))

```


This was the second addition in the generator story.

### Generators for tasks



Lets modify our two functions with print


```python
def odd_till(number):
  n = 1
  while n < number:
    print('odd_till {} currently: {}'.format(number, n))
    yield n
    n += 2

def even_till(number):
  n = 0
  while n < number:
    print('even_till {} currently: {}'.format(number, n))
    yield n
    n += 2

```


Lets have a class to run functions


```python
from collections import deque

class RunFunc:
  def __init__(self):
    self._queue = deque()

  def add_func(self, func):
    self._queue.append(func)

  def run(self):
    while self._queue:
      func = self._queue.popleft()
      try:
        next(func)
        self._queue.append(func)
      except StopIteration:
        pass

```


usage


```python
func_runner = RunFunc()

func_runner.add_func(odd_till(5))
func_runner.add_func(even_till(4))
func_runner.add_func(odd_till(6))
func_runner.run()

```



---



output


```python
odd_till 5 currently: 1
even_till 4 currently: 0
odd_till 6 currently: 1
odd_till 5 currently: 3
even_till 4 currently: 2
odd_till 6 currently: 3
odd_till 6 currently: 5

```


If we rename the same thing we get a mini task scheduler [4]


```python
from collections import deque

class TaskScheduler:
  def __init__(self):
    self._queue = deque()

  def add_task(self, task):
    self._queue.append(task)

  def run(self):
    while self._queue:
      task = self._queue.popleft()
      try:
        next(task)
        self._queue.append(task)
      except StopIteration:
        pass

```


usage


```python
scheduler = TaskScheduler()

scheduler.add_task(odd_till(5))
scheduler.add_task(even_till(4))
scheduler.add_task(odd_till(6))
scheduler.run()

```


Just a point of note, why do we remove a task (popleft) and readd it (append)?


```python
      task = self._queue.popleft()
      try:
        next(task)
        self._queue.append(task)
      except StopIteration:
        pass

```


That's because if it was finished (exception raised) well and good, it will go straight to the except block. Else the .append will get executed.

In other words if task terminated, don't add it back else add it back.

### The send method



Generators support a way of sending values to generators


```python
def times2():
    while True:
        val = yield
        yield val * 2

z = times2()


next(z)
print(z.send(1))
next(z)
print(z.send(2))
next(z)
print(z.send(3))

```


```python
2
4
6

```


This was an important addition. This passage explains why was send introduced and why it's important in asyncio [6]:


> 
>  Python's generator functions are almost coroutines -- but not quite -- in that they allow pausing execution to produce a value, but do not provide for values or exceptions to be passed in when execution resumes ... However, if it were possible to pass values or exceptions into a generator at the point where it was suspended, a simple co-routine scheduler or trampoline function would let coroutines call each other without blocking -- a tremendous boon for asynchronous applications. Such applications could then write co-routines to do non-blocking socket I/O by yielding control to an I/O scheduler until data has been sent or becomes available. Meanwhile, code that performs the I/O would simply do something like this: `data = (yield nonblocking_read(my_socket, nbytes))` in order to pause execution until the `nonblocking_read()` coroutine produced a value.
> 



yield was fundamentally changed with the addition of send.

* 1. Redefine yield to be an expression, rather than a statement. The current yield statement would become a yield expression whose value is thrown away. A yield expression's value is None whenever the generator is resumed by a normal next() call.
* 2. Add a new send() method for generator-iterators, which resumes the generator and sends a value that becomes the result of the current yield-expression. The send() method returns the next value yielded by the generator, or raises StopIteration if the generator exits without yielding another value.



send(None) can also be used instead of the first next()

### Deriving send



How do we derive send? A tricky question indeed. Here's a mini snippet showing how [4]


```python
from collections import deque

class ActorScheduler:
  def __init__(self):
    self._actors = { } # Mapping of names to actors
    self._msg_queue = deque() # Message queue

  def new_actor(self, name, actor):
    '''
    Admit a newly started actor to the scheduler and give it a name
    '''
    self._msg_queue.append((actor,None))
    self._actors[name] = actor

  def send(self, name, msg):
    '''
    Send a message to a named actor
    '''
    actor = self._actors.get(name)
    if actor:
      self._msg_queue.append((actor,msg))

  def run(self):
    '''
    Run as long as there are pending messages.
    '''
    while self._msg_queue:
      actor, msg = self._msg_queue.popleft()
      try:
        actor.send(msg)
      except StopIteration:
        pass

# Example use
if __name__ == '__main__':
  def printer():
    while True:
      msg = yield
      print('Got:', msg)

  def counter(sched):
    while True:
    # Receive the current count
      n = yield
      if n == 0:
        break
      # Send to the printer task
      sched.send('printer', n)
      # Send the next count to the counter task (recursive)
      sched.send('counter', n-1)


  sched = ActorScheduler()
  # Create the initial actors
  sched.new_actor('printer', printer())
  sched.new_actor('counter', counter(sched))
  # Send an initial message to the counter to initiate
  sched.send('counter', 100)
  sched.run()

```


The above can be expanded with more areas like ready, ready to read, ready to write and writing the appropriate code to switch between the areas and ... you have a concurrent app. This is the basics of an operating system [4]. Using `sched.send` allows to have a loop beyond the recursion limit of python. The recursion limit is `import sys; sys.getrecursionlimit()` usually 1000. try `sched.send('counter', 1001)`.

### What is yield from?



Consider the following code:


```python
def gen_alph():
  for a in 'abc':
    yield a

def gen_nums():
  for n in '123':
    yield n


def gen_data():
  yield from gen_alph()
  yield from gen_nums()


for _ in gen_data():
  print(_)

```


```python
a
b
c
1
2
3

```


It behaves exactly as if the alphabet and number loops with their respective yields was inside gen\_data.

"yield from is to generators as calls are to functions" as Brett Cannon puts it [8]

### The last part



Generators have a close method, caught by a GeneratorExit exception:


```python
def gen_alph():
  try:
    for a in 'abc':
      yield a
  except GeneratorExit:
      print('Generator exited')

z = gen_alph()
next(z)
z.close()

```


```python
Generator exited

```


They also have a throw method to catch errors:


```python
def gen_alph():
  try:
    for a in 'abc':
      yield a
  except GeneratorExit:
      print('Generator exited')
  except Exception:
    yield 'error occured'

z = gen_alph()
next(z)
print(z.throw(Exception))

```


```python
error occured

```

### The limit of generators: Infinity and Beyond



If you really want the best of Python generators the internet can give you
copied over and over by Python sites, see David Beazley's 3 parts series:

* [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators)
* [A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/)
* [Generators: The Final Frontier](http://www.dabeaz.com/finalgenerator/)



It also includes lots of use cases.

*Abdur-Rahmaan Janhangeer is an organising member of the [Python Mauritius User Group](https://www.pymug.com) (PyMUG), [FlaskCon](https://www.flaskcon.com) and maintains [pythonkitchen.com](https://www.pythonkitchen.com). The present article is the continuation of his talk about deriving asyncio*
### References



[1] https://www.python.org/dev/peps/pep-0255/
[2] https://www.python.org/dev/peps/pep-0289/
[3] https://dev.to/abdurrahmaanj/add-superpowers-to-your-python-lists-using-this-feature-24nf
[4] Python Cookbook, David Beazley
[5] https://docs.python.org/3/library/asyncio-task.html
[6] https://www.python.org/dev/peps/pep-0342/
[7] https://wiki.python.org/moin/Generators
[8] Brett Cannon: Python 3.3: Trust Me, It's Better Than Python 2.7
