title: String Manipulation Functions: The Top 5 You Forgot To Pack
slug: string-manipulation-functions-the-top-5-you-forgot-to-pack
pub: Mon, 22 Jul 2019 15:20:18 +0000
authors: Abdur-RahmaanJ

 String manipulation functions, good ones are available by default in Python. Ignorance make people always re-invent. Python is powerful and … thoughtful. We were strict and choose only 5, the five best. Hope you enjoy it!




### What are string manipulation functions?




String manipulation functions are helper functions used to manipulate strings. If you have let us say ‘ABC’, a nice lowercase function would transform it to ‘abc’. Let us begin our count.




![book case string](https://images.unsplash.com/photo-1479142506502-19b3a3b7ff33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80)


### 1. str.swapcase()




Programmers are familiar with .upper() and .lower() and try to implement case swapping using those two. .swapcase() you’ve guessed it automatically converts the case.





```python

>>> x = 'aaaBBB'
>>> x.swapcase()

'AAAbbb'


```



**Use of swapcase**




* [example1](https://github.com/samtregar/zoomascii/blob/af252c2dbba16dddd2bcd1800bc86f38b2bdb0b2/tests/bench.py#L16)
* [example2](https://github.com/MargusHenning/Programmeerimine/blob/5e9928ee9653fd55b2760a5cf4fd4d7313fe49f7/00-Kodutöö31.10.py#L4)
* [example3](https://github.com/AndrewDuncan/Doublecoset/blob/e29c9aaa483964ae469a0d4f6b3904d61e800dd2/python/genfold/adj_gen.py#L67)




### 2. str.zfill()




Let’s say you want to build a nice table to display numbers as





```python

0000123
0025378
0005234
0012374


```



If you don’t want to worry about indexes etc, zfill is your buddy.





```python

>>> '1234'.zfill(7)

'0001234'


```



zfill() fills in the missing zeros for the given width.




**Use of zfill**




* [example1](https://github.com/coopci/spring-performance/blob/7e30e88d27b687b92fe8617d5e65dc7d5f5a5dd7/gen-class.py#L19)
* [example2](https://github.com/SAMMYKH/comp/blob/0e62861717494b92d682c4d439eb60ba33a558be/board/axent/ag14003/applications/mrwa_vsls/overlay/usr/lib/python2.7/site-packages/rtacomms/rtalog.py#L16)
* [example3](https://github.com/wildcardcorp/samson/blob/9966d23a1ecebb9eeab8490f799d05413d0ac643/tests/primitives/test_camellia.py#L8)




3. str.casefold()
-----------------




Casefold is used to compare strings. It attempts to do so following unicode.





```python

if 'ABC'.casefold() == 'aBc'.casefold():
    pass


```



Question: Is that not the same as str.lower()?




Answer: casefold() is a unicode compliant version, which is not the case for str.lower()




**Use of casefold**




* [example1](https://github.com/pylangstudy/201708/blob/126b1af96a1d1f57522d5a1d435b58597bea2e57/02/01/endswith.py#L7)
* [example2](https://github.com/ThatsGobbles/cheffu-old/blob/dfd8121718f82a5f9288d9acdd0544613e1ad7b9/cheffu/helpers.py#L90)
* [example3](https://github.com/tiberiuv/Information-Retrieval-Search-Engine/blob/c501e20cd1c2e499148942f587851f7fd56d292c/CourseWork%202/util/UEAlite.py#L161)




4. center()
-----------




center() is used to center texts. A cool neatify tool out of the box.





```python

>>> 'abcd'.center(10)


'   abcd   '


```



It also supports a fillchar parameter





```python

>>> 'abcd'.center(10, '?')


'???abcd???'


```



**Use of center**




* [example1](https://github.com/epfeff/smartbetas/blob/9262dd21f0800647e4e723470dfb361c1c464282/smartbetas/i_o.py#L21)




5. expandtabs()
---------------




That one makes real sense in Python. Let’s say you are replacing tabs while reading a python source file or just converting tabs to spaces while building an editor. just do ‘’.expandtabs() and it will be converted!





```python

>>> print('''   abcd
        abcd
    abcd'''.expandtabs(4))

    abcd
        abcd
    abcd

```



**Use of expandtabs**




* [example1](https://github.com/mcaire/umat_nlv_1d/blob/ef4663a03b41873e0122bc9d2cf3c22434d8f60b/abaqus_umat_nlv_beam.py#L53)
* [example2](https://github.com/snebaybay/python/blob/9f22902f1b0ecc13060889b620b0482d58bd7374/django/djangoEnv/lib/python2.7/site-packages/pygraphviz/tests/test_attribute_defaults.py#L16)
* [example3](https://github.com/barkow/linux-can-python/blob/94a7189f46b6d7693dfe0b21ca3872ad867103c4/Tools/scripts/pindent.py#L101)




Python has coool string manipulation functions. We promised 5 and here they are. In the days of viral 10x engineer contents, the casual programmer got high standards to conform to. One of them is knowing the docs thoroughly. But, string functions are a higher priority!




Talking of strings, you might want to know [how to handle curly braces in string formatting](https://www.pythonmembers.club/2018/05/09/handling-curly-braces-in-string-formatting-python/).



