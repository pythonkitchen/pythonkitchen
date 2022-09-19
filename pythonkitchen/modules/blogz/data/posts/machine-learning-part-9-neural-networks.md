title: Machine Learning Part 9 Neural Networks
slug: machine-learning-part-9-neural-networks
pub: Wed, 07 Apr 2021 10:10:40 +0000

#9 neural networks

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
- neural networks 🎈
- support vector machines

neural networks

neural networks require a bit of explanation. entire books can be written on the subject

🕸 the perceptron

the perceptron was the basis for neural networks. it consists of two inputs, a processor and an output.

the processor is just a function that decides what to output according to the inputs. it might check if > a number or just check the sign or whatever

🕸 weight

the weight is just a value that we multiply the input by.

🕸 sum

we then sum the inputs \* weight and pass them to the function.

so we can see input -> weight -> function

🕸 example

let us say our two inputs are

input1 : 5
input2 : 6

let us have some random weights

weight1 : 2
weight2 : 1

let us sum

input1 \* weight1 + input2 \* weight2
5 \* 2 + 6 \* 1
16

let us say we configure our function as

def activation(sum):
 if sum > 10:
 return 0
 else:
 return 1

well, we just pass it to the activation function and it will return 1

⚽️ exercise:
1 find out the uses of neural networks (the fields)
hint: time series prediction, signal analysis ...

next:
the bias input and what need to be continued

...

#9 neural networks (continued)

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
- neural networks 🎈
- support vector machines

neural networks

🎋 bias input

in our example above let us say that we have input1 0 and input2 0, 0*weight1+0*weight2 will always be zero, no matter what the weight. because of this we add a permanent input of 1 so that it becomes 0*weight1+0*weight2 + 1\*weight3  weight3, in that case, the weight passes through the activation function

🎋 neural network

a neural network is a collection of perceptrons

🎋 training

whatever we wanted to do with a neural network, we must first adjust the weights as we gave it random weights at the begining. first we test the perceptrons agains inputs with known answer. we then compute the error (did it get the answer right or no). we then adjust weights according to the error. we repeat

🎋 error

our error is
desired output - guess output

🎋 tuning weight

our new weight equals
weight + change in weight

change in weight = error \* input

so,

new weight = weight + error \* input

🎋 learning constant

to decide at what rate we change our weight, we just use a value called learning constant. too large and we won't tune our weight correctly. too little and ... it takes a long time

new weight = weight + error \* input \* learning constant

⚽️ exercise:
read implementations of neural networks from scratch in python
