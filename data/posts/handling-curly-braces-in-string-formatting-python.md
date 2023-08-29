title: handling curly braces in string formatting - python
slug: handling-curly-braces-in-string-formatting-python
pub: 2018-05-09 08:35:34
authors: arj
tags: 
category: language core

let us say you want to print :

```python
{text}
```

using

```python
'{ {} }'.format(content)
```

how to escape the {}?

```python
'\{ {} \}'.format(content)
```

works not
the answer
==========


the answer is to double curly braces like that :

```python
'{{ {} }}'.format(content)
```

simple !
