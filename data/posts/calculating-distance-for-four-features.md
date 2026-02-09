title: Multi-Dimensional Euclidean Distance: Calculating Distance for N Features
slug: calculating-distance-for-four-features
pub: 2018-07-22 03:37:21
authors: arj
tags: math, python, data-science, algorithms, geometry
category: data science, machine learning

In data science and machine learning, measuring the similarity between two points is a foundational task. One of the most common ways to do this is by calculating the **Euclidean Distance**. 

While many beginners learn the formula for 2D points (X and Y), the math stays remarkably similar even as you add more dimensions (features). In this guide, we'll look at how to calculate distance for 4 features and how to write a generalized Python function for any number of dimensions.

---

## The Formula

The Euclidean distance between two points $P$ and $Q$ in $n$-dimensional space is the square root of the sum of the squares of the differences between their coordinates.

$$Distance = \sqrt{\sum_{i=1}^{n} (Q_i - P_i)^2}$$

### For 4 Features:
If we have Point A $(a_1, a_2, a_3, a_4)$ and Point B $(b_1, b_2, b_3, b_4)$:
$$Dist = \sqrt{(b_1-a_1)^2 + (b_2-a_2)^2 + (b_3-a_3)^2 + (b_4-a_4)^2}$$

---

## Manual Calculation in Python

If you have two specific points, you can calculate the distance using Python's `math.sqrt()`:

```python
import math

# Point A: (Width, Height, Weight, ColorValue)
A = (1, 2, 5, 1)

# Point B: (Width, Height, Weight, ColorValue)
B = (7, 1, 3, 0)

dist = math.sqrt((7-1)**2 + (1-2)**2 + (3-5)**2 + (0-1)**2)

print(f"Distance: {dist:.4f}")
# Output: 6.4807
```

---

## Creating a Generalized Function

In a real project, you don't want to hardcode the subtraction for every feature. We can write a function that takes two lists of any length and returns the distance.

```python
import math

def calculate_euclidean_distance(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions")
        
    squared_differences = []
    for i in range(len(p1)):
        diff = (p1[i] - p2[i]) ** 2
        squared_differences.append(diff)
        
    return math.sqrt(sum(squared_differences))

# Example usage with 4 features
point_x = [10, 20, 15, 5]
point_y = [12, 18, 14, 8]

result = calculate_euclidean_distance(point_x, point_y)
print(f"Result: {result}")
```

## The "Professional" Way: Using NumPy

If you are working on a data science project with large datasets, calculating distances in a loop is slow. The **NumPy** library is optimized for these calculations and is much more concise.

```python
import numpy as np

p1 = np.array([1, 2, 5, 1])
p2 = np.array([7, 1, 3, 0])

# NumPy can subtract entire arrays and calculate the norm in one step
dist = np.linalg.norm(p1 - p2)

print(f"NumPy Distance: {dist:.4f}")
```

## Why does this matter?

Euclidean distance is the engine behind many popular machine learning algorithms, including:
1.  **K-Nearest Neighbours (K-NN):** Finding the closest neighbors to a new data point.
2.  **K-Means Clustering:** Assigning data points to the nearest cluster center.
3.  **Recommendation Systems:** Finding users with similar tastes (coordinates).

### Related Posts:
*   [Identifying Cutlery items using K-NN](https://www.pythonkitchen.com/identifying-home-cutlery-items/)
*   [Machine Learning Part 11: Clustering Basics](https://www.pythonkitchen.com/machine-learning-part-11-unpervised-learning/)