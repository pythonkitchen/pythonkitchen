title: Machine Learning part 2: supervised learning
slug: 432
pub: 2019-01-21 07:43:27
authors: arj



Machine Learning




**♡ supervised learning**  
♡ unsupervised learning  
♡ reinforcement learning




**#2 supervised learning**




in supervised learning we have labelled data available. the machine just see and do as we do.




types of supervised learning 




  
✅ classification 🔖 :  
- logistic regression  
- supervised clustering




  
✅ regression 📈   
- linear regression (single value)  
- multivariate linear regression




  
✅ mixed ⚗  
- tree based  
- random forest  
- neural networks  
- support vector machine




  
✅ **classification** 🔖 :




- **logistic regression**




classifying data into categories. instead of predicting continuous values, we predict discrete values. 




 *continuous and discrete values* 🌀 




continuous values means if you have y = mx + c, you can have y for x: 34, x:34.1, x:34.12 etc, as much as you want. discrete values means the next value after a is b then c etc




to sum it, there are two ways to see counting. one is you say: 1 2 3 4 (discrete), and one you see infinity between 1 and 2 like 1.1, 1.11, 1.111111 etc (continuous)




logistic : the careful organization of a complicated activity so that it happens in a successful and effective way




regression means prediction




le us say we have a table of watermelon 🍉 and 🍎 apple weights. let us put a 0 for watermelon and a 1 for apple




our data in kg/(0,1) :




9.5 | 0  
10.0 | 0  
0.1 | 1  
9.4 | 0  
0.2 | 1  
etc




we build a model according to our data. so, light weights (0.1 to 0.2) seem to be 1 and heavy (10 to 11) seems to be 0. that's our model.




now we throw in a weight, let us say 10.4, it will pass it in the model and say 0. 




- **supervised clustering methods (kNN)**




well that is a kmeans method. let us say we have some data  
:cherry\_blossom:




petal - plant type




length | width | type  
--------------------------------  
2 | 0.5 | A  
4 | 1 | B  
1.5 | 0.3 | A  
6 | 1.7 | B




let us have a sample of petal length 5 and petal width 1.5 and we want to say if it's of type A or B. if we plot the graph, we can see two points (a cluster) at the bottom left corner and two points (another cluster) at the top right corner. 5,1.5 is nearer to the top right corner, hence type B




but how do we define near? near is by distance. we calculate distance 📏 between each coordinate and if it is nearer to more type B, we say it is of type B. now we can add more data and they will thus be classified




next:




**regression**



