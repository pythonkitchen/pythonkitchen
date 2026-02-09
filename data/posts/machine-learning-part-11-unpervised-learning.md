title: Machine Learning Part 11: Unsupervised Learning and Clustering
slug: machine-learning-part-11-unpervised-learning
pub: 2021-04-07 10:12:52
authors: arj
tags: machine learning, unsupervised learning, clustering, k-means
category: machine learning

So far, we've focused on Supervised Learning. Now, we enter the world of **Unsupervised Learning**, where the machine is given data without any labels and must find patterns on its own.

## What is Unsupervised Learning?

Unlike supervised learning, there is no "teacher" or "answer key." The algorithm looks at the input data and tries to find structure, such as grouping similar items together.

There are two main types:
1.  **Clustering:** Grouping similar data points.
2.  **Association:** Finding rules that describe your data (e.g., people who buy X also buy Y).

---

## Clustering with K-Means 🎲

The most popular clustering algorithm is **K-Means**. It aims to partition the data into **K** clusters.

### How it Works:
1.  **Initialize:** Randomly place K points called **Centroids**.
2.  **Assign:** Assign each data point to the nearest centroid.
3.  **Update:** Calculate the center (mean) of all points in each cluster and move the centroid to that new center.
4.  **Repeat:** Keep assigning and updating until the centroids stop moving.

### Measuring Success: SSE
How do we know if our clusters are good? We use the **Sum of Squared Error (SSE)**. This measures the total distance between every point and its assigned centroid. A lower SSE means the clusters are tighter and more accurate.

## Bisecting K-Means
If you want even better results, you can use **Bisecting K-Means**. It starts with one giant cluster and repeatedly splits the cluster with the highest SSE into two, until the desired number of clusters (K) is reached.

## Summary
Unsupervised learning is powerful for:
*   **Customer Segmentation:** Grouping customers by buying habits.
*   **Anomaly Detection:** Finding data points that don't fit into any cluster (potential fraud).
*   **Data Compression:** Representing a large dataset with a few cluster centers.

**Exercise:**
Look for a visualization of the K-Means algorithm online. Seeing the centroids "dance" into position makes the logic much clearer!