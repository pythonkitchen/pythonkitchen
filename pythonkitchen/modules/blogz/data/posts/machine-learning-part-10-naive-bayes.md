title: Machine Learning Part 10 Naive Bayes
slug: machine-learning-part-10-naive-bayes
pub: Wed, 07 Apr 2021 10:11:56 +0000
authors: Abdur-RahmaanJ

#10 naive bayes

Machine Learning

๐โก supervised learning
โก unsupervised learning
โก reinforcement learning

recap:
๐ types of supervised learning

โ classification ๐

โ regression ๐

โ mixed โ

naive bayes classification

โฑ bayes theorem

bayes theorem states that

P(B|A) = (P(A|B) \* P(B)) / P(A)

Probability of B given A = ...

๐ naive comes from the fact that features have been independently chosen from a distribution

โฑ conditional probability

that's it, checkout dependent events' probabilities. let us take a domino game. the probability taking out a piece containing one after having taken a piece containing a 6. in this example, the taking of one is affected at the very least by the fact that the tiles have been diminished by 1 (7/28 ร 7/27). similarly naive bayes allows us to guess events more precisely by adding known events in the game.

โฑ are you ill?

a famous use of the theorem is to find out whether you are ill given you have symptoms of a disease. the formula tells us that only looking if you have symptoms is not enough.

le us say that a new disease named scarius is out. now you check out the symptoms, brr you have those it seems ... but do you really have the disease?

P(scarius given symptoms) = (P(symptoms given scarius) \* P(scarius))/P(symptoms)

if symptoms is fever, P(symptoms) is P(fever) i.e. the probability that a person gets fever on any day.

P(symptoms given scarius) will be high since when you are ill you will get symptoms. let us say 0.96

P(scarius) ah let us say that disease is rare, 0.0001

p(fever) let us say 0.1

our P will be

(0.0001 ร 0.96) รท 0.1

= 0.00096

so, without taking in consideration those 3 probabilities, you'd make an erroneous guess

โฑ one interesting article

https://www.saedsayad.com/naive\_bayesian.htm

โฝ๏ธ exercise

see the theorem's derivation by using sets via a venn diagram
