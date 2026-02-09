title: Daily Coding Problem #2: Product of Array Except Self
slug: daily-coding-problem-solution-2
pub: 2021-03-22 19:24:08
authors: arj
tags: python, algorithms, uber, interview, product-array
category: algorithm and data structures, daily coding problem

This problem was asked by Uber and is a popular variation of array manipulation questions.

## The Problem

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

**Example 1:**
Input: `[1, 2, 3, 4, 5]`
Output: `[120, 60, 40, 30, 24]`

**Example 2:**
Input: `[3, 2, 1]`
Output: `[2, 3, 6]`

**Follow-up:** What if you can't use division?

---

## Solution 1: Division (If allowed)

If division is allowed, the solution is simple: calculate the product of all numbers, then divide by the current number for each index.

*   Total Product = `1 * 2 * 3 * 4 * 5 = 120`
*   Index 0: `120 / 1 = 120`
*   Index 1: `120 / 2 = 60`
*   ...and so on.

However, this fails if there are zeros in the array! And often, interviews explicitly forbid division.

## Solution 2: Without Division (Prefix and Suffix Products)

Without division, we can solve this by calculating the product of all numbers to the **left** of `i` and multiplying it by the product of all numbers to the **right** of `i`.

We can do this efficiently using two passes (or three if we store prefix/suffix separately).

1.  **Prefix Pass:** Iterate forward, storing the running product.
2.  **Suffix Pass:** Iterate backward, storing the running product.
3.  **Combine:** Multiply prefix[i] * suffix[i].

```python
def product_except_self(nums):
    length = len(nums)
    
    # Initialize result array
    answer = [0] * length
    
    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the answer[0] would be 1
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
    
    # R contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R would be 1
    R = 1
    for i in reversed(range(length)):
        # For the index 'i', R would contain the product of elements to the right of 'i'
        answer[i] = answer[i] * R
        R *= nums[i]
        
    return answer

# Test
input_arr = [1, 2, 3, 4, 5]
print(product_except_self(input_arr))
# Output: [120, 60, 40, 30, 24]
```

**Complexity Analysis:**
*   Time Complexity: **O(N)**. We iterate through the array twice.
*   Space Complexity: **O(1)** (excluding the output array), as we reuse the `answer` array to store prefixes and update it on the fly with suffixes.

This is the optimal solution often expected in technical interviews.

