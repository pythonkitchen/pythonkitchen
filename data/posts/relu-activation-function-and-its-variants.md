title: ReLU Activation Function and Its Variants
slug: relu-activation-function-and-its-variants
pub: 2022-12-13 11:23:46
authors: parthshukla
tags: activations functions,relu
category: machine learning

Activation functions in deep learning are the functions that decide the output from node or hidden layers from a given set of inputs in neural networks. There are many activation functions used in deep learning but among all of them rectified linear unit or ReLU is the widely used activation function in almost all deep learning neural networks.

Table of Content
----------------


1. ReLU Activation Function
2. Dying ReLU Problem
3. Variants of ReLU
4. Leaky ReLU (LReLU)
5. Parametric ReLU (PReLU)
6. Exponential Linear Unit (ELU)
7. Scaled Exponential Linear Unit (SELU)
8. Conclusion


ReLU Activation Function
------------------------



The full form of the term ReLU is the rectified linear unit. ReLU is the activation function that is most widely used in neural network architectures.

The equation for the ReLU activation function is:

F(x) = max(0,x)

which tells that if the input x is less than zero then the output from the function will be zero and if the input given to the relu function is greater than zero then the output from the function will be the same as the input.
![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu1-300x169.png)
[Image Source](https://www.google.com/search?q=relu+activation+function+graph&tbm=isch&ved=2ahUKEwiUzP2WxOn6AhU-iNgFHexiC-sQ2-cCegQIABAA&oq=relu+activation+function+graph&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BAgjECc6BwgAEIAEEBhQmBBY5xVguhdoAHAAeACAAcICiAHgCZIBBzAuNC4xLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=53pOY9S8IL6Q4t4P7MWt2A4&bih=579&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=NbAH97YJC7mO9M "Image Source")
Dying ReLU Problem
------------------



Due to the formula of the ReLU activation function, all the values less than zero will be zero after passing through the ReLU function. If the neural network is having a lot of negative values in the dataset then they all will be converted to zero after passing through the ReLU activation function and there will be zeros in the output which will make the neurons inactive. This type of scenario is called the dying ReLu problem in neural networks.

![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu2-300x170.png)
[Image Source](https://miro.medium.com/max/1400/1*r_fTwA86CGc6iqFQlVjZ-g.png "Image Source")
In the above image, we can see that all of the negative values passing through the ReLU activation function will be converted to zero and there will be a straight line in the graph of the function on the negative x-axis.

Variants of ReLU
----------------



To solve the dying ReLU problems in the neural networks there are some other variants of the ReLU activation function that is developed, which do not face dying ReLU or dying neurons problem.

1. Leaky ReLU (LReLU)
---------------------



The first and easiest variant of the ReLU activation function is leaky ReLU. there is only a little change in the formula of the normal ReLu activation function which solves the problem of dying ReLU.

The formula for the Leaky ReLU activation function is

F(x) = max(0.01x, x)

So according to the leaky ReLU if the input passes to the activation function are less than zero then the output value would be 0.01 times the input values and if the input passes to the activation function is greater than zero the output values will be equal to the input value.
![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu3-300x177.png)
[Image Source](https://www.researchgate.net/publication/358306930/figure/fig2/AS:1119417702318091@1643901386378/ReLU-activation-function-vs-LeakyReLU-activation-function.png "Image Source")
2. Parametric ReLU (PReLU)
--------------------------



Parametric ReLU is similar to the leaky ReLU activation function, but here instead of having a predetermined value for multiplying the input values with 0.01, we use the parameter "a" in parametric ReLU. The value of the "a" parameter will be decided by the neural network itself.

The formula for Parametric ReLU is

F(x) = max(ax, x)

which stated that if the input value given to the parametric RELU is less than zero then the output values will be equal to the input values multiplied with parameter "a" and if the input value if greater than zero then the output value will be the same as the input value.
![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu4-300x266.png)
[Image Source](https://cdn-images-1.medium.com/max/800/0*ChdsWvPFTyZ8kbbR.png "Image Source")
3. Exponential Linear Unit (ELU)
--------------------------------



The exponential linear unit is a variant of ReLU activation which fixes some problems and gives some advantages compared to the normal ReLU activation function.

The formula for Exponential Linear Unit is
![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu5.png)
[Image Source](https://www.v7labs.com/blog/neural-networks-activation-functions "Image Source")
ELU activation function uses a log curve and due to this it does not gives a straight line for negative values, unlike leaky and parametric ReLU.

ELU activation functions also solve the dying ReLU problem and also the curve of the ELU becomes smooth slowly for negative values having high magnitude while normal Relu becomes smooth instantly.

![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu6-300x192.png)
[Image Source](https://www.google.com/search?q=elu+activation+graph&rlz=1C1CHBD_enIN933IN933&sxsrf=ALiCzsbSAcYfWuUzgQ7eUq9stJh4AhC8qQ:1666090389003&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiM9LKuzun6AhUb43MBHTytBx8Q_AUoAXoECAEQAw&biw=1220&bih=579&dpr=1.12#imgrc=fabozd3VMZV4KM "Image Source")
Higher computational powers are required while working with ELU compared to ReLU and there is a chance of exploding gradient problems while working with ELU.

4. Scaled Exponential Linear Unit (SELU)
----------------------------------------



This activation function is one of the latest activation functions in deep learning. The equation for this activation function just looks like the other equations. The equation for this activation function is
![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu7-300x61.png)
[Image Source](https://www.google.com/search?q=selu+activation+formula&tbm=isch&ved=2ahUKEwitk8y6zOn6AhW1j9gFHXh3Bt0Q2-cCegQIABAA&oq=selu+activation+formula&gs_lcp=CgNpbWcQAzIECCMQJ1D6F1j6F2DEGGgBcAB4AIAB2gGIAdoBkgEDMi0xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=lYNOY-30KrWf4t4P-O6Z6A0&bih=579&biw=1204&rlz=1C1CHBD_enIN933IN933&hl=en-GB#imgrc=78l7EbscdBRa0M "Image Source")
The equation states that, if the input value x is greater than zero, the output value becomes x multiplied by lambda λ term and If the input value x is less than or equal to zero then alpha is multiplied with the exponential of the x-value minus the alpha value, and then we multiply by the lambda value.

The calculated values for alpha and lambda are

Alpha = 1.6732632423543772848170429916717

Lambda = 1.0507009873554804934193349852946

![](https://pythonkitchen.com/wp-content/uploads/2022/12/relu8-300x200.png)
[Image Source](https://www.google.com/search?q=selu+activation+graph&tbm=isch&ved=2ahUKEwi5hcLYz-n6AhU8k9gFHZlaCqwQ2-cCegQIABAA&oq=selu+activation+graph&gs_lcp=CgNpbWcQAzoECCMQJ1DPB1iJEGDpEWgAcAB4AIAB5wGIAZkJkgEFMC40LjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=-YZOY_mkLrym4t4PmbWp4Ao&bih=579&biw=1204&rlz=1C1CHBD_enIN933IN933&hl=en-GB#imgrc=qJPE_mBWQXNMSM "Image Source")
The special case in the SELU activation function is that it is self normalizing activation function, which means that the input value will be passed through an activation function and the output from the function will be normalized by subtracting the mean from the value and diving it by its standard deviation. By doing this means centralizing will take place and the value of the mean will be zero and the standard deviation will be equal to 1.

Conclusion
----------



In this article, the ReLU activation function is discussed with its core mathematics behind it with dying ReLU problems and variants of ReLU like PReLU, LReLu, ELU, and SELU. Knowledge about the ReLU activation function and its variants will help one to understand its core intuition of it and will be able to differentiate between other variants of ReLU and their need of them.

Some **Key Insights** from this article are

1. ReLu is the most widely used activation function with the low computational power required for its use.
2. Dying ReLU is a problem associated with the Normal ReLu activation function due to its nature of converting negative values to zero.
3. Leaky ReLu and Parametric ReLu are the variants of Relu having linear negative x-axis graph in which some value is multiplied by input value if its negative to avoid dying ReLU problem.
4. ELU and SELU are the variants of the Normal RelU activation function having nonlinear graphs for negative x-axis value with high computation power required and advantages like self-normalizing etc.

