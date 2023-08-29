title: Machine Learning part 5: mixed methods
slug: machine-learning-part-5-mixed-methods
pub: 2019-01-26 14:01:04
authors: arj
tags: 
category: machine learning




#5 mixed methods




Machine Learning




👉 ♡ supervised learning  
♡ unsupervised learning  
♡ reinforcement learning







types of supervised learning




✔ classification 🗒




✔ regression 📈




✔ mixed ⚗  
- tree based  
- random forest  
- neural networks  
- support vector machines




mixed methods are used for classification and regression.




🌱 tree based method




 those trees used for both for classification and regression are called Classification And Regression Trees (CART) models




let us say that we want to predict whether an event will be good or bad, the event being having a good day at school




our data looks as follows




t. represents teacher  
a means abscent  
p means present




mood stands for parents' mood  
g good. b bad




hwork means homework  
d done  
nd not done




t. | mood | hwork | result  
---------------------------------------  
a |      g    |       d    |      g  
p |      b    |       d    |      g  
a |      g    |     nd    |      g  
a |      b    |       d    |      b  
p |      b    |     nd    |      b  
a |      g    |     nd    |      g  
p |      b    |       d    |      g  
a |      g    |      nd   |      g  
a |      g    |       d    |      g




let us say that today the student entered the school. he wants to know how his day will go, today he has




t.           p  
mood   g  
hwork  nd




about splitting
---------------




the first step is to split the tree to get a high purity index




if we split by teacher's presence first, we get




a   
good 5 bad 1  
p   
good 2 bad 1




if we split by parents' mood we get




g  
good 5 bad 0  
b  
good 2 bad 2




if we split by homework done we get




d  
good 4 bad 1  
nd  
good 3 bad 1




the highest index of purity was with parents' mood with good 5 and 0 bad day




we start with it




mood  
--  g  
a |      g    |       d    |      g  
a |      g    |     nd    |      g  
a |      g    |     nd    |      g  
a |      g    |      nd   |      g  
a |      g    |       d    |      g




good 5 bad 0




-- b  
p |      b    |       d    |      g  
a |      b    |       d    |      b  
p |      b    |     nd    |      b  
p |      b    |       d    |      g




good 2 bad 2




so bad mood must be split further as good mood had 100% purity with 5 good result




now our condition is




t.           p  
mood   g  
hwork  nd




if we go for mood g, we can stop spliting as our purity is 100%. we'll get a good day




next:  
〰 enthropy and gain  
🌱 random forest  
🌱 support vector machines (SVM)  
🌱 neural networks



