title: Reviving Bertrand Russell Through Python
slug: reviving-bertrand-russell-through-python
pub: Fri, 28 Dec 2018 19:35:04 +0000


famous authors are praised, respected, admired and missed due to their works. after reading all the titles of an excellent author, one is left wishing for more. curiously enough we now have the ability to produce more books that fit in the literary style, depth and topic tackling techniques of writers. perfection in this field opens a new era, you might hear of ~~mouse~~ cat trap by darwin, russian trip by mark twain and god beyond doubt by hawkins.




markov?
-------




markov chains are probabilistic pattern generating models. 'patterns' can be events, text or geometrical arrangements




let us take the example of a person going to a fast food outlet where there are only three types of foods, rounder, burger and panini.




the probability of him taking a rounder after already taking one is 0.2 or 2/10




after a rounder, the probability of taking a burger is 0.4 or 4/10




after a rounder, the probability of taking a panini is 0.4 or 4/10




notice that there are three arrows going out for three choices, which when added make up 1




* ![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov.png)




let us make up the remaining part for burger




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov2.png)


now completed it looks like




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov2-1.png)


B P P R P P ...




matrix representation
---------------------




the above can also be written as




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov_matrix_python.png)


but whatever does that means?




that's why we have state space to specify from where we begin




  **state space {1 = rounder, 2 = burger, 3 = panini}** 




means we start first by rounder, then burger then panini




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov_matrix_python2.png)


applying markov to text
-----------------------




the idea is to:




* build a markov model
* then to generate text through the model




### rehearsal




we'll have a program that scans every word and records the next word




let us take the text:




*the meadow was green. the sun was shining. the boy went away. the glass was shining*




tabulating next words we get:




the -> meadow, sun, boy, glass




meadow -> was




was -> green, shining,shining




sun -> was




boy -> went




went -> away




glass -> was




from those we can generate the text




the sun was green




with path




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/sunwasgreenpy.png)


-----------------------------------------------------------------




the meadow was shining




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/meadowwasshiningpy.png)


### wait, what about probabilities ?!




well see




 was -> green, shining,shining 




when we randomly choose from [ green, shining,shining ] we actually have more chance getting shining than green as they occur twice more, no need of writing up the probabilities. the only draw back is programming efficiency, which we'll clean up in another post




the code
--------





```python

def format_text(file_read):
    # getting the data ready for generation
    data = {}
    lines = file_read.replace('\n', ' ').split('.')
    for line in lines:
        words = line.split()

        for i,word in enumerate(words):
            if i+1 < len(words):
                next_word = words[i+1]

                if word not in data:
                    data[word] = [next_word]
                else:
                    data[word].append(next_word)
    return data

def rand(data):
    # chooses random element from dictionary
    return random.choice(list(data))

def generate(times, data):
    # specifies length of generated phrase
    current = rand(data)
    gens = [current]
    try:
        for i in range(times):
            current = random.choice(data[current])
            gens.append(current)
    except:
        pass
    return gens


with open('source.txt', 'r') as source:
    file = source.read()

data = format_text(file)

print(' '.join(generate(10, data)))

```



format text returns a dictionary. here is a snapshot:





```python
{
'is,': ['besides'], 
'unsupported': ['by'], 
'one': ['which', 'of', 'at', 'reason', 'proposition', 'form', 'of', 'which', 'thing', 'thing', 'magnitude', 'kind', 'of', 'relation', 'fact,', 'fact,', 'involving', 'case', 'of', 'kind', 'atomic', 'of', 'happens,', 'something', 'is', 'would'],
...

```



i ran the program over some paragraphs of   





*Our Knowledge of the External World as a Field for Scientific Method in Philosophy* 




 from





> Mathematical logic, even in its most modern form, is not *directly* of  
>  philosophical importance except in its beginnings. After ...
> 
>  Our Knowledge of the External World as a Field for Scientific Method in Philosophy  
> by Bertrand Russell 




to





> Charles I. and death and his bed  
>  are objective, but they are not, except in my thought, put together as  
>  my false belief supposes. It is therefore necessary, in analysing a  
>  belief, to look for some other logical form than a two-term relation.  
>  Failure to realise this necessity has, in my opinion, vitiated almost  
>  everything that has hitherto been written on the theory of knowledge,  
>  making the problem of error insoluble and the difference between belief  
>  and perception inexplicable.
> 
> Our Knowledge of the External World as a Field for Scientific Method in Philosophy   
> by Bertrand Russell




the core is here





```python
    current = rand(data)
    gens = [current]
    try:
        for i in range(times):
            current = random.choice(data[current])
            gens.append(current)
    except:
        pass
    return gens

```



we start by adding a random word (a random element of the dictionary) to the list





```python
current = rand(data)
gens = [current]

```



then we choose a random word from the words coming next




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/explanation_markov_code.png)


the code produces like




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markovgen1.png)


![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov2-2.png)


with length 20




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov3-1024x21.png)


again length 10




![](https://www.pythonmembers.club/wp-content/uploads/2018/12/markov4.png)


the phrase is correct euu yes, it imitates the style for now





> infinite number of which we have the one thing having some other terms or opinion about Socrates--that he feels his insight, we can discover, for example, two classifications we mean that two terms, being equally true when one of the most
> 
> generated text - length 40  
> 





> inductive principle, which need not known form made space and so that there were none except prejudice, so long as follows that, if they may sometimes know that we saw that I shall bring my umbrella if you could hardly be outlined in the whole theory of general truths by no
> 
> generated text - length 50





> return to asymmetrical relations, such as follows that, if this way to be in the existent world, and red, and pure logic, no particular subject-matter otherwise than the case of the supposed common constituent, but are true or "one inch taller" or deny this is true, we are more than a "fact," I have that membership of have knowledge is any
> 
> generated text - length 60 





> Thus "father" is the difference between B is something altogether more difficult, and common world would be inferred from sense, and mortality that certain relation is apt to be asserted or deny this hypothetical form, but the second being equally true in order to have accepted and B, and philosophically it is said to properties becomes obviously impossible to infer all propositions are and B, also knew that all things have
> 
>  generated text - length 70 





> From poverty in any such as regards the subject-predicate form--in other thing is in its constituents and were less anxious to deal throughout the other property, then B and most of unreality of the weather had been written on the marks of a certain known objects are indispensable in the everyday world with completely general propositions, and so that there is independent of three things, it should be explained would not transitive, but to give rise to exist
> 
>  generated text - length 80 




room for improvement
--------------------




well we can improve many things such as: first word first, choosing probabilities as numbers rather than from list, be sensitive to punctuations, improve context etc. a rough code lands up a pretty nice result



