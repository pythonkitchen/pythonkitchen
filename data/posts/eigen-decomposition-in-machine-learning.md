title: Eigen Decomposition in Machine Learning
slug: eigen-decomposition-in-machine-learning
pub: 2023-02-01 11:33:43
authors: parthshukla
tags: data science,eigen decomposition,linear algebra
category: data science,machine learning

Matrix decomposition in linear algebra is one of the most valuable techniques for reducing the matrix into smaller parts. In matrix decomposition, the eigendecomposition is a fundamental concept that decomposes the matrix in **eigen values and eigen vectors**. This type of **decomposition** technique plays an essential role in techniques like Principle component analysis where there is a need for dimensionality reduction of the data.

In this article, we will discuss **eigen decomposition** and eigen values and eigen vectors, their core intuition, and some of the application parts of the same. This will help one understand the concept from the very level to the required knowledge of the concept in data science.

Table of Contents
=================


* Eigen Decomposition
* Eigen Values and Eigen Vectors
* Mathgematicqal Undersatnding of the - Eigen Equaltion
* Applications of the Eigendecomposition
* Key Takeaways
* Conclusion


Eigen Decomposition
===================



Eigendecomposition is a type of technique that is used to decompose the given matrix into **eigenvalues and eigenvectors**. Eigendecomposition is one of the most widely used **matrix decomposition** techniques due to its accuracy and reliability.

A mathematical expression for eigendecomposition is as follows:



> AV = Lambda V


Where,

> A = Matrix that is to be decomposed

> V = EigenVector 

> Lambda = EigenValue

A question might come into your mind why is the eigen decomposition needed, what is the need for decomposing it?

Well, a very straight answer to this question is for better analyzing a matrix. Same as when we **decompose** integer values or any dataset, the reduced size of the same helps us analyze it better, the same way the eigen decomposition can help us analyze the matrix and its behavior properly.

**Decomposition** a matrix with eigen values and eigen vectors can help us analyze the properties of the matrix like rank and power, more easily and efficiently.

Eigen Values and Eigen Vectors
==============================



In matrix operations, some of the **linear transformations** are applied to the data, to convey the data into the right format or in case of analyzing it. Now as we know that eigen values and eigen vectors are also part of the matrix, so whenever the linear transformation will be applied to the matrix, the values and direction of the vectors in the matrix can change. But some of the vectors are there whose direction does not change, only the magnitude can be changed.

Basically, eigenvectors are those vectors whose direction does not change after applying the linear transformation, the values of the **magnitude** only changes. And the eigenvalues are the values or the coefficient with which the value of the vector changes.

![](/assets/ed1.jpg)
[Image Source](https://www.google.com/search?q=eigen+values+and+eigen+vectors+img&rlz=1C1CHBD_enIN933IN933&sxsrf=AJOqlzV17WsKybgOPhWzhEKqoR6LmYQcGg:1675040453445&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjs4dj5i-78AhWu7jgGHXe0AvQQ_AUoAnoECAIQBA&biw=1220&bih=547&dpr=1.12#imgrc=sc0AR-N2iuLZHM "Image Source")

> AV = Lambda V

As we can see in the above expression that v is represented as the eigenvector whose **direction** will **not** change after linear transformations and the Lambda is a coefficient that is eigenvalues according to which the value or the magnitude of the eigenvector will change.

Sometimes the Eigenvectors are also known as the true or right vectors. Here note that if the value of the eigenvalue is negative it will reverse the direction of the eigenvector but the line on which the vector is lying will be the same.

Mathematical Understanding of the Eigen Equation
================================================



As we discussed above that the mathematical expression for the eigendecomposition is

> AV = Lambda V


Now to understand it better, we can consider a simple matrix on which **linear transformation** is applied to transform the values of the matrix due to some purpose.

Now here the v is an eigenvector that is multiplied to the matrix A. the values that we will get will be the same as we multiply the vector with a coefficient Lambda, which is the designed value.

That basically means that the eigenvalues will decide the magnitude or the length of the vector to change and to what extent. Although the direction of the vector will be the same only, positive or negative.

Calculating Eigen Values and Vectors
We can easily perform the eigen decomposition on a matrix with using NumPy and **eig()** functions.

Let us try to find the eigen values and eigen vectors of a matrix with code examples.


```python
#eigendecomposition
from numpy import array
from numpy.linalg import eig
#matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#eigendecomposition
Eig(A)= values, vectors
print(vectors)
print(values)

```

Applications of Eigen Decomposition
===================================



There are many applications of the eigendecomposition here it is very useful and outperforms some of the existing algorithms as well. Let us discuss them one by one.

### Principle Component Analysis


Principle component analysis or the PCA is one of the widely used methods for **dimensionality reduction** of the given dataset. The PCA technique uses eigen decomposition to find the eigen values and eigen vectors from the dataset and then transforms the data and results in a principle components which help in reducing the dimensionality of the data.

Here the covariance matrix is prepared first for the dataset and then the **eigenvalues and eigenvectors** are calculated. These vectors and their **coefficients** or values help to find the best possible principle components that can represent the whole data in a less dimensional format.

### Google Page Rank


**Eigendecomposition** techniques are also used in google page ranks where the algorithms rank pages according to the interest and previous clicks of the user. Although only eigendecomposition can not help rank a billion pages, yes it can be used with some other algorithms.

### Clustering Techniques



A very popular clustering technique like K Means also fails in some cases where there is a high number of dimensions in the data. In such cases, spectral clustering techniques can be used to find the **K** clusters from the data with the help of **eigenvectors and Eigenvalues**.

Key Takeaways
=============


* Eigendecomposition is a technique in which the matrix is **decomposed** in eigenvalues and Eigenvectors.
* Eigenvectors are a type of vector whose values changes but the **direction** remains the same, after applying the linear transformation.
* Eigenvalues are the coefficient or the rate at which the value or the **magnitude** of the vector will change.
* The **eigendecomposition** can help in techniques like PCA, google page rankings, and clustering algorithms.


Conclusion
==========



In this article, we discussed the eigendecomposition and Eigenvalues and eigenvectors with their core intuitions, mathematical expression, and applications. This will help one to understand the concept of eigendecomposition better and will be able to relate the application of the same.
