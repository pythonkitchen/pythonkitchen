title: Machine Learning Part 11 Unpervised Learning
slug: machine-learning-part-11-unpervised-learning
pub: Wed, 07 Apr 2021 10:12:52 +0000

#11 unsupervised learning

Machine Learning

♡ supervised learning
👉 ♡ unsupervised learning
♡ reinforcement learning

unsupervised learning is where your program has to find how the data relates to each other. there is no prior training

types of unsupervised learning

♠️ clustering
♠️ association

🎲 clustering

the k means (the distance-based) algorithm is used to try to classify the data into clusters. it will find k clusters (k is the number the user provides). the centroid defines a cluster.

🔎 centroid is a point at the center of the cluster

🎲 the how

first the centroids are randomly assigned. next each point in our dataset are assigned to a cluster. this is done by measuring nearness to the centroids. next the centroid locations are themselves updated by taking the mean value of points in the cluster

🎲 the SSE

how good was our clustering? by using the Sum of Squared Error. it is the sum of the difference between a point and the mean point in the cluster. a lower SSE means that points are closer to their centroids meaning you've got it right. we can split clusters with higher SSE into two clusters

🎲 bisecting k means

one way to increase our clustering is to use the bisecting k means method. we choose rhe cluster with the largest SSE, split and repeat until you get the required number of clusters

⚽️ exercise

see an implementation in python
