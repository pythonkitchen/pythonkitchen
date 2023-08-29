title: PyQt5 / PySide2 QTableView how to find out if row is selected and which one in Python?
slug: pyqt5-pyside2-qtableview-how-to-find-out-if-row-is-selected-and-which-one-in-python
pub: 2019-11-06 18:19:38
authors: arj
tags: pyqt5,pyside2
category: gui,pyside

Question: I have a QTableView in PyQT5 / PySide2

I want to
* Know if a row is selected (my tableview is set to select by rows)
* Know which row is selected


Thanks

Answer:

A bit hackishly though:

```python
select = tableview.selectionModel()

selected = select.selectedRows()

if selected:
      print(selected[0].row())
```

but that does it well:

```python
selected = select.hasSelection()
```

