title: The Zen Of Python: A Most In Depth Article
slug: zen-of-python-in-depth
pub: 2020-12-23 17:19:28
authors: arj
tags: 
category: zen

Note: *I wrote a quite complete article on the Zen but for some reason it went down in seo history. I am tired seeing people write 'in-depth' article with commentaries from the top of their head and materials they pulled out of their pockets. I'm publishing the article in here. The commentary part is built from the sayings of Brett Cannon, Guido, Chris Angelico, Nick Coghlan, Raymond Hettinger & co. Warning: read only if you are a fan of Python. Last notes: I do hope learners will get a great glimpse of how the Zen can help them structure their code and give them better insight and foresight. It's a documentation of how practically the Zen is applied in Python decisions.*
Table of contents
-----------------


* Birth of the Path
* Zen, Strunk and White
* Master Tim Showers his Blessings
* Authentic Commentary



The Zen of Python saw light for the first time in 1999. It's one of the many aspects that adds to the awesomeness of Python. It's a set of expressions which corners the spirit of the language. It was enounced by Tim Peters, a reputable software engineer, master Pythonista and Python's 'most prolific and tenacious core developer' in the words of none other than Guido [18]. This article bases itself mostly on the saying of core devs and highly reputable members. It makes a great gift to all those interested in the history of the sysadmin script which took the world by (pleasent) surprise.

