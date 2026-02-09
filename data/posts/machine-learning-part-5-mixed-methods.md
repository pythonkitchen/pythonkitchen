title: Machine Learning Part 5: Decision Trees and Mixed Methods
slug: machine-learning-part-5-mixed-methods
pub: 2019-01-26 14:01:04
authors: arj
tags: machine learning, decision trees, classification, regression, CART
category: machine learning

Some machine learning methods are versatile enough to be used for both **Classification** and **Regression**. These are often called "Mixed Methods."

In this post, we'll focus on one of the most popular mixed methods: **Decision Trees**.

## What are Decision Trees?

A Decision Tree is a flowchart-like structure where each internal node represents a "test" on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label or a continuous value.

When used for both tasks, they are often referred to as **CART** (Classification And Regression Trees).

### Other Mixed Methods include:
*   Random Forests (Ensembles of trees)
*   Neural Networks
*   Support Vector Machines (SVM)

---

## Example: Predicting a "Good Day" at School

Let's say we want to predict whether a student will have a **Good (G)** or **Bad (B)** day at school based on three factors:
1.  **Teacher:** Present (p) or Absent (a)
2.  **Parent Mood:** Good (g) or Bad (b)
3.  **Homework:** Done (d) or Not Done (nd)

### Our Dataset:

| Teacher | Mood | HWork | Result |
| :--- | :--- | :--- | :--- |
| a | g | d | G |
| p | b | d | G |
| a | g | nd | G |
| a | b | d | B |
| p | b | nd | B |
| a | g | nd | G |
| p | b | d | G |
| a | g | nd | G |
| a | g | d | G |

## Building the Tree: The Art of Splitting

To build an efficient tree, we need to decide which feature to "split" on first. We want the split that gives us the highest **Purity** (where the resulting groups are mostly one class).

### Comparing Splits:

**1. Split by Teacher:**
*   Absent: 5 Good, 1 Bad
*   Present: 2 Good, 1 Bad

**2. Split by Parent Mood:**
*   Good: **5 Good, 0 Bad** (100% Pure!)
*   Bad: 2 Good, 2 Bad

**3. Split by Homework:**
*   Done: 4 Good, 1 Bad
*   Not Done: 3 Good, 1 Bad

### The Winner: Parent Mood
Splitting by **Parent Mood = Good** immediately gives us a perfect prediction. If the parents are in a good mood, the student has a good day 100% of the time in our dataset.

For the **Bad Mood** branch, we would need to split further (perhaps by Teacher or Homework) to resolve the 2 Good / 2 Bad tie.

## Why use Decision Trees?

*   **Easy to understand:** You can literally draw them and follow the logic.
*   **Handle different data types:** They work with both numbers and categories.
*   **Feature Importance:** They naturally show which factors (like Parent Mood) are the most important for the prediction.

In the next part, we will look at how we mathematically measure this "purity" using concepts like **Entropy** and **Information Gain**.