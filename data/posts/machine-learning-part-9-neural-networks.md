title: Machine Learning Part 9: An Introduction to Neural Networks
slug: machine-learning-part-9-neural-networks
pub: 2021-04-07 10:10:40
authors: arj
tags: machine learning, neural networks, perceptron, deep learning, ai
category: machine learning

Neural Networks are the backbone of modern Artificial Intelligence, powering everything from face recognition to self-driving cars. In this post, we'll explore the basic building block of a neural network: the **Perceptron**.

## The Building Block: The Perceptron 🕸

The perceptron is a simplified mathematical model of a biological neuron. It takes multiple inputs, processes them, and produces a single output.

### How it Works:
1.  **Inputs:** Numerical values from your data.
2.  **Weights:** Every input has a weight that determines its importance.
3.  **Summation:** The perceptron multiplies each input by its weight and adds them up.
4.  **Activation Function:** The sum is passed through a function that decides whether the neuron "fires" (outputs a value).

### Example Calculation:
*   Inputs: $x_1 = 5, x_2 = 6$
*   Weights: $w_1 = 2, w_2 = 1$
*   Sum = $(5 \cdot 2) + (6 \cdot 1) = 16$

If our **Activation Function** says: "If sum > 10, output 1, else 0," then our perceptron outputs **1**.

---

## Adding the Bias 🎋

If all inputs are 0, the sum will always be 0, no matter what the weights are. To prevent this, we add a **Bias** input (usually a constant 1 with its own weight). This allows the neuron to "fire" even when all other inputs are zero.

## Training the Network 🎋

A Neural Network is just a large collection of these perceptrons organized in layers. When we "train" a network, we are actually adjusting the **weights** and **biases**.

1.  **Guess:** The network makes a prediction using random weights.
2.  **Calculate Error:** We compare the guess to the actual answer ($Error = Actual - Guess$).
3.  **Adjust:** We update the weights based on the error.
    $$New Weight = Weight + (Error \cdot Input \cdot Learning Rate)$$

The **Learning Rate** controls how much we change the weight in each step. Too high, and the model becomes unstable. Too low, and it takes forever to learn.

## Summary
Neural Networks learn by trial and error. By processing thousands of examples and constantly adjusting their weights, they can eventually "recognize" complex patterns that traditional algorithms can't.

## Exercise
Try to find a "Neural Network from scratch" tutorial in Python. You'll be surprised at how simple the math actually is for a single neuron!