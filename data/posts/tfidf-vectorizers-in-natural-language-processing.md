title: TFIDF Vectorizers in Natural Language Processing
slug: tfidf-vectorizers-in-natural-language-processing
pub: 2023-03-13 10:13:01
authors: parthshukla
tags: 
category: data science,machine learning

Vectorization is a technique in natural language processing that is used to transform the text into vectors. However, multiple vectorization techniques are used to transform different texts. TFIDF is a widely used and efficient vectorization technique that data scientists use.

In this article, We will discuss the TFIDF vectorization technique, how it works, the core intuition behind it, and some examples associated with the same. This article will help one to understand the technique more deeply and will be able to apply it wherever necessary.

Before directly jumping into the article, let us discuss what vectorization techniques are.

Table of Content
================


1. What are Vectorization Techniques?
2. What is TFIDF?
3. Some Important Terminologies
4. Term Frequency
5. Document Frequency
6. Inverse Document Frequency
7. The TFIDF Score
8. Key Takeaways
9. Conclusion


What are Vectorization Techniques?
==================================



Machine learning algorithms are primarily statistically based learner who learns from the data and apply functions that are predefined to train and learn from the data. Here the algorithm can not understand any type of text data; hence, if we are needed to work on any text data, we can not directly feed that data to the algorithm. The algorithms only understand the language of vectors and numbers.

Hence in such cases, we vectorize or transform the data into vectors or numbers to feed that data to the machine learning algorithms and train the model. There are multiple vectorization techniques available that are used for vectorization. Some of them are CountVectorizer, Word2Vec, and TFIDF.

What is TFIDF?
==============



As we discussed above, TFIDF is a vectorization technique used to transform any kind of textual data into vectors to feed the data to the machine learning algorithms and to train on.

Generally, TFIDF consists of two terms TF and IDF. TF stands for Term Frequency, and IDF stands for Inverse Document Frequency. The TFIDF technique works on the principle of the same. Here the TF and iDF for a word and document are calculated and multiplied, which returns the TFIDF score, and based upon that, the word is transformed into the vector.

Let's try to understand the same by splitting it into two parts, Term Frequency, and inverse Document Frequency.

Some Terminologies
==================



Before jumping to the term frequency, let us discuss some of the terminologies that can be helpful here.

**Character:** A character is a term used for a single letter. For example: a, b, c, etc

**Word:** A word combines several characters, For example, Machine, Learning, Data, etc.

**Document:** A document is a term used to represent any kind of sentence or a combination of words. For example, Machine Learning is good to have skills.

**Corpus:** A corpus is a term used to represent all 5the documents and texts in the dataset. For example, the complete dataset will be fed to the model for training.

Term Frequency
==============



Term frequency measures how frequently a particular term appears in a document. It gives an idea about the frequency of a term, word, or term that appears in different documents.

**Example:**

Document: Machine Learning is a Good Skill.

Now here we can see the document consists of 6 words that are Machine, Learning, Is, a, Good, and Skills.

Now here, every word in the document will have its term frequency.

The formula for the Term Frequency is,
`Term Frequency = Number of Times Word Appears in a Document / Total Number of Words in a Document.`

Now the Term Frequenc6y for the Word Machine would be ⅙, for the word Learning would be 1/6, and if a particular word is not in a document, then the term frequency would be zero.

Document Frequency
==================



Document Frequency is a term used to measure how frequently a word appears in several documents. It gives an idea of the word's popularity in the whole corpus.

The formula for the document frequency is 
`Document Frequency = Number of Documents That has the Word / Total Number of Documents`

For example, if we have two documents 
Document 1 = Machine Learning is a Good Skill.
Document 2 = Machine Learning is Complex to learn.

Then the document frequency for the word Machine would be 2/2.

Inverse Document Frequency
==========================



Inverse document frequency is an inversed form of document frequency calculated in a log form.

> Inverse document frequency = 1 / document Frequency


The TFIDF Score
===============

Now that we know the term and inverse document frequency, let us discuss how it helps vectorize the word or text of the data. As we measure the importance of a term in a document and different documents, we can now assign a score to all the words in the corpus and vectorize them accordingly.

Here we will calculate the Tf and IDf scores for each of the terms, and the values will be multiplied to achieve a score or weightage of the term. The higher the TFIDF score, the higher the importance and significance of the term in a document and a corpus.

Code Example:
=============



```python
From sklearn.feature_extraction.text, import TfidfVectorizer
from sklearn.model_selection import train_test_split

X_tfidf = vectorizer.fit_transform(X)

# split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.33, random_state=42
)

From sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

# Training classifier model 
sgd = SGDClassifier()
sgd.fit(X_train, y_train)

# model prediction
y_pred = sgd.predict(X_test)

print(classification_report(y_test, y_pred))

```

Key Takeaways
=============


1. Vectorization is a technique that transforms text data into vectors to feed it to the machine learning algorithm.
2. TFIDF is a vectorization technique that transforms textual data into vector form.
3. TF is a term frequency measure of the importance or significance of a term in a particular document.
4. Inverse document frequency is a measure that is a measure of the significance of a term in the corpus, calculated by measuring the presence of a term in different documents.
5. Higher the TFIDF scores, the higher the significance of the term in a document and a corpus of the dataset.


Conclusion
==========



In this article, we discussed vectorization techniques, how they work, what TFIDF is, what are the terms Term Frequency and Inverse document frequency, and how they are calculated with the code examples. This article will help one to understand this technique deeply and will able to apply it wherever necessary.
