title: Efficient Column Removal in Pandas: Dropping by Index or Range
slug: removing-last-columns-of-excel-dataframe-using-pandas-by-index
pub: 2018-07-22 09:19:28
authors: arj
tags: python, pandas, dataframe, data-cleaning, beginners
category: data science, pandas

When cleaning data in Pandas, we often need to remove columns. While dropping by name (`df.drop(columns=['Name'])`) is common, there are many scenarios where it’s more efficient to drop columns by their **index position**. 

This is particularly useful when:
1.  You have dozens of columns and don't want to type their names.
2.  Your columns have names that change frequently, but their order remains the same.
3.  You want to remove the "last X" columns of a dataset.

---

## The Core Concept: `iloc` and `columns`

To drop columns by index, we first need to identify the column names at those specific positions using the `iloc` or `columns` property.

### 1. Dropping a Single Column by Index
Let's say we want to remove the 3rd column (index 2).

```python
import pandas as pd

df = pd.read_excel("data.xlsx")

# Get the name of the column at index 2
col_to_drop = df.columns[2]

# Drop it
df = df.drop(columns=[col_to_drop])
```

---

## 2. Dropping a Range of Columns

A more powerful technique is to use Python's slicing notation. If you want to drop the first 3 columns:

```python
# Get names of columns 0, 1, and 2
cols_to_drop = df.columns[:3]

df = df.drop(columns=cols_to_drop)
```

---

## 3. Removing the "Last X" Columns

This is a very common task in data cleaning, especially when Excel files have empty columns at the end. In Python, we can use negative indexing to refer to the end of the list.

### To remove the last 2 columns:
```python
# Get the names of the last two columns
last_two = df.columns[-2:]

df = df.drop(columns=last_two)
```

### A "One-Liner" using `iloc`
Alternatively, you can keep only the columns you want using `iloc`. This is often cleaner:

```python
# Keep everything from the start up to the last two columns
df = df.iloc[:, :-2]
```
*The `:` before the comma means "keep all rows." The `:-2` after the comma means "keep all columns except the last two."*

---

## Summary

| Goal | Code Snippet |
| :--- | :--- |
| **Drop by Name** | `df.drop(columns=['ColName'])` |
| **Drop by Index** | `df.drop(df.columns[i], axis=1)` |
| **Drop First 3** | `df.iloc[:, 3:]` (Keeps from 3 onwards) |
| **Drop Last 2** | `df.iloc[:, :-2]` |

## Conclusion

Knowing how to manipulate DataFrames by index allows you to write more flexible and automated data cleaning scripts. Whether you're dealing with raw Excel dumps or scraped web data, mastering `iloc` and `drop` is essential for any aspiring data scientist.

### Related Posts:
*   [Preparing Excel Files for Analysis in Pandas](https://www.pythonkitchen.com/preparing-an-excel-file-for-analysis-using-pandas/)
*   [How to Handle Missing Values in Pandas](https://www.pythonkitchen.com/preparing-an-excel-file-for-analysis-using-pandas/)