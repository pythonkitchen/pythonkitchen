title: Pyside2 / PyQt5 Extract Data From QFormLayout
slug: pyside2-pyqt5-extract-data-from-qformlayout
pub: 2020-02-09 10:16:21
authors: arj
tags: gui,layout
category: pyqt5,pyside



```python
import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Organiser')

        self.win = QtWidgets.QWidget()
        self.layout = QtWidgets.QFormLayout()

        # You can't really extract data 
        # from the layout. You can predefine
        # the widgets though.
        self.name = QtWidgets.QLineEdit()
        self.surname = QtWidgets.QLineEdit()
        self.pet_name = QtWidgets.QLineEdit()
        self.get_data_b = QtWidgets.QPushButton('get data')
        self.get_data_b.clicked.connect(self.get_data)

        # and use them here
        self.layout.addRow(QtWidgets.QLabel("Name:"), self.name)
        self.layout.addRow(QtWidgets.QLabel("Surname:"), self.surname)
        self.layout.addRow(QtWidgets.QLabel("Pet Name:"), self.pet_name)
        self.layout.addRow(self.get_data_b)

        self.win.setLayout(self.layout)
        self.setCentralWidget(self.win)

    def get_data(self):
        print(self.name.text())
        print(self.surname.text())
        print(self.pet_name.text())


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```



![](https://www.pythonmembers.club/wp-content/uploads/2020/02/extract_form_layout.png)


[from this user](https://github.com/Abdur-rahmaanJ)



