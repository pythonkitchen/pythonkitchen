title: Checking for Prime Numbers in Python
slug: checking-for-prime
pub: 2018-12-29 15:00:00
authors: arj
tags: math, number theory, fundamentals
category: algorithms
related_posts: armstrong-numbers,daily-coding-problem-solution-1,zen-of-python-in-depth

Checking if a number is prime is a fundamental programming task. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

In this tutorial, we will explore different ways to check for primality in Python, from the naive approach to more optimized solutions.

## The Naive Approach

The simplest way to check if a number `n` is prime is to divide it by every number from 2 up to `n-1`. If any division results in a remainder of 0, then `n` is not prime.

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
```

This works, but it's slow for large numbers. The time complexity is **O(N)**.

## Optimizing the Loop: Halfway Point

We don't need to check all numbers up to `n-1`. The largest possible factor of `n` (other than `n` itself) is `n/2`. So we can stop checking at `n // 2 + 1`.

```python
def is_prime_v2(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
```

This cuts the work in half, but the complexity is still **O(N)**.

## The Efficient Approach: Square Root Optimization

We can do much better. If a number `n` is composite (not prime), it must have a factor less than or equal to its square root.

Why? If `n = a * b`, then one of the factors must be less than or equal to `sqrt(n)`. If both were greater than `sqrt(n)`, their product would be greater than `n`.

So we only need to check divisors up to `int(sqrt(n)) + 1`.

```python
import math

def is_prime_optimized(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False  # Even numbers > 2 are not prime

    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):  # Check only odd numbers
        if num % i == 0:
            return False
    return True
```

**Complexity Analysis:**
*   Time Complexity: **O(sqrt(N))**. This is significantly faster for large numbers.

## Summary

When checking for primes:
1.  Handle edge cases (numbers <= 1).
2.  Check for divisibility by 2.
3.  Loop from 3 up to the square root of `n`, checking only odd numbers.

This optimized approach is efficient enough for most competitive programming and interview scenarios.



