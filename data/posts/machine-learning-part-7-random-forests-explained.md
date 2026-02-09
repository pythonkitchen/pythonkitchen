title: Machine Learning Part 7: Random Forests Explained
slug: machine-learning-part-7-random-forests-explained
pub: 2019-02-03 13:00:39
authors: arj
tags: machine learning, random forest, ensemble learning, overfitting
category: machine learning

While Decision Trees are easy to understand, they have a major weakness: they tend to **overfit** the data. In this post, we'll see how **Random Forests** solve this problem.

## The Problem with Single Trees 🌳

Decision Trees work by drawing "boxes" around data. If a tree is allowed to grow too deep, it will create tiny, specific boxes for every single data point in your training set. This is called **overfitting**. The tree becomes great at "remembering" the training data but terrible at "predicting" new data.

### Pruning
One way to fix this is **Pruning**—cutting back branches that don't add much predictive power. This helps, but it isn't always enough.

---

## The Solution: Random Forests 🌳🌳🌳

A **Random Forest** is an "Ensemble" method. Instead of relying on one tree, it builds a whole forest of them.

### How it works:
1.  **Random Sampling (Bagging):** Each tree in the forest is trained on a random subset of the data.
2.  **Feature Randomness:** Each time a tree needs to split, it only considers a random selection of the available features.
3.  **Voting:** When it's time to make a prediction, every tree in the forest "votes." The forest then picks the majority result (for classification) or the average (for regression).

By randomizing the data and the features, the trees become different from one another. While one tree might overfit, the average of 100 different trees will be much more stable and accurate.

## Why use Random Forests?
*   **Highly Accurate:** One of the most powerful algorithms for structured data.
*   **Robust to Overfitting:** Much better than a single decision tree.
*   **Handles Missing Data:** Works well even if some data is missing.

## Real-World Uses
*   **Banking:** Detecting loyal vs. fraudulent customers.
*   **Medicine:** Identifying the correct combination of components in medicine.
*   **E-commerce:** Predicting whether a customer will recommend a product.

## Exercise
1. Research how many trees are usually in a "typical" Random Forest.
2. Compare a Random Forest implementation in Python (using `scikit-learn`) vs. other languages. You'll see why Python is the king of ML!

Next up, we dive into the "geometric" world of **Support Vector Machines (SVM)**.