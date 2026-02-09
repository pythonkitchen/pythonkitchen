title: Machine Learning Part 4: Gradient Descent and Cost Function
slug: machine-learning-part-4-gradient-descent-and-cost-function
pub: 2019-01-24 14:00:21
authors: arj
tags: machine learning, gradient descent, cost function, optimization
category: machine learning

In this part, we explore the engine under the hood of most machine learning algorithms: **Optimization**. Specifically, we will look at the **Cost Function** and **Gradient Descent**.

## The Cost Function (Mean Squared Error)

To improve a model, we first need a way to measure how "wrong" it is. This measurement is called the **Cost Function**.

The most common cost function for regression is **Mean Squared Error (MSE)**. 
1.  Calculate the **Error**: The difference between the actual value ($y$) and the predicted value ($\hat{y}$).
2.  **Square** the errors: This makes all values positive and penalizes larger errors more heavily.
3.  **Mean**: Take the average of these squared errors.

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

Our goal is to find the values of $m$ and $c$ that result in the **lowest possible cost**.

## Gradient Descent

**Gradient Descent** is an optimization algorithm used to find the minimum of a function. In machine learning, we use it to find the values of our model parameters ($m$ and $c$) that minimize the cost function.

Imagine you are standing on a mountain in a thick fog. To find the bottom of the valley, you feel the slope of the ground under your feet and take a step in the direction where the slope goes down most steeply. You repeat this until the ground is flat.

### How it Works:
1.  **Iterative:** It repeats the process over and over.
2.  **Steps:** The size of each step is determined by the **Learning Rate**.
    *   **Too small:** It will take forever to reach the bottom.
    *   **Too large:** You might overstep the bottom and end up back on the other side.

### The Math in Python

Here is a simple implementation using NumPy to demonstrate how a model "learns" the line of best fit.

```python
import numpy as np

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        # Calculate Cost (MSE)
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
        
        # Calculate Derivatives (Gradients)
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)
        
        # Update weights
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        
        if i % 100 == 0:
            print(f"Iteration {i}: m {m_curr:.4f}, b {b_curr:.4f}, cost {cost:.4f}")

# Sample Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
```

## Summary

*   The **Cost Function** tells us how far off our predictions are.
*   **Gradient Descent** tells us how to change our parameters to reduce that error.
*   The **Learning Rate** controls how quickly we try to reach the optimal solution.

**Exercise:**
Look up **Stochastic Gradient Descent (SGD)**. How does it differ from the "Batch" gradient descent we used here?





