title: Machine Learning part 7: Random Forests Explained
slug: machine-learning-part-7-random-forests-explained
pub: Sun, 03 Feb 2019 13:00:39 +0000
authors: Abdur-RahmaanJ



#7 random forest




Machine Learning




π β‘ supervised learning  
β‘ unsupervised learning  
β‘ reinforcement learning




recap:  
π types of supervised learning




β classification π




β regression π




β mixed β  
- tree based   
- random forest π  
- neural networks  
- support vector machines




π³ overfitting and the problem with trees




trees classify by drawing square boxes around the data, which does not work well where many separations are needed. it overfits the data




π³ pruning




pruning means to trim (a tree, shrub, or bush) by cutting away dead or overgrown branches or stems (or unwanted parts), especially to encourage growth.




for example, if you had a single data (a leaf) that is making your square a large one, so you just remove it so that the tree still maintains relevence. improves accuracy of the tree.




π³ random forests




just like a forest is made up of trees, similarly random forest is a machine learning method made up of tree methods. random as it randomises the input of the trees.




the basic form of it acts on tally. a tree gives out an output, this one collects all the outputs of the trees and try to make up an answer. if 10% of trees said A and 90% said B, it will say B (majority). much like you ask questions to 10 people as to what book they think will be most popular this year or what team will win. just here as theΒ  inputs are randomised, each trees are not the same. it might be further tweaked to give more or less meanings to the answers in the tree.




π³ use of random forests




used to identify customer type, whether people will like a product or predict behaviour.




β½ exercise  
1) dig more into the uses of random forests  
2) compare it's implementation across languages ( with libs included ), how elegant you think python is?




next:  
π± support vector machines#8 support vector machines 



