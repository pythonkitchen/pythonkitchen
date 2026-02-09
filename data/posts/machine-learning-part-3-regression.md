title: Machine Learning Part 3: Understanding Regression
slug: machine-learning-part-3-regression
pub: 2019-01-23 07:38:19
authors: arj
tags: machine learning, regression, linear regression, algorithms
category: machine learning

In the previous parts, we introduced machine learning and supervised learning. Today, we focus on one of the two main pillars of supervised learning: **Regression**.

## What is Regression?

In machine learning, **Regression** simply means **prediction**. Specifically, it involves predicting a continuous numerical value.

In regression, we deal with:
*   **Independent Variables:** Often called **features** (the input).
*   **Dependent Variable:** The **target** (the value we want to predict).

## Types of Regression Methods

### 1. Simple Linear Regression
This is the most basic form, where we predict a target based on a single input variable.

Imagine plotting points on a graph and trying to draw a "line of best fit." The goal is to find the values of $m$ (slope) and $c$ (y-intercept) in the equation:
$$y = mx + c$$

### 2. Multivariate Linear Regression
Most real-world problems are complex and depend on many factors. Multivariate regression handles one target variable based on two or more features.

**Example:** Predicting the fuel cost of a trip.
Features: engine age, car weight, distance, fuel price.
Formula:
$$Cost = m_1 \cdot feature_1 + m_2 \cdot feature_2 + m_3 \cdot feature_3 + b$$

We train the model on historical data to find the optimal weights ($m_1, m_2, ...$) to make accurate predictions for new data.

### 3. Ridge Regression (Regularization)
Sometimes our models become too complex and "overfit" the training data (following every tiny fluctuation or "mountain ridge" in the data).

**Ridge Regression** is used as a **regularization** method. It adds a penalty to the model to keep the coefficients simple and prevents the model from being too sensitive to noise in the data. This leads to better predictions on new, unseen data.

---

## Exercise: Dig into the Math

To truly understand regression, I recommend researching:
1.  **Ordinary Least Squares:** How the line of best fit is actually calculated.
2.  **Polynomial Regression:** How we fit curves instead of just straight lines.
3.  **Lasso Regression:** Another regularization method similar to Ridge.

In the next post, we will look at **Cost Functions** and **Gradient Descent**—the engines that make these predictions possible!





