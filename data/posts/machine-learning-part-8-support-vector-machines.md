title: Machine Learning Part 8: Support Vector Machines (SVM)
slug: machine-learning-part-8-support-vector-machines
pub: 2021-04-07 10:08:14
authors: arj
tags: machine learning, svm, classification, hyperplane, kernel-trick
category: machine learning

Support Vector Machines (SVM) are powerful supervised learning models used for classification and regression. In this post, we'll break down the geometry and logic behind them.

## The Goal: Finding the Best Boundary

Imagine you have two groups of data points on a 2D graph. You want to draw a line that separates them. There are many lines you could draw, but which one is the "best"?

### Hyperplanes 🔎
In SVM, the boundary that separates the data is called a **Hyperplane**.
*   In **2D**, a hyperplane is a **1D line**.
*   In **3D**, a hyperplane is a **2D plane**.
*   In **N dimensions**, a hyperplane has **N-1 dimensions**.

### Margin and Support Vectors 🚂
SVM doesn't just find *any* line; it finds the one with the **Maximum Margin**.

1.  **Support Vectors:** These are the data points from each class that are closest to the boundary. They "support" the hyperplane.
2.  **Margin:** The distance between the hyperplane and the support vectors. 

The goal of SVM is to maximize this margin. A wider margin acts like a "safety buffer," making the model more robust to new, slightly different data.

---

## The Kernel Trick 🚂

What if the data isn't linearly separable? Imagine a ring of "Type A" points surrounding a circle of "Type B" points. No straight line can separate them.

SVM solves this using the **Kernel Trick**. It mathematically transforms the data from a lower dimension to a **higher dimension** where a flat hyperplane *can* separate them. 

Think of it like lifting the "Type B" points off the table into the air; now you can slide a sheet of paper (a plane) between them and the "Type A" points on the table.

## Summary
*   **SVM** looks for the widest possible "street" between classes.
*   **Support Vectors** are the most important points that define that street.
*   The **Kernel Trick** allows SVM to solve complex, non-linear problems.

## Exercise
Research these terms to see the math behind SVM:
1. **Lagrange Multipliers**
2. **Platt's SMO Algorithm** (The standard algorithm for training SVMs)

Next, we move into the world of **Neural Networks**—the foundation of modern AI.