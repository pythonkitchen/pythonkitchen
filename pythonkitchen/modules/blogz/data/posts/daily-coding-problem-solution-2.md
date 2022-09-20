title: Daily Coding Problem Solution 2
slug: daily-coding-problem-solution-2
pub: Mon, 22 Mar 2021 19:24:08 +0000
authors: Abdur-RahmaanJ

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?



---


### A Pythonic Attempt



```python
import copy
import functools

mylist1 = [1, 2, 3, 4, 5]
output1 = [120, 60, 40, 30, 24]

mylist2 = [3, 2, 1]
output2 = [2, 3, 6]

def prod_arr(mylist):
    # pythonic
    ans = []
    for i, num in enumerate(mylist):
        copied = copy.deepcopy(mylist)
        copied.remove(num)
        ans.append(functools.reduce(lambda a,b : a*b, copied))
    return ans


def prod_arr2(mylist):
    # barebones
    ans = []
    for i, num in enumerate(mylist):
        prod = 1
        for i2, num2 in enumerate(mylist):
            if i2 != i:
                prod *= num2
        ans.append(prod)
    return ans

assert prod_arr(mylist1) == output1, 'fail'
assert prod_arr(mylist2) == output2, 'fail'

assert prod_arr2(mylist1) == output1, 'fail'
assert prod_arr2(mylist2) == output2, 'fail'

```

### The Real Solution Online



```python
def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result

```

