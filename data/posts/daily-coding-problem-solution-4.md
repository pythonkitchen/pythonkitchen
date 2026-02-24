title: Daily Coding Problem Solution 4
slug: daily-coding-problem-solution-4
pub: 2021-03-22 20:03:38
authors: arj
tags: coding challenges, arrays, logic
category: algorithms
related_posts: daily-coding-problem-solution-1,daily-coding-problem-solution-2,daily-coding-problem-solution-3

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.



---


### Attempt 1



```python
def lowest_positive(arr):
    num = None
    arr = sorted(list(set(arr)))
    # arr = [i for i in arr if i > 0]
    for i, n in enumerate(arr):
        if n > 0: # if uncomment above, comment here
            if i+1 < len(arr):
                if n+1 == arr[i+1]:
                    continue
                else:
                    num = n+1
                    break
    if num is None:
        num = arr[-1] + 1
    return num

assert lowest_positive([3, 4, -1, 1]) == 2, 'fail'
assert lowest_positive([1, 2, 0]) == 3, 'fail'

```


nLog(n)

### Attempt 2



```python
def lowest_positive2(arr):
    # 2nd solution
    minimum = None
    nums = []

    for i, n in enumerate(arr):
        if n > 0:
            nums.append(n)
            if minimum is None:
                minimum = n
            if n < minimum:
                minimum = n

    i = 1
    while 1:
        if minimum+i in nums:
            i+=1
            continue
        else:
            return minimum+i

```


O(n^2) worst case

### Attempt 3



```python
def lowest_positive3(arr):
    # 3rd solution
    minimum = None
    maximum = None
    nums = []

    for i, n in enumerate(arr):
        if n > -1:
            nums.append(n)
            if minimum is None:
                minimum = n
            if n < minimum:
                minimum = n

            if maximum is None:
                maximum = n
            if n > maximum:
                maximum = n
    i = 1
    while 1:
        if minimum+i == nums[i-1]:

            i+=1
            continue
        else:
            return (minimum+i)

    return maximum+1

```


O(n)