![](https://images.unsplash.com/photo-1598545343242-89b4c263a343?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80)
Birth of the Path
=================



The way the Zen came about was unique. It was a reflection from the unknown Patrick Phalen about the Python feel [1]:


> 
>  ... the more I use
>  and learn about the language, the more I find myself appreciating the
>  nice balance and heft Guido gave to it. Yet there doesn't seem to be a
>  single document that sums up that "aesthetic," but rather it
>  tends to appear piecemeal, over time, mostly in the Wisdom of Chairman Tim.
> 



It was a call to infuse the Python spirit into aliens from Perl Land and beyond. It requested some 10 to 20 lines which sums up the Python view


> 
>  Would both Guido and TIm Peters be willing to collaborate on a short
>  paper -- call it "The Python Way" for lack of a better title -- which
>  sets out the 10-20 prescriptives they might offer to those who come to
>  Python from other languages and immediately want to find a way to bend
>  it into uncomfortable positions -- (implement closures, etc.).
> 



It was a request to prevent Pythonistas from falling into the error of campaigning for changing the language. It advocated for imbuing yourself with the language's flow and change your ways and views instead of the other way round. In the original mail, it quoted Fredrik Lundh as saying "sure looks like the 'community' thinks that changing the
language is more important that using it..." [5]. Patrick clarifies:


> 
>  What I have in mind is sort of a very brief Strunk-&-White-like
>  "Elements of Style" for Python, which suggests fundamental idiomatic
>  recommendations for operating within the spirit of the language. A
>  distillation of Python Zen is what I'm talking about -- something to go
>  off and contemplate when the "fix Python now" decibels become a bit
>  much.
> 


![](https://images.unsplash.com/photo-1555573989-14a9017746c3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=749&q=80)
Zen, Strunk and White
=====================



The Zen school lays out hints and guidelines. You understand by your own exercise and by the company of someone seasoned in the craft


> 
>  it de-emphasizes mere knowledge of sutras and doctrine and favors direct understanding through spiritual practice and interaction with an accomplished teacher or Master.[2]
> 



The Zen was a request to help Python people achieve the Python state of mind so that your code resonates well with the structure behind, conveying in the process the associated beauty, elegance and finesse. Those guidelines if well impregnated would make your code revered whithin the circle of true monks.

But, curiously enough, Tim tells [19]:


> 
>  If I were to change anything, I'd drop the reference to "Zen". That wasn't
>  part of the original, and was added by someone else.
> 



In other words, the title is not from the author [23]

Strunk & White is the name of two people, viz William Strunk and Elwyn Brooks White. Strunk wrote *The Elements of Style*, acclaimed by the Times as one of the most influencial books since 1923 [3]. White who was Strunk's student and reviser after the professor's death describes the book as:


> 
>  a forty-three page summation of the case
>  for cleanliness, accuracy, and brevity in the use of English [4]
> 



The effect of the book is described below, he being Strunk:


> 
>  he omitted so
>  many needless words, and omitted them so forcibly and with such eagerness and obvious
>  relish, that he often seemed in the position of having shortchanged himself — a man left
>  with nothing more to say yet with time to fill, a radio prophet who had out-distanced the
>  clock. Will Strunk got out of this predicament by a simple trick: he uttered every sentence
>  three times
> 



One effect of applying the Zen would then also be lighter code files.

![](https://images.unsplash.com/photo-1484108678824-e6543e2e4230?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=752&q=80)
Master Tim Showers his Blessings
================================



Master Tim heard the plea, approved the demand and responded accordingly [6]


> 
>  Clearly a job for Guido alone -- although I doubt it's one he'll take on
>  (fwiw, I wish he would too!). Here's the outline he would start from,
>  though :
> 



```python
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```


The 20th was left for Guido to fill in:


> 
>  There you go: 20 Pythonic Fec^H^H^HTheses on the nose, counting the one I'm
>  leaving for Guido to fill in.
> 



Venerable Tim shares exactly how the lines came about [15]:


> 
>  It was a throwaway python-list post. But like all great triumphs of literature, it was written during commercials breaks while watching professional wrestling on TV, and munching on a ham sandwich. All true!
> 



Yet, the author is emphatical: It's complete and more than meets the demand [6]:


> 
>  If the answer to *any* Python design issue
>  isn't obvious after reading those -- well, I just give up .
> 



The above also reveals the purpose of the Zen: To address design issues. And it's not a simple matter. Guido says [18]:


> 
>  In many ways, the design philosophy I used when creating Python is probably one of the main reasons for its ultimate success.
> 



The Zen only gives the outlines, in contrast to Strunk and White which gives explanations and examples in addition. Thus the need for commentaries. These help the non-initiated without being a replacement for the company of the bright minds.

In a time of fluctuating and steered standards, the reference in the actual PEP8 document to Strunk and White in the usage of the English language caused a bitter, ugly and messy thread [7]. It caused some of the best people of the community to forego following python-list [8], a casual reminder that being too open without limit hurts.

![](https://images.unsplash.com/photo-1593297372323-2ba78409d0b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80)
Reality of the Zen
==================



The Zen has become an important piece of the Python programming language. If you don't know the Zen, you won't strike the right chord to communicate with the community. Raymond Hettinger advises:


> 
>  Before creating more tracker items, please take time to learn about how Python's history, how it is used, and its cultural norms. In particular, read the Zen of Python, consider what is meant by duck-typing, what is meant by "a consenting adults language", what is meant by over-specification, etc. Python is quite different from Java in this regard. [13]
> 



There's also a practical aspect to it. It's popular because it works [14]. It's the golden guiding principle in pretty much everything Python.

Finally are the Zen points rules? What are they really. Many people take the Zen for rules. The 'most opinionated linter ever' at one time actually included the Zen to back their views [9]. It was situations like these which prompted me to write: The Zen Of Python Is A Joke And Here Is Why [10]. It was nice enough for Michael Kennedy and Brian Okken to call it a 'must read' on PythonBytes [11].

According to Nick Coghlan, the Zen gives you the idea, not everything [12]:


> 
>  This
>  challenge is reflected in the fact that the Zen of Python is
>  deliberately self-contradictory, as it articulates competing design
>  principles to take into consideration, rather than being able to
>  provide ironclad rules that avoid the need for human judgement in
>  determining which of those design guidelines are most salient in any
>  given situation.
> 



Self contradiction is also coincidentally, one of the criticised aspect of Strunk and White [17].
The Zen also goes beyond coding, such as shaping the thought pattern of features [12]:


> 
>  The thing we work toward as core developers, and aspiring core
>  developers, is good design intuition that aligns with the Zen of
>  Python. That doesn't mean we're all going to be able to perfectly
>  articulate that intuition in every case, and even when we can, those
>  explanations are themselves generally going to be backed by intuition
>  rather than rigorous scientific research.
> 



If ever i myself would have added a 20th one it would have been: "Use your judgement.". But Nick illustrated it better.

As for the famous `import this` command, it was Barry Warsaw's pick. He sneaked it in a this.py in 2001 along with the ROT13 obfuscation [16]. He also mentionned that it was a time 'when the Python community had a sense of humor'.

![](https://images.unsplash.com/photo-1561739091-9d698cb277ec?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80)
Authentic Commentary
====================



Now the time is ripe to see what the Zen actually means. But before we should know that whatever the words
and concepts mean in the Zen is not necessarily applicable elsewhere [20].

### Beautiful is better than ugly.



Beautiful and ugly in this context has nothing to do with human appearance. It's in the same general sense as in other technical fields: there's beautiful & ugly physics, beautiful & ugly mathematics, beautiful & ugly computer code [19]. Beauty in design is very similar to beauty in flora. For it refers to a general feeling of consistency, pureness and standing out on its own. It's abstract and doesn't have anything to do with humans [20]. This line can be replaced by 'Elegant is better than inelegant.' to understand it better [21]. The 'beauty' line is one of multiple contrasts, and should be judged in that context, not in isolation [22]. At heart, Python's design emerged from Guido's sense of beauty [23]

### Explicit is better than implicit.



> 
>  The Zen of Python points out that "explicit is better than implicit" for a reason: ambiguity and implicit knowledge that is not easily communicated code is easy to get wrong and leads to bugs. By forcing developers to explicitly separate out their binary data and textual data it leads to better code that has less of a chance to have a certain class of bug.
> 



Brett Cannon [25]


> 
>  It's been interesting seeing how ppl interpret "explicit is better than implicit" to say specifying 'object' is good. For me, syntactically leaving out a base class **is** explicit, not as *verbose*, and is more visually identifiable
> 



Brett Cannon [26]


> 
>  Implicit package directories go against the Zen of Python
>  
>  Getting this one out of the way first. As I see it, implicit package
>  directories violate at least 4 of the design principles in the Zen:
>  - Explicit is better than implicit (my calling them implicit package
>  directories is a deliberate rhetorical ploy to harp on this point,
>  although it's also an accurate name)
>  - If the implementation is hard to explain, it's a bad idea (see the
>  section about backwards compatibility challenges)
>  - Readability counts (see the section about introducing ambiguity into
>  filesystem layouts)
>  - Errors should never pass silently (see the section about implicit
>  relative imports from main)
> 



Nick Coghlan [24]:

### Simple is better than complex.



> 
>  Currently, when I teach sets, I take pleasure in the near-zero learning curve
>  and absence of special cases. Set code becomes a prime example of
>  "readability counts" and "simple is better than complex." More importantly,
>  I think there is value in API simplicity for lists, sets, and dicts, our basic tools.
>  The ABCs for sets currently reflect that simplicity and it would be sad if that
>  started to get lost in order to save one line here or there.
> 



Raymond Hettinger [39]

### Complex is better than complicated.



oxfordlearnersdictionaries.com gives both complex and complicated as synonyms with meaning:
"made of many different things or parts that are connected; difficult to understand"

dictionary.cambridge.org gives complex as: "having many parts connected in ways that are difficult to understand" and complicated as: "confusing or difficult to understand"

macmillandictionary.com defines complex as: "something that is complex has a lot of details or small parts that make it difficult to understand or deal with" and complicated as: "difficult to do, deal with, or understand, especially because of involving a lot of different processes or aspects" and 2. "made up of many different but connected parts"

merriam-webster.com gives complex as: a whole made up of complicated or interrelated parts and composed of two or more parts, complicated as: consisting of parts intricately combined and difficult to analyze, understand, or explain

We can translate the line to mean:


> 
>  A solution which is made up of different interconnected parts is better than one which is difficult to analyze, understand, or explain
> 



or


> 
>  A complex solution is better than a more complex one
> 



or


> 
>  A solution which is made up of different interconnected parts is better than one which has many parts but is difficult to analyze, understand, or explain
> 


### Flat is better than nested.



Nesting constructs like conditionals or functions or classes or modules one inside the other too much is frowned upon. The x.y.z.q.w.w example is given as the author of the lib nested too many modules one inside the other, given a tiring usage experience

### Sparse is better than dense.



> 
>  When I channeled "sparse is better than dense" as one of Guido's
>  fundamental design principles, I was as mystified as anyone else. Indeed,
>  my first thought was "what the hell is that supposed to mean?!". But, as a
>  professional channeler, I was duty-bound to pass it on as it was revealed,
>  neither adding nor removing jot nor tittle.
>  
>  In the years since, I've come to see that it has many meanings, some of
>  which I explained yesterday. I'm learning from other thoughtful posts (such
>  as yours) that I still have a long way to go in mining its full depth. Or
>  in realizing its full shallowness, depending on how you view it .
>  
>  << Or maybe his attention is just elsewhere... but I'd like to think that
>  this is a Zen koan.>>
>  
>  Oh no. Koans are far more advanced, in the nature of using a stick to stir
>  up a fire that consumes the stick in its quest to illuminate its own nature.
>  The channeled 20 Pythonic Theses (their original name -- "The Zen of Python"
>  was tacked on by somebody else, whom I suspect was not really a Zen master)
>  are more about using sticks to build a strong platform, as if sticks were
>  real and strong platforms were worthy of building. It takes a stronger
>  channeler than me to dismiss that as illusion. The end of Pythonic
>  Enlightenment is pleasure in achieving fine code; it's not enough to get you
>  Nirvana, presumably because it's still full of sticks .
>  
>  <>
>  
>  That's definitely part of it. The openness of Python's visual appearance,
>  the ubiquitous use of dicts, and the carefully chosen handful of control
>  structures were the first things I thought of.
>  
>  <<...
>  I'm probably reading more into this little statement than is there.>>
>  
>  I don't believe that's possible. Try harder .
> 



Tim Peters [40]

### Readability counts.



> 
>  There's that word "readability" again. Sometimes I wish the Zen of
>  Python didn't use it, because everyone seems to think that "readable"
>  means "code I like".
> 



Chris Angelico [34]

The motto of Python is clarity. The language attempts to be as readable as the english language. Guido says [18]:


> 
>  I’d like to mention one readability rule specifically: punctuation characters should be used conservatively, in line with their common use in written English or high-school algebra.
> 


### Special cases aren't special enough to break the rules.


### Although practicality beats purity.



> 
>  if you're going from 8-bit strings to unicode using implicit con-
>  version, the current design can give you:
> 
> 
> ```python
> "UnicodeError: UTF-8 decoding error: unexpected code byte"
> 
> ```
> 
>  
>  if you go from unicode to 8-bit strings, you'll never get an error.
>  
>  however, the result is not always a string -- if the unicode string
>  happened to contain any characters larger than 127, the result
>  is a binary buffer containing encoded data. you cannot use string
>  methods on it, you cannot use regular expressions on it. indexing
>  and slicing won't work.
> 
> 
> ```python
> unlike earlier versions of Python, and unlike unicode-aware
> versions of Tcl and Perl, the fundamental assumption that
> a string is a sequence of characters no longer holds. =20
> 
> ```
> 
>  
>  in my proposal, going from 8-bit strings to unicode always works.
>  a character is a character, no matter what string type you're using.
>  
>  however, going from unicode to an 8-bit string may given you an
>  OverflowError, say:
> 
> 
> ```python
> "OverflowError: unicode character too large to fit in a byte"
> 
> ```
> 
>  
>  the important thing here is that if you don't get an exception, the
>  result is *always* a string. string methods always work. etc.
>  
>  [8. Special cases aren't special enough to break the rules.]
> 



Fredrik Lundh [42]


> 
>  First, I think the PyCharm case is compelling enough on its own. I 
>  realized after I sent it that there's a related class of tools that are 
>  interested: PyFlakes, PyLint, and the like. I'm sure the static 
>  correctness analyzers would like to be able to automatically determine 
>  "this is an illegal number of parameters for this function" for 
>  builtins--particularly for third-party builtins! The fact that we 
>  wouldn't need to special-case pydoc suggests it's the superior 
>  approach. ("Special cases aren't special enough to break the rules.")
> 



Larry Hastings [41]

### Errors should never pass silently.


### Unless explicitly silenced.



> 
>  Thus, in Python 2.3, we abandoned my home-grown 2.2 MRO algorithm in favor of the academically vetted C3 algorithm. One outcome of this is that Python will now reject any inheritance hierarchy that has an inconsistent ordering of base classes. For instance, in the previous example, there is an ordering conflict between class X and Y. For class X, there is a rule that says class A should be checked before class B. However, for class Y, the rule says that class B should be checked before A. In isolation, this discrepancy is fine, but if X and Y are ever combined together in the same inheritance hierarchy for another class (such as in the definition of class Z), that class will be rejected by the C3 algorithm. This, of course, matches the Zen of Python's "errors should never pass silently" rule.
> 



Guido [33]


> 
>  This is of course a backwards-incompatible change to logging semantics: instead
>  of saying that logging will be silent unless explicitly asked to produce output,
>  we're saying that logging will always produce output for warnings and errors (or
>  perhaps just errors), unless explicitly silenced. This is of course in line with
>  the Zen of Python; the present behaviour, which is not so aligned, is based on
>  the idea that logging should not affect program behaviour if it's not wanted by
>  the program developer (as opposed to library developer).
>  
>  It would also mean changing the documentation about NullHandler to say: "If you
>  have messages which must get out when you can't raise an exception, then don't
>  add a NullHandler to your top-level loggers."
> 



Vinay Sajip [28]


> 
>  You might prefer to get an exception for "missing keys"that would help alert you to a bug in your
>  program, in cases in which you know all ks in somekeys should definitely also be keys in
>  somedict. Remember, "errors should never pass silently. Unless explicitly silenced," to quote The
>  Zen of Python --Python Cookbook
> 


### In the face of ambiguity, refuse the temptation to guess.



> 
>  Well, the Zen of Python states "In the face of ambiguity, refuse the temptation 
>  to guess". So that's the policy the builtin dict follows - it doesn't try to guess when to 
>  make a copy, or whether or not to use identity based semantics in the face of 
>  mutability. Instead, it raises an exception at key entry time, asking the 
>  programmer to clarify their intent.
> 



Nick Coghlan [37]


> 
>  On the issue of {a.b.c}: like several correspondents, I don't like the
>  ambiguity of attribute vs. key refs much, even though it appears
>  useful enough in practice in web frameworks I've used. It seems to
>  violate the Zen of Python: "In the face of ambiguity, refuse the
>  temptation to guess."
>  
>  Unfortunately I'm pretty lukewarm about the proposal to support
>  {a[b].c} since b is not a variable reference but a literal string 'b'.
>  It is also relatively cumbersome to parse. I wish I could propose
>  {a+b.c} for this case but that's so arbitrary...
> 



Guido [31]


> 
>  By now, you can probably imagine why Python refuses to guess among the hundreds of possible
>  encodings. It's a crucial design choice, based on one of the Zen of Python principles: "In the face
>  of ambiguity, resist the temptation to guess." --Python Cookbook
> 


### There should be one-- and preferably only one --obvious way to do it.



> 
>  But remember TOOWTDI from the Zen of Python.
> 



Guido [32]


> 
>  The Zen of Python says that "there should be one -- and preferably only one -- obvious way to do it". Having literals in the language that could represent either textual data or binary data was a problem.
> 



Brett Cannon [25]


> 
>  When Python evolves, new ways emerge inevitably. DeprecationWarning
>  are emitted to suggest to use the new way, but many developers ignore
>  these warnings which are silent by default.
> 



Victor Stinner [35]


> 
>  String formatting is one of those things that defy the
>  Zen of Python, that there should only be one obvious way to do things.
> 



Mariatta Wijaya [36]

It should be noted that the dashes here don't play a role as it's Tim's way of emphasis. And it is to be noted that Brett missed it on his blog. He was maybe writing from memory.

### Although that way may not be obvious at first unless you're Dutch.



> 
>  In context, "Dutch" means a person from the Netherlands, or one imbued with
>  Dutch culture (begging forgiveness for that abuse of the word). I would
>  have said French, except that every French person I asked "how do you make a
>  shallow copy of a list?" failed to answer: alist[:]
>  so I guess that's not obvious to them. It must be obvious to the Dutch,
>  though, since it's obvious to Guido van Rossum (Python's creator, who is
>  Dutch), and a persistent rumor maintains that everyone who posts to
>  comp.lang.python is in fact also Dutch. The French people I asked about
>  copying a list weren't Python users, which is even more proof (as if it
>  needed more).
>  
>  Or, in other words, "obvious" is in part a learned, cultural judgment.
>  There's really nothing universally obvious about any computer language,
>  deluded proponents notwithstanding. Nevertheless, most of Python is obvious
>  to the Dutch. Others sometimes have to work a bit at *learning* the one
>  obvious way in Python, just as they have to work a bit at learning to
>  appreciate tulips, and Woody Woodpecker impersonations.
> 



Tim Peters [38]

### Now is better than never.


### Although never is often better than *right* now.



> 
>  There are also cases where we'll decide "it seems plausible that this
>  might be a good idea, so let's try it out and see what happens in
>  practice rather than continuing to speculate" - only ever doing things
>  that you're already 100% certain are a good idea is a recipe for
>  stagnation and decline (hence the "Now is better than never" line in
>  the Zen).
> 



Nick Coghlan [27]

### If the implementation is hard to explain, it's a bad idea.


### If the implementation is easy to explain, it may be a good idea.



> 
>  Yeah, that's what everybody proposes to keep the language semantics
>  unchanged. But I claim that an easier solution is to say to hell with
>  those semantics, let's change them to make the implementation simpler.
>  That's from the Zen of Python: "If the implementation is easy to
>  explain, it may be a good idea." I guess few people can seriously
>  propose to change Python's semantics, that's why I am proposing it.
> 



Guido [29]


> 
>  Accepting peps: A bit more motivation for my choice: re-reading PEP 549 reminded me of how
>  its implementation is remarkably subtle (invoking Armin Rigo; for more
>  details read https://www.python.org/dev/peps/pep-0549/#implementation). On
>  the contrary, the implementation of PEP 562 is much simpler. With the Zen
>  of Python in mind, this gives a hint that it is the better idea, and
>  possibly even a good idea.
> 



Guido [30]

### Namespaces are one honking great idea -- let's do more of those!



> 
>  Namespaces (and also global and local scopes) are key for preventing names in one module or scope from conflicting with names in another. But also remember that flat is better than nested: As great as they are, namespaces should be made only to prevent naming conflicts, and not to add needless categorization.
> 



Al Sweigart [43]

The Koans offered the programming world a great legacy. It is an interesting sight to see from Go to JavaScript devs analysing their own langs in the light of the Zen.

Your suggestions accepted at: arj [.] python [@] gmail [.] com



---



[1] https://mail.python.org/pipermail/python-list/1999-June/014096.html
[2] https://en.wikipedia.org/wiki/Zen with references to Poceski and Yampolski
[3] All-TIME 100 Nonfiction Books. Time, Inc. Retrieved 2014-05-14.
[4] http://www.jlakes.org/ch/web/The-elements-of-style.pdf
[5] https://mail.python.org/pipermail/python-list/1999-June/017368.html
[6] https://mail.python.org/pipermail/python-list/1999-June/001951.html
[7] https://mail.python.org/archives/list/python-ideas@python.org/thread/AE2M7KOIQR37K3XSQW7FSV5KO4LMYHWX/
[8] https://www.mail-archive.com/python-dev@python.org/msg109166.html
[9] https://github.com/wemake-services/wemake-python-styleguide/tree/fd7b6d9d14d73cab3d7f3ac4c910e4c75b093c4c
[10] https://dev.to/abdurrahmaanj/the-zen-of-python-is-a-joke-and-here-is-why-you-should-not-take-it-too-seriously-508d
[11] https://pythonbytes.fm/episodes/show/170/visualize-this-visualizing-python-s-visualization-ecosystem
[12] https://mail.python.org/archives/list/python-dev@python.org/thread/DOKCD6TKN26DOOMYWAHFIMU3LGSCN7Y5/
[13] https://mail.python.org/pipermail/docs/2014-June/019159.html
[14] https://mail.python.org/pipermail/python-committers/2018-July/005747.html
[15] https://www.wefearchange.org/2020/05/zenofpython.rst.html
[16] https://www.wefearchange.org/2010/06/import-this-and-zen-of-python.html
[17] Wikipaedia via Pullum, Geoffrey K. (April 17, 2009). "50 Years of Stupid Grammar Advice". The Chronicle of Higher Education.
[18] http://python-history.blogspot.com/2009/01/pythons-design-philosophy.html
[19] https://mail.python.org/pipermail/python-ideas/2018-September/053389.html
[20] https://mail.python.org/pipermail/python-ideas/2018-September/053382.html
[21] https://mail.python.org/pipermail/python-ideas/2018-September/053412.html
[22] https://mail.python.org/pipermail/python-ideas/2018-September/053421.html
[23] https://groups.google.com/g/python-ideas/c/Upc9MbzmFAA/m/2TiIWTlbBwAJ
[24] https://mail.python.org/pipermail/import-sig/2012-March/000423.html
[25] https://nothingbutsnark.silvrback.com/why-python-3-exists
[26] https://twitter.com/brettsky/status/1253704411873869826?lang=en
[27] https://mail.python.org/pipermail/python-list/2005-January.txt
[28] https://mail.python.org/pipermail/python-dev/2010-December/106556.html
[29] https://mail.python.org/archives/list/python-dev@python.org/thread/XZ23MPVGDDHUWE2VTGGEHVW4A4W76SH6/
[30] https://mail.python.org/pipermail/python-dev/2017-November/150528.html
[31] https://mail.python.org/pipermail/python-dev/2006-May/065059.html
[32] https://mail.python.org/pipermail/python-3000/2006-April/000348.html
[33] http://python-history.blogspot.com/2010/06/method-resolution-order.html
[34] https://www.mail-archive.com/python-dev@python.org/msg100513.html
[35] https://discuss.python.org/t/rejected-rfc-pep-608-coordinated-python-release/2539
[36] https://static.realpython.com/python-tricks-book/Python%20Tricks%20Sample.pdf
[37] https://mail.python.org/pipermail/python-list/2005-January/296762.html
[38] https://mail.python.org/pipermail/python-list/2004-May/283635.html
[39] https://mail.python.org/pipermail/python-ideas/2009-February/002998.html
[40] https://mail.python.org/pipermail/python-list/2002-July/147124.html
[41] https://mail.python.org/pipermail/python-dev/2013-July/127229.html
[42] https://mail.python.org/pipermail/python-dev/2000-April/003742.html
[43] https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/
