title: Machine Learning Part 12 Association Analysis
slug: machine-learning-part-12-association-analysis
pub: Wed, 07 Apr 2021 10:14:26 +0000

#12 association analysis

Machine Learning

♡ supervised learning
👉 ♡ unsupervised learning
♡ reinforcement learning

unsupervised learning is where your program has to find how the data relates to each other. there is no prior training

types of unsupervised learning

♠️ clustering
♠️ association

association analysis

finds associations between items, like what customers usually buy together in a store. if that is known, sales might be put on those items, or they could be placed together to ease the customers' life or ... why not rise the price on both?

🔎 itemset: those items occuring together

✳ confidence

confidence measure how certain a rule. if clients always buy milk with eggs, we say that the confidence is 100%

confidence(A, B) = P(B|A)
i.e. P(B) given A

✳ support

the support of an itemset is the percentage of the dataset that contains the itemset

let us say out of 5 transactions at a store, butter and bread was bought together 3 times. it's support is 3/5

● with support and confidence, we can assess our association rule's success

✳ lift

lift is defined as

support(X u Y) / support(X) \* support(Y)

if we are looking for milk, tea to sugar together in a dataset of 6 transactions,

support(X u Y) means how many times over 6 they appear together, let us say it is 2

support(X) means how many times milk, tea appear together in the dataset, let us say it is 4

support(Y) means how many times sugar appear in the dataset, let us say 3 times

our support is

2/6 / 4/6 \* 3/6

= 1

a lift if one means one has no effect on the other

if the lift is greater than one it means that one is dependent on the other (it matters)

a lift of less than one means that one adversely impacts the other

✳ a priori algorithm

this tells us that if an item set is frequent, then it's subset must also be frequent. you specify a certain support level to go from as if you check each and every transaction, it is very slow!

✳ multilevel association rules

instead of pinpointing items, they can be associated higher up. like finding people who bought milk brand A and flour brand B together might be hard but finding that people bought milk and flour together might be easier
