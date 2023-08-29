title: Decoding Symmetric Indefinite Matrices In Python
slug: decoding-symmetric-indefinite-matrices-in-python
pub: 2022-10-18 06:35:29
authors: abdulkhan
tags: 
category: data science,machine learning

This article is a gentle introduction to symmetric indefinite matrices in Python

Table of content
----------------


* What are symmetric indefinite matrices andwhere are they used?
* Implementing symmetric indefinite matrices (SYMMQL) in python
* Comparing convergence rate of SYMMLQ, CG (Conjugate Gradient), and MINRES by solving the following classical symmetric indefinite system


What are symmetric indefinite matrices and where are they used?
---------------------------------------------------------------



A matrix is symmetric indefinite if it is symmetric and has both positive and negative **eigenvalues**. Symmetric Indefinite matrices are a crucial class of matrices since its used for Fine-Tuning in-built algorithms or creating one from scratch. Available in many applications. To name a few: this class of matrices appears in Newton's methods for the unconstrained/constrained [optimization algorithms](https://www.sciencedirect.com/topics/mathematics/unconstrained-optimization), [penalty function](https://en.wikipedia.org/wiki/Penalty_method), methods for nonlinear programming, and in discretized incompressible [Navier{Stokes equations}](https://www.sciencedirect.com/science/article/pii/S0021999120305647). Apart from arising intrinsically in applications, symmetric indefinite matrices are also created from definite ones because of errors in measuring or computing the matrix elements.

As of now, there's no method of directly dealing with Symmetric Indefinite matrices in Python. People either use the (MINRES) Minimal Residual method or (LSQR) Least Square Root method for working/manipulating symmetric indefinite matrices which is very inconvenient for users. This was a Major deficiency of Python as it cannot meet the demands of professionals who use symmetric indefinite matrices in mechanics, computer science, or ML researchers who find innovative ways to enhance current systems to the next level.

Implementing symmetric indefinite matrices (SYMMQL) in python
-------------------------------------------------------------



SYMMQL is widely used in programming languages like MATLAB, PETSc, Trilinos, and PyKrylov. For python, The idea of implementing a method(SYMMQL) that keeps up the pace and doesn't compromise the optimization was initially proposed by [C.C.Paige](https://scholar.google.com/citations?user=iTzCWMwAAAAJ&hl=en) and [M.A.Saunders](https://web.stanford.edu/~saunders/) back in 1998. But due to some unknown reasons, It was not carried out.
 By the way, [here](https://github.com/PythonOptimizers/pykrylov/blob/master/pykrylov/symmlq/symmlq.py) There is a Python version of this algorithm, but the library seems to be deprecated, and also it is licensed under LGPL, Hence it was not adopted in python as well.

This year(2022) [Gang Zhao](https://github.com/scipy/scipy/pull/16202) picked up this idea and made a PR to make this implementation. But I think the PR is not fully adapted because the following tests were conducted to merge this method into SciPy. However, 13 out of 23 failed :
[See the tests](https://github.com/scipy/scipy/pull/16202/checks?check_run_id=6709247274)
Comparing convergence rate of SYMMLQ, CG (Conjugate Gradient), and MINRES by solving the following classical symmetric indefinite system
----------------------------------------------------------------------------------------------------------------------------------------



Here's some prototype code:


```python
    import numpy as np
    from scipy import sparse

    # Building coefficient matrix `A`
    n = 50
    mu = np.sqrt(3.)
    data = np.zeros((3, n))
    data[0, :] = 2.
    data[1, :] = -1.
    data[2, :] = -1.
    sp = sparse.spdiags(data,[0, -1, 1],
     n, n, format='csr')
    A = sp @ sp
    muI = mu * sparse.eye(n)
    A -= muI

    # Building R. H. S. `b`
    b = np.ones(n)

```


The convergence rate is as follows:
![屏幕截图 2022-05-19 185218](https://user-images.githubusercontent.com/31978442/169277269-abcb40ff-b03a-4387-a8cb-59f2109dc319.png)

And CPU time is as follows:
![2022-05-19 16-26-34 的屏幕截图](https://user-images.githubusercontent.com/31978442/169277587-425bedc5-3d11-42e1-b1b2-fd669194690e.png)
For a symmetric indefinite system, compared with CG, SYMMLQ has a smoother convergence curve and better convergence rate. I believe SYMMLQ can replace MINRES to get almost the same performance.

Conclusion
----------



There's almost no information available on the internet regarding symmetric indefinite matrices. There are only scholarly articles written decades ago. This topic is very underrated compared to other concepts of ML or computer science. I presume the main reason for that is because it requires substantial knowledge of Linear Algebra + computer science. I hope there will be someone taking the Big leap forward in this.

References
----------


* [scipy-dev](https://mail.python.org/archives/list/scipy-dev@python.org/thread/NA7XKDBXXSI4I3RIPZKUEWAACT4Z2QVN/)
* [scipy-github](https://github.com/scipy/scipy/pull/16202)

