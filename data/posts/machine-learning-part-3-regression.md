title: Machine Learning part 3: regression
slug: machine-learning-part-3-regression
pub: 2019-01-23 07:38:19
authors: arj
tags: 
category: Uncategorized


**Machine Learning**




**♡ supervised learning**  
♡ unsupervised learning  
♡ reinforcement learning




**#3 supervised learning: regression**




note: **independent variables** are also called \*features\*




regression simply means prediction. there are many types of regression methods:




- simple linear regression  
- multivariate linear regression  
- polynomial regression  
- ridge regression  
- lasso regression




 🎁 **simple linear regression** means predicting for only two variables, a dependent and an independent one




let us say that we have many points on a graph of x,y and want to draw a line of best fit. we draw the line of best fit then we predict for further values of x and y. i.e. it calculates the values of m and c in **y = m \* x + c**




 🎁 : **multivariate linear regression** means predicting for one dependent variable and two or more independent variables




the formula is in the format 




ind. var. means independent variable 




stuff = m1 \* ind. var. 1+ m2 \* ind. var. 2 + ... + b




or 




stuff = m1\*feature1 + m2\*feature2 + ... + b




b is the intercept




many real world examples better fit with multivariate regression. like you might want to calculate fuel cost of trip based on many factors such as state of engine, age etc etc




we train our data to get the m1 m2 m3 etc then we can predict our target value for such and such situations




 🎁 **ridge regression**




definition of ridge:   
A ridge or a mountain ridge is a geological feature consisting of a chain of mountains or hills that form a continuous elevated crest for some distance.




just like the tops of mountains go up and down, similarly in the case where a graph's shape is like mountain tops, going up and down, ridge regression is used as a \*regularisation\* method to have a simple curve so as to ignore large coefficients and get better predictions




another name: tikhonov regularization




exercise:




1) dig into the maths of how   
i. linear regression works (how the line of best fit is drawn)  
ii. multivariate regression works  
iii. polynomial regression works




next:  
cost function and gradient descent





