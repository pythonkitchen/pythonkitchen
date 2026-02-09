title: How to Annotate Each Point in a Matplotlib Scatter Plot
slug: matplotlib-scatter-plot-annotate-set-text-at-label-each-point
pub: 2018-05-08 04:32:11
authors: arj
tags: python, matplotlib, data-visualization, pandas, plotting
category: data science

One of the most frequent questions when working with Matplotlib is: **"How do I label each point in my scatter plot?"** 

While plotting coordinates is straightforward, adding descriptive text to those points can quickly become messy, especially when points are crowded together. In this guide, we'll look at the simplest way to achieve this using `plt.text` and discuss more advanced options for professional-grade visualizations.

---

## The Simple Method: `plt.text()`

The most direct way to add a label to a specific coordinate is the `text()` function. You simply provide the X position, Y position, and the string you want to display.

### Basic Implementation

When working with a list of points (like from a Pandas DataFrame), you can iterate through them and apply the label one by one:

```python
import matplotlib.pyplot as plt

# Sample data
cities = ['London', 'Paris', 'New York', 'Tokyo', 'Sydney']
x_coords = [10, 15, 5, 25, 30]
y_coords = [20, 25, 10, 30, 5]

plt.figure(figsize=(8, 6))
plt.scatter(x_coords, y_coords, color='blue')

# Iterate and annotate
for i, label in enumerate(cities):
    # We add a small offset (+0.5) so the text doesn't sit directly on the dot
    plt.text(x_coords[i] + 0.5, y_coords[i] + 0.5, label, fontsize=10)

plt.title("City Coordinates with Labels")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

---

## Advanced Method: `ax.annotate()`

While `plt.text` is easy, `ax.annotate()` is more powerful. It allows you to create arrows pointing to the data points and gives you more control over the "offset" (moving the text relative to the point).

```python
fig, ax = plt.subplots()
ax.scatter(x_coords, y_coords)

for i, label in enumerate(cities):
    ax.annotate(label, (x_coords[i], y_coords[i]), 
                textcoords="offset points", # How to position the text
                xytext=(0,10),               # Distance from text to points (x,y)
                ha='center')                # Horizontal alignment
```

---

## The "Overlapping" Problem

If your scatter plot has dozens of points, `plt.text` will likely cause labels to overlap, making them unreadable. 

### The Pro Solution: `adjustText`
If you are doing serious data science, there is a fantastic library called `adjustText` that automatically moves labels so they don't overlap.

```bash
pip install adjustText
```

Then in your code:
```python
from adjust_text import adjust_text

texts = []
for i, label in enumerate(cities):
    texts.append(plt.text(x_coords[i], y_coords[i], label))

# This one line handles all the magic of preventing overlaps!
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))
```

## Summary
*   Use **`plt.text()`** for quick, simple labels on a few points.
*   Use **`ax.annotate()`** if you need arrows or more precise positioning.
*   Use **`adjustText`** if you have many points and want a clean, professional look without overlaps.

Visualizing data is about telling a story—make sure your labels are clear so your audience can read it!