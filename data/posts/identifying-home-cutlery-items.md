title: Machine Learning 101: Identifying Kitchen Cutlery with K-NN
slug: identifying-home-cutlery-items
pub: 2018-05-08 06:12:23
authors: arj
tags: opencv, image recognition, project
category: computer vision
related_posts: installing-opencv-on-the-pi3-with-python3-and-usb-webcam,plotting-hotspots-in-mauritius-with-python-and-folium,translating-location-to-map-coordinates

Machine Learning can often feel like a "black box" of complex math and scary terminology like "Tensors" and "Neural Networks." But at its core, Machine Learning is just applied statistics. 

In this project, we’ll build a simple classifier to identify different types of kitchen cutlery—specifically **Bowls**, **Mugs**, and **Plates**—using the **K-Nearest Neighbours (K-NN)** algorithm.

---

## The Concept: Machines Learn from Data

Imagine you have a new object from the kitchen. How do you know if it's a mug or a bowl? You probably look at its dimensions: height and diameter.

*   **Plates:** Wide diameter, very short height.
*   **Mugs:** Narrow diameter, tall height.
*   **Bowls:** Medium diameter, medium height.

In Machine Learning, these dimensions are called **Features**. Our goal is to train a model so that when we give it the features of an unknown item, it can predict the **Category**.

---

## Step 1: Collecting the Data

For this project, I literally took a ruler to my kitchen and measured several items. Here is a sample of the data we collected in a CSV format:

```csv
Diameter,Height,Type
17,5,bowl
15.5,5,bowl
22.5,1,plate
8,7.5,mug
8,9,mug
6,11,mug
24,2.5,plate
26,2,plate
11,8,mug
18,5.5,bowl
```

---

## Step 2: Visualizing the Data

Before we run any math, let's look at the data. By plotting Diameter on the X-axis and Height on the Y-axis, we can see distinct clusters forming.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cutlery.csv")

colors = {'bowl': 'red', 'mug': 'blue', 'plate': 'green'}

plt.figure(figsize=(8, 6))
for i, row in df.iterrows():
    plt.scatter(row['Diameter'], row['Height'], color=colors[row['Type']])
    plt.text(row['Diameter'] + 0.3, row['Height'], row['Type'], fontsize=8)

plt.xlabel("Diameter (cm)")
plt.ylabel("Height (cm)")
plt.title("Cutlery Dimensions Distribution")
plt.show()
```

When you look at the plot, you'll see Mugs in the top left (tall and narrow) and Plates in the bottom right (wide and short).

---

## Step 3: Predicting with K-Nearest Neighbours

The **K-Nearest Neighbours (K-NN)** algorithm is simple: to classify a new, unknown point, we look at the "K" closest points in our dataset. If the majority of those neighbors are "Mugs," then our new point is probably a Mug too!

### The Distance Formula
We calculate the "closeness" using the Euclidean distance formula:
$$Distance = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

### The Python Logic

```python
from math import sqrt

def classify_item(new_diameter, new_height, data):
    distances = []
    for i, row in data.iterrows():
        # Calculate distance from new point to every known point
        d = sqrt((new_diameter - row['Diameter'])**2 + (new_height - row['Height'])**2)
        distances.append((d, row['Type']))
    
    # Sort by distance (closest first)
    distances.sort(key=lambda x: x[0])
    
    # Return the type of the single closest neighbor (K=1)
    return distances[0][1]

# Test with a new unknown item: Diameter 9cm, Height 14cm
new_item = (9, 14)
prediction = classify_item(9, 14, df)
print(f"The unknown item is likely a: {prediction}")
```

---

## Conclusion

This project demonstrates **Supervised Learning**. We provided the computer with "labeled" data (examples with known answers), and it used that information to make predictions about new data.

While our manual implementation works for small datasets, in professional data science, we use libraries like **Scikit-Learn**. Using Scikit-Learn, you can implement K-NN in just three lines of code!

Machine Learning doesn't have to be scary. Sometimes, all you need is a ruler, a CSV file, and a little bit of Python.