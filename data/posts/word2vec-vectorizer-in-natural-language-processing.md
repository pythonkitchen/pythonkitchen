title: Word2Vec: Capturing Meaning in Vector Space
slug: word2vec-vectorizer-in-natural-language-processing
pub: 2023-04-13 11:09:08
authors: parthshukla
tags: embeddings, word2vec, deep learning
category: nlp
related_posts: bag-of-words-in-natural-language-processing,tfidf-vectorizers-in-natural-language-processing,chatterbot-google-colab-train-english-corpus

Bag of Words and TF-IDF are great, but they suffer from a fatal flaw: they have no concept of **meaning**. To those algorithms, "car" and "automobile" are just as different as "car" and "banana."

**Word2Vec** changed everything. It was the first popular technique to create **Word Embeddings**—dense vectors where similar words appear close to each other in mathematical space.

This allows us to do "math" with words, leading to the famous example:
$$King - Man + Woman \approx Queen$$

## The Core Intuition: Context is King

Word2Vec is based on the **Distributional Hypothesis**:
> "You shall know a word by the company it keeps."

The algorithm doesn't try to understand the word itself. Instead, it looks at the words *surrounding* it.
*   If "pizza" and "burger" both appear frequently next to "eat," "delicious," and "hungry," the model learns they are semantically similar.

---

## Architectures: CBOW vs. Skip-gram

Word2Vec is essentially a shallow neural network trained on a "fake" task. There are two ways to set this up:

### 1. CBOW (Continuous Bag of Words)
*   **Task:** Predict the **target word** based on the **context words**.
*   **Input:** "The cat sat ___ the mat."
*   **Output:** "on"
*   **Use Case:** Faster to train, better for frequent words.

### 2. Skip-gram
*   **Task:** Predict the **context words** based on the **target word**.
*   **Input:** "___ ___ sat ___ ___"
*   **Output:** "The", "cat", "on", "mat"
*   **Use Case:** Slower, but much better for rare words and smaller datasets.

---

## Python Implementation: Using `Gensim`

While TensorFlow or PyTorch can build these models, the industry standard for traditional Word2Vec is the **Gensim** library.

### 1. Training a Model

```python
from gensim.models import Word2Vec

# Data must be a list of lists of tokens
sentences = [
    ['i', 'love', 'machine', 'learning'],
    ['machine', 'learning', 'is', 'amazing'],
    ['i', 'love', 'coding', 'in', 'python'],
    ['python', 'is', 'a', 'great', 'language']
]

# Train the model
# vector_size: Dimension of the dense vector (e.g., 100 or 300)
# window: How many words to look at (left and right)
# min_count: Ignore words that appear less than this
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# The training is done! The vectors are stored in the model.
```

### 2. Using the Embeddings

Once trained, the model allows us to query for similarity.

```python
# Get the vector for a word
vector = model.wv['python']

# Find most similar words
similar = model.wv.most_similar('machine')
print(similar) 
# Output might include 'coding', 'python' depending on data
```

---

## Word2Vec vs. TF-IDF

| Feature | TF-IDF | Word2Vec |
| :--- | :--- | :--- |
| **Dimensionality** | High (Sparse, 10k+) | Low (Dense, 100-300) |
| **Semantics** | None | Captures meaning |
| **Memory** | High | Low |
| **Interpretability** | Easy (keywords) | Hard (random numbers) |

---

## Limitations

1.  **Static:** Word2Vec generates *one* fixed vector for every word. It cannot handle **polysemy** (words with multiple meanings). For example, "bank" (river) and "bank" (money) get the same vector.
    *   *Solution:* Newer models like **BERT** or **ELMo** generate contextualized embeddings.
2.  **OOV Words:** Like other methods, it struggles with words it hasn't seen before.

## Conclusion

Word2Vec is the bridge between simple counting statistics and modern Deep Learning NLP. By converting sparse, massive text data into dense, meaningful vectors, it enables powerful applications like recommendation engines, synonym detectors, and sophisticated chatbots.