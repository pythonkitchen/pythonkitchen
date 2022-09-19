title: Machine Learning part 4: Gradient Descent and cost function
slug: machine-learning-part-4-gradient-descent-and-cost-function
pub: Thu, 24 Jan 2019 14:00:21 +0000


**#4 gradient descent and cost function**




Machine Learning




👉 ♡ supervised learning  
♡ unsupervised learning  
♡ reinforced learning




**☄ cost function**
-------------------




cost function is also called mean squared error. 




well mean means sum of elements / number of elements. here we take the sum of all squared errors




(error1 ^ 2 + error2 ^ 2 + error3 ^ 2)/3




/3 as there are 3 errors




we define error as the difference in y between your point and the y on thwline you are trying to fit




-> y predicted - y on line  
-> y predicted - m\*x on line + c




☄ gradient descent
------------------




wikipaedia defines gradient descent such:




Gradient descent is a first-order iterative optimization algorithm for finding the minimum of a function.




well first, that has nothing specific to machine learning but concerns more maths




iterative means it repeats a process again and again  
the minimum of a function is the lowest point of a u shape curve




in machine learning it means finding the line of best fit for a given training data




if you plot cost v/s m or cost v/s c you'll get a u shape graph




☄ the aim
---------




when you plot the above graph, the minimum is the point where the error is the lowest (that's when you get the line of best fit). now, how exactly do you find it? 




☄ the how
---------




well you plot either of the above graphs i.e. cost versus m or cost versus b and you find the minimum by checking the gradient at each point. at the minimum the gradient is 0 (gradient of straight line)




for the curve, you apply calculus to get the gradient function.




☄ about steps
-------------




well when you start, you need to check the gradient after an interval of c. when we see the gradient rising again we know we've found our minimum.




too small an interval of c (step) and your program might run too long




too big an interval of c and you miss your minimum




⌨ the code





```python

import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)

```



🗒 notes




md means derivative (gradient) of m




the above calculates the m and c to get the right amount to find the relationship between 1 and 5, 2 and 7 etc (see array in code) 




⚽ exercise:  
1. google up stochastic gradient descent




code credits: code basics





