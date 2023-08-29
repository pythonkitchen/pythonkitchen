title: PyQt5 / PySide2 How to get value of cells of selected row in QTableView in Python?
slug: pyqt5-value-cells-selected-row-qtview
pub: 2019-01-21 07:43:27
author: arj

Question:

My QTableView is set to select by rows only. How do i get the value of cells in the selected row?

  


Answer:

```
selection_model = tableview.selectionModel()


        if selection_model.hasSelection():


           _index = selection_model.currentIndex()  
             first_cell = _index.sibling(_index.row(), 0).data() # replace the 0 by the desired index  
             second_cell = _index.sibling(_index.row(), 1).data() 

```
