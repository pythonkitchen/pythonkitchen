title: Daily Coding Problem #1: Two Sum Solution in Python
slug: daily-coding-problem-solution-1
pub: 2021-03-22 19:19:57
authors: arj
tags: python, algorithms, google, interview, two-sum
category: algorithm and data structures, daily coding problem

This problem was recently asked by Google and is a classic interview question often referred to as "Two Sum".

## The Problem

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return `true` since `10 + 7` is `17`.

**Bonus:** Can you do this in one pass?

---

## Solution 1: Brute Force (The "Bad" Way)

The most intuitive approach is to check every pair of numbers. We can loop through the list twice.

```python
def add_up_to_k_v1(mylist, k):
    # This checks every combination
    ans = [x + y == k for x in mylist for y in mylist]
    return sum(ans) > 0
```

**Complexity Analysis:**
*   Time Complexity: **O(N²)** because of the nested iteration (or list comprehension).
*   Space Complexity: **O(N²)** because we are creating a list of boolean results for every pair.

This is not efficient for large lists.

---

## Solution 2: Using a Set (The Efficient Way)

We can improve this significantly by using a set (hash map). As we iterate through the list, we can check if the "complement" (the number we need to reach `k`) has already been seen.

If we are at number `num`, we need to find `k - num`. If `k - num` exists in our set of seen numbers, we have found a pair!

```python
def add_up_to_k_v2(mylist, k):
    seen = set()
    for num in mylist:
        target = k - num
        if target in seen:
            return True
        seen.add(num)
    return False

# Test cases
mylist = [10, 15, 3, 7]
k = 17

assert add_up_to_k_v2(mylist, k) == True, 'Test Failed'
print("Test Passed!")
```

**Complexity Analysis:**
*   Time Complexity: **O(N)**. We iterate through the list once. Set lookups are O(1) on average.
*   Space Complexity: **O(N)**. In the worst case, we store all numbers in the set.

This "one pass" solution is much faster and is the expected answer in a coding interview.
