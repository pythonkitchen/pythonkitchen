title: Understanding Armstrong Numbers in Python
slug: armstrong-numbers
pub: 2018-12-27 19:27:39
authors: arj
tags: python, programming-challenge, beginners, math
category: programming problems

In this post, we'll explore a classic beginner programming problem: **Armstrong Numbers**.

## What is an Armstrong Number?

An Armstrong number (also known as a Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

**Formula:**
If a number $N$ has $d$ digits ($a, b, c, ...$), then:
$$N = a^d + b^d + c^d + ...$$

### Examples

**1. Number: 153**
*   Digits: 1, 5, 3
*   Number of digits ($d$): 3
*   Calculation: $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$
*   Result: **Yes**, 153 is an Armstrong number.

**2. Number: 1634**
*   Digits: 1, 6, 3, 4
*   Number of digits ($d$): 4
*   Calculation: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$
*   Result: **Yes**, 1634 is an Armstrong number.

**3. Number: 123**
*   Digits: 1, 2, 3
*   Number of digits ($d$): 3
*   Calculation: $1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36$
*   Result: **No**, 123 is not an Armstrong number (36 != 123).

---

## Python Implementation

Here is a Python script to find all Armstrong numbers up to 1,000,000.

```python
def is_armstrong(number):
    # Convert number to string to easily iterate digits
    num_str = str(number)
    num_digits = len(num_str)
    
    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
        
    return sum_of_powers == number

# Find Armstrong numbers in a range
print("Finding Armstrong numbers up to 1,000,000:")
for i in range(1000000):
    if is_armstrong(i):
        print(f"{i} is an Armstrong number")
```

### How it Works

1.  **`str(number)`**: Converting the integer to a string allows us to easily count the digits (`len()`) and iterate through them.
2.  **`int(digit) ** num_digits`**: We convert each character back to an integer and raise it to the power of the total count of digits.
3.  **Comparison**: Finally, we check if our calculated sum equals the original number.

Try running this code and see which numbers pop up! It's a great exercise for practicing loops and type conversions.



