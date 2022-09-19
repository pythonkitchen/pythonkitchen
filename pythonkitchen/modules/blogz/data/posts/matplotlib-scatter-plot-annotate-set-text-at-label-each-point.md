title: matplotlib scatter plot annotate / set text at / label each point
slug: matplotlib-scatter-plot-annotate-set-text-at-label-each-point
pub: Tue, 08 May 2018 04:32:11 +0000


a hard question in matplotlib is to annotate each point with a text or label. answers range from ax.annotate to some more weird stuffs. fortunately, the answer is a simple one! this question poses itself quite often in scatter plots




the key
-------




without beating around the bush, the answer is using **pyplot.text** found [here](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html)




demo
----




code :





```python
import matplotlib.pyplot as plt

# simulating a pandas df['type'] column
types = ['apple', 'orange', 'apple', 'pear', 'apple', 'orange', 'apple', 'pear']
x_coords = [10, 10, 5, 4, 3, 20, 19, 21]
y_coords = [21, 23, 12, 21, 10, 20, 14, 2]

for i,type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x+0.3, y+0.3, type, fontsize=9)
plt.show()
```






output :




![matplotlib label annotate points](https://www.pythonmembers.club/wp-content/uploads/2018/05/matplotlib_label_points-1.png)matplotlib label points

