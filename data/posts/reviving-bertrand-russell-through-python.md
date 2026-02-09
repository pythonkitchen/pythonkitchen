title: Markov Chains in Python: Reviving Bertrand Russell's Prose
slug: reviving-bertrand-russell-through-python
pub: 2018-12-28 19:35:04
authors: arj
tags: python, markov-chains, probability, natural-language-processing, bertrand-russell
category: programming problems

Have you ever finished a book by a brilliant author and wished there was just one more chapter? While we can't bring back the great thinkers of the past, we can use **Markov Chains** to imitate their unique literary style. 

In this tutorial, we will explore the theory behind Markov Chains and build a Python script to generate text in the style of the philosopher Bertrand Russell.

---

## What is a Markov Chain?

A Markov Chain is a stochastic model describing a sequence of possible events. The crucial rule is that the probability of each event depends **only** on the state attained in the previous event.

In the context of text generation:
1.  We look at a "source text" (e.g., a book).
2.  We break it down into words.
3.  For every word, we record which words typically follow it.
4.  To generate new text, we pick a starting word and then "roll the dice" to pick the next word based on our recorded frequencies.

---

## The "Sun was Green" Example

Imagine our source text is:
> "The meadow was green. The sun was shining. The boy went away. The glass was shining."

We can map out the connections (the "Chain"):
*   **The** -> [meadow, sun, boy, glass]
*   **was** -> [green, shining, shining]
*   **shining** -> [The]

Because "shining" appears twice after "was," our model has a 66% chance of picking "shining" and a 33% chance of picking "green." This is how we maintain the statistical "feel" of the original author.

---

## Implementation in Python

Here is a robust implementation that reads a source file and generates a stylized phrase.

```python
import random

def build_markov_model(text):
    """Creates a dictionary mapping words to a list of possible next words."""
    words = text.split()
    model = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        
        if current_word not in model:
            model[current_word] = []
        model[current_word].append(next_word)
        
    return model

def generate_text(model, length=20):
    """Generates a random string of text based on the model."""
    if not model:
        return "Model is empty."
        
    # Start with a random word
    current_word = random.choice(list(model.keys()))
    output = [current_word]
    
    for _ in range(length - 1):
        if current_word in model:
            # Pick a random next word based on frequency
            current_word = random.choice(model[current_word])
            output.append(current_word)
        else:
            # If a word has no follower, pick a new random start
            current_word = random.choice(list(model.keys()))
            output.append(current_word)
            
    return " ".join(output)

# Example Usage
source_text = "Your long source text from Bertrand Russell here..."
model = build_markov_model(source_text)
print(generate_text(model, 30))
```

---

## Why Bertrand Russell?

Russell’s prose is famous for its logical clarity and complex but structured sentences. When you run this model over his work, like *Our Knowledge of the External World*, you get fascinating results:

> "The inductive principle, which need not known form made space and so that there were none except prejudice..."

While it might not always make perfect logical sense, it captures the **cadence** and **vocabulary** of the philosopher remarkably well.

## Conclusion

Markov Chains are a simple but effective introduction to Natural Language Processing (NLP). While they don't "understand" grammar, they demonstrate how powerful statistical patterns can be. 

Want to try something more advanced? Look into **Bigrams** (looking at pairs of words) or **LSTM Neural Networks** for even more realistic text generation!

### Further Reading:
*   [Building a Lexer in Python](https://www.pythonkitchen.com/building-a-lexer-in-python-tutorial/)
*   [Machine Learning Part 9: Neural Networks](https://www.pythonkitchen.com/machine-learning-part-9-neural-networks/)