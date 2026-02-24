title: Machine Learning Part 10: Naive Bayes Classification
slug: machine-learning-part-10-naive-bayes
pub: 2021-04-07 10:11:56
authors: arj
tags: probabilistic models, bayesian, classification
category: machine learning
related_posts: adaboost-vs-naive-bayes-algorithms-in-machine-learning,machine-learning-part-1-introduction,supervised-learning

Naive Bayes is a simple yet powerful classification algorithm based on **Bayes' Theorem**. It's particularly popular for text classification and spam filtering.

## Bayes' Theorem ⚱

The heart of this algorithm is Bayes' Theorem, which describes the probability of an event based on prior knowledge of conditions that might be related to the event.

$$P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)}$$

In machine learning terms, we can think of this as:
$$P(\text{Class} | \text{Data}) = \frac{P(\text{Data} | \text{Class}) \cdot P(\text{Class})}{P(\text{Data})}$$

### Why "Naive"?
The algorithm is called "Naive" because it assumes that all features are **independent** of each other. In reality, features are often related (e.g., if you see "Machine" and "Learning" in a text, they aren't independent), but despite this "naive" assumption, the algorithm works surprisingly well!

---

## Example: Are you ill? 🤒

Imagine a new rare disease called "Scarius." You have a fever—what is the probability you actually have Scarius?

*   **P(Scarius):** The probability of having the disease (it's rare: 0.0001).
*   **P(Fever | Scarius):** The probability that you have a fever if you have the disease (let's say 0.96).
*   **P(Fever):** The probability that any random person has a fever (let's say 0.1).

**Calculation:**
$$P(\text{Scarius} | \text{Fever}) = \frac{0.96 \cdot 0.0001}{0.1} = 0.00096$$

Even though you have the symptom, the probability you have this specific rare disease is still less than 0.1%! This shows why considering the "Prior" ($P(B)$) is so important.

## Summary
Naive Bayes is:
*   **Fast:** It requires a small amount of training data.
*   **Scalable:** It handles high-dimensional data well.
*   **Effective:** Great for things like spam detection or sentiment analysis.

## Exercise
Try to derive Bayes' Theorem using a Venn diagram. It's a great way to visualize how conditional probability works!