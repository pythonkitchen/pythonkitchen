title: Machine Learning Part 6: Entropy and Information Gain
slug: machine-learning-part-6-enthropy-and-gain
pub: 2019-01-29 05:55:06
authors: arj
tags: machine learning, entropy, information gain, decision trees, math
category: machine learning

In the previous post, we saw how Decision Trees split data based on "purity." But how do we measure this purity mathematically? This is where **Entropy** and **Information Gain** come in.

## What is Entropy? 🎗

In machine learning, **Entropy** is a measure of impurity or randomness in a dataset. 

*   If a subset is **perfectly pure** (all items belong to one class), the entropy is **0**.
*   If a subset is **totally impure** (items are evenly split between classes), the entropy is **1**.

### The Entropy Formula
To calculate entropy ($H$) for a subset with two classes:
$$H = -(P_+) \log_2(P_+) - (P_-) \log_2(P_-)$$

Where:
*   $P_+$ is the probability of the positive class.
*   $P_-$ is the probability of the negative class.

### Example: Teacher's Presence
Recalling our "Good Day" example from Part 5, let's look at the "Teacher Present" split:

**Teacher Absent:** 5 Good (G), 1 Bad (B)
$$H(\text{absent}) = -(5/6) \log_2(5/6) - (1/6) \log_2(1/6) \approx 0.65$$

**Teacher Present:** 2 Good (G), 1 Bad (B)
$$H(\text{present}) = -(2/3) \log_2(2/3) - (1/3) \log_2(1/3) \approx 0.92$$

Since 0.65 is closer to 0 than 0.92, the "Absent" group is "purer" than the "Present" group.

---

## What is Information Gain? 🎗

**Information Gain** measures the reduction in entropy after a dataset is split on an attribute. We want to split on the attribute that gives us the **highest** Information Gain.

### The Formula:
$$Gain(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Entropy(S_v)$$

Basically: **(Entropy before split) - (Weighted average of Entropy after split)**.

If we calculate the gain for "Teacher Presence" in our 9-row dataset:
*   Total Entropy $H(S) \approx 0.76$
*   $Gain = 0.76 - (6/9 \cdot 0.65) - (3/9 \cdot 0.92) \approx 0.02$

A gain of 0.02 is quite low, suggesting that teacher presence isn't the most important factor in predicting a good day.

## Exercise
Calculate the Information Gain for "Parent Mood" from the dataset in Part 5. You'll find it is much higher!

In the next part, we will see how combining many decision trees creates a powerful model called a **Random Forest**.