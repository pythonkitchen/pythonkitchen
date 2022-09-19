title: Display Most Frequent Words Using Pygame
slug: display-most-frequent-words-python-pygame
pub: Tue, 24 Nov 2020 11:22:02 +0000


```python
"""
Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-rahmaanJ
Instructions:
    pip install hooman
"""
from hooman import Hooman
import pygame
from collections import Counter

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

text = '''
Python programs frequently need to handle data which varies in type, presence of attributes/keys, or number of elements. Typical examples are operating on nodes of a mixed structure like an AST, handling UI events of different types, processing structured input (like structured files or network messages), or “parsing” arguments for a function that can accept different combinations of types and numbers of parameters. In fact, the classic 'visitor' pattern is an example of this, done in an OOP style -- but matching makes it much less tedious to write.

Much of the code to do so tends to consist of complex chains of nested if/elif statements, including multiple calls to len(), isinstance() and index/key/attribute access. Inside those branches users sometimes need to destructure the data further to extract the required component values, which may be nested several objects deep.

Pattern matching as present in many other languages provides an elegant solution to this problem. These range from statically compiled functional languages like F# and Haskell, via mixed-paradigm languages like Scala [4] and Rust [3], to dynamic languages like Elixir and Ruby, and is under consideration for JavaScript. We are indebted to these languages for guiding the way to Pythonic pattern matching, as Python is indebted to so many other languages for many of its features: many basic syntactic features were inherited from C, exceptions from Modula-3, classes were inspired by C++, slicing came from Icon, regular expressions from Perl, decorators resemble Java annotations, and so on.
'''.strip().replace('\n', '')

words = text.split()


word_counts = Counter(words)
top_freq = word_counts.most_common(5)
# top_freq: [('to', 12), ('of', 11), ('and', 7), ('languages', 6), ('the', 5)]
print(top_freq)
data_dict = dict(top_freq)


while hapi.is_running:
    hapi.background(bg_col)

    hapi.barchart(
        190, 30, 200, 200, {
        "data": data_dict,
        "mouse_line": True
        }
    )


    hapi.event_loop()
    hapi.flip_display()

pygame.quit()

```


Output:

![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/screen.png)
