title: Machine Learning Part 8: Support Vector Machines
slug: machine-learning-part-8-support-vector-machines
pub: 2021-04-07 10:08:14
authors: arj
tags: 
category: machine learning

#8 support vector machines

Machine Learning

👉♡ supervised learning
♡ unsupervised learning
♡ reinforcement learning

recap:
🔖 types of supervised learning

✅ classification 📑

✅ regression 📈

✅ mixed ⚗
- tree based
- random forest
- neural networks
- support vector machines 🎈

support vector machines (svm)

🔎 support vectors : read on to know

🔎 machine means model

support vector machines use hyperplanes to separate data. in a 2D plot, the line separating the data is called a separating hyperplane.

in 2D, a 1D hyperplane separates the data, in 1000D, a 999D hyperplane separates the data. so in N dimension, we need a hyperplane of N-1 dimension

🚂 on how to separate and how it shines

suppose whe have some data scattered on the right and some on the left. we can do something like averaging distances (best fit) and drawing a line but, if we consider that the farthest a point is from our separating line, the more confident we are that we got it right (if many points close to the boundary, we would doubt as whether we got it right or not).

svm makes use of this idea. it divides the data in such a way as to maximise the distance between the line (hyperplane) and the data lying closest to the line. 〰️ it might not be a straight line.

🚂 margin

the distance between the line and the closest coordinates is called margin. large margins make up for errors and limited data.

👉 🔎 support vectors are those points lying closest to the line (hyperplane) i.e. the closest coordinates

🚂 kernel trick

to separate complex shapes like a ring of data of type A surrounding data of type B appearing as a circle in the middle, SVM makes use of the kernel trick

the kernel trick transform inputs from a lower dimension (in 2D for example) to a higher dimension (like 3D) in a fashion that the data can ve separated. mostly used in non-linear problems

🚂 the maths behind

i plan to make a post about the maths behind but see the exercises if you want to get an idea beforehand

⚽️ exercise
1) google up
.. lagrange multipliers
.. platt’s smo algorithm

in relation to svm
