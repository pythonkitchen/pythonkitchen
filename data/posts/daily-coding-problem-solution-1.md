title: Daily Coding Problem Solution 1
slug: daily-coding-problem-solution-1
pub: 2021-03-22 19:19:57
authors: arj
tags: 
category: algorithm and data structures,daily coding problem

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?



---


### Very Bad Solution:



```python
def add_up_to_k_v1(mylist, k):

    ans = [x+y==k for x in mylist for y in mylist]

    return sum(ans) > 0

```

### My Original Solution Demo



```python
def add_up_to_k_v2(mylist, k):
    for i, num in enumerate(mylist):
        if k-num in mylist:
            return True
    return False


assert add_up_to_k_v1(mylist, k) == True, 'fail'
assert add_up_to_k_v2(mylist, k) == True, 'fail'

```


Zyaad Jaunoo: Using a "set" instead of a list will bring down the complexity to nlogn.
