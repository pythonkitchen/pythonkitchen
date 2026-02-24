title: Machine Learning Part 2: Supervised Learning Explained
slug: machine-learning-part-2-supervised
pub: 2019-01-21 07:43:27
authors: arj
tags: supervised learning, regression, classification
category: machine learning
related_posts: machine-learning-part-1-introduction,machine-learning-part-3-regression,supervised-learning

**Supervised learning** is a fundamental concept in machine learning where we have labelled data available. The machine "learns" from this data, much like a student learning from a teacher who provides the answers during the training process.

In this article, we will explore the different types of supervised learning, including classification and regression, and look at some common algorithms.

## Types of Machine Learning

*   **Supervised Learning** (Our focus today)
*   Unsupervised Learning
*   Reinforcement Learning

---

## What is Supervised Learning?

In supervised learning, algorithms are trained using labeled examples. This means the input data comes with the desired output. The learning algorithm receives a set of inputs along with the corresponding correct outputs, and the algorithm learns by comparing its actual output with correct outputs to find errors. It then modifies the model accordingly to improve accuracy.

There are two main categories of supervised learning problems:

### 1. Classification 🔖

Classification involves predicting a discrete class label. The output variable is a category, such as "spam" or "not spam," or "cat" vs "dog."

Common algorithms include:
*   **Logistic Regression** (Used for binary classification)
*   **k-Nearest Neighbors (k-NN)**
*   **Support Vector Machines (SVM)**
*   **Naive Bayes**
*   **Decision Trees**

### 2. Regression 📈

Regression involves predicting a continuous quantity. The output variable is a real value, such as "price," "temperature," or "weight."

Common algorithms include:
*   **Linear Regression** (Single value)
*   **Multivariate Linear Regression** (Multiple features)
*   **Polynomial Regression**

---

## Deep Dive: Classification

Let's look closer at **Logistic Regression**. Despite its name, it is a classification algorithm used to predict the probability of an object belonging to a certain class.

### Continuous vs. Discrete Values 🌀

To understand classification vs regression, you must understand the data types:
*   **Continuous values:** Infinite possibilities within a range (e.g., 1.1, 1.11, 1.112). Think of measuring weight or time.
*   **Discrete values:** Distinct, separate values (e.g., 1, 2, 3 or "Apple", "Orange"). Think of counting objects or picking categories.

**Example: Fruit Classification**

Imagine we have a dataset of fruit weights and we want to classify them as either **Watermelon (0)** or **Apple (1)**.

| Weight (kg) | Type (0=Watermelon, 1=Apple) |
| :--- | :--- |
| 9.5 | 0 |
| 10.0 | 0 |
| 0.1 | 1 |
| 9.4 | 0 |
| 0.2 | 1 |

We build a model based on this data. The model learns that light weights (around 0.1 - 0.2 kg) are likely Apples, and heavy weights (9+ kg) are likely Watermelons. If we then provide a new weight, say **10.4 kg**, the model will predict **0 (Watermelon)**.

---

## Supervised Clustering (k-NN)

k-Nearest Neighbors (k-NN) is a simple, intuitive algorithm. It assumes that similar things exist in close proximity. In other words, similar data points are "near" to each other on a graph.

**Example: Flower Classification 🌸**

Let's say we have data on flower petals:

| Petal Length | Petal Width | Type |
| :--- | :--- | :--- |
| 2 | 0.5 | A |
| 4 | 1 | B |
| 1.5 | 0.3 | A |
| 6 | 1.7 | B |

If we plot these on a graph, we see two distinct clusters. Now, suppose we find a new flower with **Length 5** and **Width 1.5**. 

By calculating the distance between this new point and its neighbors, we find it is much closer to the Type B cluster. Therefore, k-NN would classify it as **Type B**.

## Conclusion

Supervised learning is the most common form of machine learning today, powering everything from email filters to medical diagnosis systems. By understanding whether you are predicting a category (Classification) or a value (Regression), you can choose the right tool for your project.

In the next part, we will dive deeper into **Regression** and the math that makes it work!