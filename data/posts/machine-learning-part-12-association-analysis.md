title: Machine Learning Part 12: Association Analysis Explained
slug: machine-learning-part-12-association-analysis
pub: 2021-04-07 10:14:26
authors: arj
tags: machine learning, unsupervised learning, association analysis, apriori
category: machine learning

**Association Analysis** is an unsupervised learning technique used to discover interesting relationships hidden in large datasets. It's most famous for its use in "Market Basket Analysis."

## The Goal 🛒

Imagine you own a grocery store. You want to know which items are frequently bought together. If you find that customers who buy bread also tend to buy butter, you can place them next to each other to increase sales.

### Key Terms:
*   **Itemset:** A collection of one or more items (e.g., {Bread, Milk, Butter}).
*   **Support:** How frequently an itemset appears in the dataset.
*   **Confidence:** How often item Y is bought when item X is bought.

---

## Measuring Strength: Support, Confidence, and Lift ✳

### 1. Support
The percentage of total transactions that contain the itemset.
$$Support(A) = \frac{\text{Number of transactions containing A}}{\text{Total transactions}}$$

### 2. Confidence
The likelihood that item B is purchased given that item A is purchased.
$$Confidence(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A)}$$

### 3. Lift
Lift measures how much more likely item B is to be bought given item A, compared to how often B is bought anyway.
$$Lift(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A) \cdot Support(B)}$$

*   **Lift = 1:** A and B are independent.
*   **Lift > 1:** A and B are positively associated (A makes B more likely).
*   **Lift < 1:** A and B are negatively associated.

---

## The Apriori Algorithm ✳

Checking every possible combination of items in a large store would be incredibly slow. The **Apriori Algorithm** simplifies this by using the "Apriori Principle":

> **If an itemset is frequent, then all of its subsets must also be frequent.**

This allows the algorithm to "prune" (skip) thousands of combinations that couldn't possibly be frequent, making the analysis much faster.

## Summary
Association analysis helps businesses understand customer behavior and optimize store layouts, recommendation engines, and marketing campaigns. 

**Exercise:**
Look up **"Market Basket Analysis"** examples. You'll find interesting (and sometimes weird) stories about items people frequently buy together!