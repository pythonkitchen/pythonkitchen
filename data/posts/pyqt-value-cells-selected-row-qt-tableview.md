title: PyQt5 / PySide2: How to Get Values from a Selected QTableView Row
slug: pyqt5-value-cells-selected-row-qtview
pub: 2019-01-21 07:43:27
authors: arj
tags: pyqt, qtableview, data handling
category: gui development
related_posts: pyqt5-pyside2-qtableview-how-to-find-out-if-row-is-selected-and-which-one-in-python,pyside2-pyqt5-extract-data-from-qformlayout,a-fix-to-tkinter-output-not-showing

When building desktop applications with PyQt5 or PySide2, the `QTableView` is the go-to widget for displaying spreadsheet-like data. A common requirement is to retrieve the data from a row when a user clicks on it.

In this guide, we'll show you the most efficient way to access cell data using the **Selection Model** and the `sibling()` method.

---

## The Core Solution

To get data from a selected row, you first need to access the table's `selectionModel()`. Once you have the current index, you can "look sideways" to other columns in that same row using the `sibling()` function.

### Code Snippet

```python
# 1. Get the selection model
selection_model = tableview.selectionModel()

if selection_model.hasSelection():
    # 2. Get the index of the currently clicked cell
    current_index = selection_model.currentIndex()
    row = current_index.row()
    
    # 3. Use sibling to get data from other columns in the same row
    # sibling(row, column)
    id_val = current_index.sibling(row, 0).data()
    name_val = current_index.sibling(row, 1).data()
    
    print(f"Selected Row {row}: ID={id_val}, Name={name_val}")
```

---

## A Complete, Runnable Example

Here is a full Python script demonstrating a functional table with a "Get Selection" button.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class TableApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Table Selection Demo")
        self.setGeometry(100, 100, 400, 300)

        # 1. Setup the Model
        self.model = QStandardItemModel(4, 2)
        self.model.setHorizontalHeaderLabels(['ID', 'Name'])
        
        data = [('1', 'Alice'), ('2', 'Bob'), ('3', 'Charlie')]
        for r, (uid, name) in enumerate(data):
            self.model.setItem(r, 0, QStandardItem(uid))
            self.model.setItem(r, 1, QStandardItem(name))

        # 2. Setup the View
        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QTableView.SelectRows) # Select full rows

        # 3. Setup Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        
        btn = QPushButton("Print Selected Data")
        btn.clicked.connect(self.print_selection)
        layout.addWidget(btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def print_selection(self):
        index = self.table.selectionModel().currentIndex()
        if index.isValid():
            row = index.row()
            # Get data from column 1 (Name)
            name = index.sibling(row, 1).data()
            print(f"You selected: {name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableApp()
    window.show()
    sys.exit(app.exec_())
```

---

## Why use `sibling()`?

Using `sibling(row, column)` is considered the best practice in Qt's Model/View architecture because:
1.  **Safety:** It ensures you are looking at the data relative to the current selection.
2.  **Performance:** It directly accesses the model's index without needing to loop through the entire dataset.
3.  **Flexibility:** It works even if your table is sorted or filtered.

## Summary Checklist
*   Set `selectionBehavior` to `SelectRows` if you want the whole row highlighted.
*   Check if `hasSelection()` or `isValid()` is true before accessing data to avoid crashes.
*   Use `index.row()` to identify the row number.
*   Use `index.sibling(row, col).data()` to extract the actual value.

Happy coding with PyQt!