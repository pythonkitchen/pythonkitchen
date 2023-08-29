title: Auto-differentiation and Autograd explained step by step
slug: automatic-differentiation-step-by-step
pub: 2022-11-15 14:34:00
authors: abdulkhan
tags: pythonmembers.club
category: algorithm and data structures,data science,machine learning

We will understand what is automatic differentiation for absolute beginners, although this concept requires a fair amount of theoretical understanding of derivatives and the chain rule, But don't worry I will try to explain in a very practical way, and we will build our knowledge one concept at a time and the end you will be able to compute painful calculus functions in seconds, This concept took me 7 - 8 days to comprehensively understand the importance and use cases in machine learning, so don't feel overwhelmed if you don't understand it even in your 10th attempted, Know this we are automating something which takes months for math graduate to understand!.



---


Table of content:
-----------------


* 1. Derivative
* 2. The Chain Rule
* 3. Auto differentiation
* 4. Behind the scenes of auto differentiation
* 5. Reverse mode autodiff
* 6. what can autodiff differntiatite


Derivative
----------


*A derivative is the instantaneous rate of change.*

I will try to help you understand the derivative with an example provided.

Let's say we have a graph x2.
![](https://qph.cf2.quoracdn.net/main-qimg-78715523fe6ed2e94c18fc96fb333ae9-lq)
###### d/dx [x^2] = 2x



The derivative of a function gives the slope at a single point.
If we plug in the x value of 2 into the derivative function, we get 4.

###### m = 4



The slope is defined as “rise over run” or the change in y divided by the change in x

Or

###### m=ΔyΔx


![](https://qph.cf2.quoracdn.net/main-qimg-99c8ad7d4050fd06e8a9231015581e6c-lq)

The problem with finding the slope of a singular point is that the change in y and the change in x is 0.

###### m=0/0



m is undefined, but that does not always mean that it doesn’t exist. We just have to try a different way. Newton and Leibniz created a different way to calculate slopes.

(If you don’t understand limits then you probably should study up on those before you start learning about derivatives)
![Autograd](//qph.cf2.quoracdn.net/main-qimg-41de61230502525630a1ac2c11535f1c-lq) "Autograd")

This is the limit definition of a derivative.

As h approaches 0, the change in y and x approaches 0.

I’ll do this with the function provided.

###### limh→ 0(x+h)2−x2h= limh→0x2+2xh+h2−x2h


###### limh→ 02xh+h2h= limh→0h(2x+h)h


###### limh→ 0(2x+h)



We can evaluate now.

###### 2x+0= 2x



Thus, our derivative.

The Chain Rule:
---------------



The rule applied for finding the derivative of the composite function (e.g. cos 2x, log 2x, etc.) is basically known as the chain rule. It is also called the composite function rule.

I understand the chain rule concept in this way:
![](https://qph.cf2.quoracdn.net/main-qimg-12a3a28a9283c105d116dd22ca9e474e)

Our objective is to go from A to C, we can either go directly and if it's not possible we have to go to a different point B which allows access to point C. Depending on the situation there can be more points B, D, and E….which we have to pass through in order to reach C.

So I think, for this situation, I can write

###### da/dc = (da/db • db/dc)



This is exactly your chain rule.

The way I understand it while problem-solving:

Try to focus on the outer function, and take the derivative. Move inside to the immediate next function, and take the derivative. Continue this process until there is nothing left to differentiate. Now, multiply everything you found altogether.

Let me give you a basic example:

###### f(x) = sinn (2x2 + x + 1)m


* Outer Function is sin **[(2x2 + x + 1)m]n**,
the function now resembles an xn format, take the derivative, and we get
**n sin^n−1(2x2+x+1)m**
* We move to the next function, which is **sin(2x2+x+1)m** , take the derivative
**cos(2x2+x+1)m**
* Next function, **(2x2+x+1)m** , take derivative
**m(2x2+x+1)m−1**
* Next function **(2x2+x+1)** , take derivative
**4x+1**


There are no more functions left to differentiate. Multiply all the derivative results you found.

We will get

**f′(x) = mn(4x + 1)(2x2 + x+1)m− 1sin^n−1(2x2 + x+1) mcos(2x2 + x+1)m**
Auto differentiation:
---------------------



Imagine you want to test out a new machine-learning model for your data. This usually means coming up with some loss function to capture how well your model fits the data and optimizing that loss with respect to the model parameters. If there are many model parameters (neural nets can have millions) then you need gradients. You then have two options: derive and code them up yourself or implement your model using the syntactic and semantic constraints of a system like Theano or TensorFlow.

I want to provide a third way: just write down the loss function using a standard numerical library like Numpy, and Autograd will give you its gradient.


```python
import autograd.numpy as np   # Thinly-wrapped version of Numpy
from autograd import grad

def taylor_sine(x):  # Taylor approximation to sine function
    ans = currterm = x
    i = 0
    while np.abs(currterm) > 0.001:
        currterm = -currterm * x**2 / ((2 * i + 3) * (2 * i + 2))
        ans = ans + currterm
        i += 1
    return ans

grad_sine = grad(taylor_sine)
print "Gradient of sin(pi) is", grad_sine(np.pi)

```


A common use case for automatic differentiation is to train a probabilistic model. Let me present a very simple (but complete) example of specifying and training a logistic regression model for binary classification:


```python
import autograd.numpy as np
from autograd import grad

def sigmoid(x):
    return 0.5 * (np.tanh(x / 2.) + 1)

def logistic_predictions(weights, inputs):
    # Outputs probability of a label being true according to the logistic model.
    return sigmoid(np.dot(inputs, weights))

def training_loss(weights):
    # Training loss is the negative log-likelihood of the training labels.
    preds = logistic_predictions(weights, inputs)
    label_probabilities = preds * targets + (1 - preds) * (1 - targets)
    return -np.sum(np.log(label_probabilities))

# Build a toy dataset.
inputs = np.array([[0.52, 1.12,  0.77],
                   [0.88, -1.08, 0.15],
                   [0.52, 0.06, -1.30],
                   [0.74, -2.49, 1.39]])
targets = np.array([True, True, False, True])

# Define a function that returns gradients of training loss using Autograd.
training_gradient_fun = grad(training_loss)

# Optimize weights using gradient descent.
weights = np.array([0.0, 0.0, 0.0])
print("Initial loss:", training_loss(weights))
for i in range(100):
    weights -= training_gradient_fun(weights) * 0.01

print("Trained loss:", training_loss(weights))

```

What going on behind the scenes?
--------------------------------



To compute the gradient, Autograd first has to record every transformation that was applied to the input as it was turned into the output of your function. To do this, Autograd wraps functions (using the function primitive) so that when they're called, they add themselves to a list of operations performed. Autograd's core has a table mapping these wrapped primitives to their corresponding gradient functions (or, more precisely, their vector-Jacobian product functions). To flag the variables we're taking the gradient with respect to, we wrap them using the Box class. You should never have to think about the Box class, but you might notice it when printing out debugging info.

After the function is evaluated, Autograd has a graph specifying all operations that were performed on the inputs with respect to which we want to differentiate. This is the computational graph of the function evaluation. To compute the derivative, we simply apply the rules of differentiation to each node in the graph.

Reverse mode differentiation
----------------------------



Given a function made up of several nested function calls, there are several ways to compute its derivative.

For example, given `L(x) = F(G(H(x)))`, the chain rule says that its gradient is `dL/dx = dF/dG * dG/dH * dH/dx`. If we evaluate this product from right-to-left: `(dF/dG * (dG/dH * dH/dx))`, the same order as the computations themselves were performed, this is called forward-mode differentiation. If we evaluate this product from left to right: `(dF/dG * dG/dH) * dH/dx))`, the reverse order as the computations themselves was performed, this is called reverse-mode differentiation.

Compared to finite differences or forward-mode, reverse-mode differentiation is by far the more practical method for differentiating functions that take in a large vector and output a single number. In the machine learning community, reverse-mode differentiation is known as 'backpropagation', since the gradients propagate backward through the function. It's particularly nice since you don't need to instantiate the intermediate Jacobian matrices explicitly, and instead only rely on applying a sequence of matrix-free vector-Jacobian product functions (VJPs). Because Autograd supports higher derivatives as well, Hessian-vector products (a form of second-derivative) are also available and efficient to compute.

What can Autograd differentiate?
--------------------------------



The main constraint is that any function that operates on a Box is marked as primitive, and has its gradient implemented. This is taken care of for most functions in the Numpy library, and it's easy to write your own gradients.

The input can be a scalar, complex number, vector, tuple, a tuple of vectors, a tuple of tuples, etc.

When using the grad function, the output must be a scalar, but the functions elementwise\_grad and jacobian allow gradients of vectors.

Conclusion
----------



In recent years many universities and schools have changed their teaching method from calculative and theoretical to geometrically intuitive and practical and autodiff is one of the most famous product of this, Rather than spending our energy on computing ridiculous arithmetic operations why not let the machine do it and you focus on inventing concepts and techniques in machine learning.

I hope this article helps you out, wish you the very best!

References:
-----------


* [Jon Krohn's autodiff with pytorch](https://www.youtube.com/watch?v=W-aiTln22cA "Jon Krohn's autodiff with pytorch")
* [videolectures.net](http://videolectures.net/deeplearning2017_johnson_automatic_differentiation/ "videolectures.net")
Auto differntiation



