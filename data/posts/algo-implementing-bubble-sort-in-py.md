title: Implementing Bubble Sort in Python
slug: implementing-bubble-sort-in-python
pub: 2026-11-28
authors: arj
tags: algorithm
category: algorithm
related_posts: armstrong-numbers

Bubble sort is a *sorting algorithm*. 

> [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort), sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the input list element by element, comparing the current element with the one after it, swapping their values if needed. These passes through the list are repeated until no swaps have to be performed during a pass, meaning that the list has become fully sorted. The algorithm, which is a comparison sort, is named for the way the larger elements "bubble" up to the top of the list.

Give this array:

```
[1, 8, 3, 2] 
```

It goes like this:

```
[1, 8, 3, 2] # 1 < 8 - no swap 
-----

[1, 8, 3, 2] # 8 > 3 - swap
    ----

[1, 3, 8, 2] # 8 > 2 - swap
       ----

[1, 3, 2, 8] # 1 < 3 - no swap
-----

[1, 3, 2, 8] # 3 > 2 - swap
    ----

[1, 2, 3, 8] # 3 < 8 - no swap
       ----

```

A typical implementation goes like this 

```

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
    
```


### Notes

- The `temp` part is how we do things in other languages
- The `- i` in the inner loop skips uneeded passes.