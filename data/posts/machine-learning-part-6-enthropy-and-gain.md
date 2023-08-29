title: Machine Learning part 6: enthropy and gain
slug: machine-learning-part-6-enthropy-and-gain
pub: 2019-01-29 05:55:06
authors: arj
tags: 
category: machine learning


Machine Learning




👉 ♡ supervised learning  

♡ unsupervised learning  

♡ reinforcement learning




recap:  
 🔖 types of supervised learning




✔ classification 📑




✔ regression 📈




✔ mixed ⚗




* tree based :balloon:
* random forest
* neural networks
* support vector machines




🎗 enthropy




enthropy is just another word for expected value




in the past post, we decided what to use to split based on purity index. we can do the same thing mathematically (easier) by




P+ means probability of target (good day in our case)  

P- means probability not target (bad day)




log2(P-) means log(P-) base 2




H = -(P+)log2(P+) - (P-)log2(P-)




the above is the formula for the purity of subset. it measures how likely you get a positive element if you select randomly from a particular subset




let us take teacher's presence. we had




absent  

good 5 bad 1  

present  

good 2 bad 1




H(absent) = -(5/6)log2(5/6) - (1/6)log2(1/6)  

= 0.65




H(present) = -(2/3)log2(2/3) - (1/3)log2(1/3)  

= 0.92




0 is extremely pure and 1 is extremely impure




so absent is purer than than present




🎗 gain




gain is used to determine what to split first by finding the feature with the highrst gain. 0 means irrelevent. 1 means very relevent




gain is defined by




gain = H(S) − Σ (SV/S) H(SV)




S -> total number of points in leaf  

v is the possible values and SV -> subset for which we have those values  

H is our enthropy as above




taking for presence, our gain is




our S is 9 that is (6+3)




gain = H(presence) - sum( SV/9 \* H(SV))  

gain = H(presence) - (6/9 \* 0.65) - (3/9 \* 0.92)




our H(presence) is -(7/9)log2(7/9) - (2/9)log2(2/9)   

= 0.76




gain = 0.76 - (6/9 \* 0.65) - (3/9 \* 0.92)  

gain = 0.02




exercise:  

google up information gain related to decision trees as well as associated concepts




next:  

random forest



