title: Packaging An Sqlite db-included CRUD PyQt5 app using PyInstaller
slug: packaging-an-sqlite-db-included-crud-pyqt5-app-using-pyinstaller
pub: Tue, 31 Dec 2019 20:17:54 +0000


The Python programmer's journey inevitably leads him to one of the black belts of the industry: packaging and distribution. But, particularly in Python, distribution can also be a black beast. We've seen slow and steady progress in the field with the advent of tools like cx\_freeze, pyinstaller and protocols like zipapp. In this post we'll see how to package a realistic PyQt5 app.




As a side note, i was hesitating between titles to choose so i made a poll in our facebook group. This title got far more votes many requests beforehand. I went on with it.




Complexity of the demo app
--------------------------




Since we are focusing on packaging, we deliberately choose a demo that tackles common headaches. We included picture files and sqlite database. We'll package a CRUD app which uses SqlAlchemy. You can use this as a basis for more ambitious projects. Moreover we used some 'good' PyQt5 practices like custom widgets, OOP approach and namespaced functions.




Repo at [PyQt5\_CRUD](https://github.com/Abdur-rahmaanJ/PyQt5_CRUD) 




Project Structure
-----------------




Our project looks like this





```python
project_folder/
    db/
        items.db # created automatically
    pics/
        icon.png
    base.py
    main.py
    models.py
    utils.py
    template.spec # our spec reference
    main.spec # generated, to be modified to match template.spec
    icon.ico # since we are on windows, you can use any file format used by your os
    requirements.txt # what package we'll be using
    README.md # instructions
```



db/ is the folder used for storing databases




pics/ is the picture where pics are stored




models.py is where we'll define our model




main.py is the file we'll run




utils.py contains some utitlities functions




base.py contains some SqlAlchemy configurations




main.spec is the pyinstaller specifications file




App & Code
----------




![](https://www.pythonmembers.club/wp-content/uploads/2019/12/main_screen.jpg)The app we'll be building


It features the minimum working mechanism a CRUD app should have. Let's see what each file contains




base.py
-------





```python
import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils import app_path

engine = create_engine('sqlite:///{}'.format(app_path('db/items.db')))
Session = sessionmaker(bind=engine)

Base = declarative_base()
```






models.py
---------





```python
from sqlalchemy import Column, String

from base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    barcode = Column(String)
    name = Column(String)
```



Our demo product just has a barcode and a name.




utils.py
--------





```python
import os
import sys

from PyQt5 import QtWidgets

def app_path(path):
    frozen = 'not'
    if getattr(sys, 'frozen', False):
            # we are running in executable mode
            frozen = 'ever so'
            app_dir = sys._MEIPASS
    else:
            # we are running in a normal Python environment
            app_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(app_dir, path)


def layout_addWidget(layout, widgets):
    '''adds widgets to layouts'''

    for widget in widgets:
        if isinstance(layout, QtWidgets.QGridLayout):
            layout.addWidget(widget[0], widget[1], widget[2])
        else:
            layout.addWidget(widget)
```



The first function allows you to get the correct resource path like an image right. Just putting pics/icon.png is going to break when using the executable version. So putting 





```python
app_path('pics/icon.png')
```



ensure smooth fetching.




The second function just spares you having to write layout.addWidget many times.




main.py
-------




Let's see our imports





```python
import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from models import Product
from base import Session, engine, Base
from utils import app_path, layout_addWidget
```



We can see that for PyQt5 we imported only QtWidgets. To use a QPushButton we need to write QtWidgets.QPushButton. This takes longer to read but makes you a Qt master, believe me. There are many advantages in doing so, the least of them is easy PySide2 migration




Then we'll see our globals





```python
Base.metadata.create_all(engine)
session = Session()
```



session is used by SqlAlchemy to make queries




Then we have our first custom widget: the AddProduct widget. In the above picture, the complete add product section is defined and manage by the following widget





```python
class AddProduct(QtWidgets.QWidget):

    def __init__(self, view_product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view_product = view_product
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.barcode_label = QtWidgets.QLabel('Enter barcode')
        self.barcode_entry = QtWidgets.QLineEdit()
        self.name_label = QtWidgets.QLabel('Enter Name')
        self.name_entry = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Add')


        self.button.clicked.connect(self.button_clicked)

        layout_addWidget(self.layout, [
            self.barcode_label, 
            self.barcode_entry, 
            self.name_label, 
            self.name_entry,
            self.button
            ])

        self.setLayout(self.layout)

    def clear_textboxes(self):
        self.barcode_entry.setText('')
        self.name_entry.setText('')

    def button_clicked(self):
        product = Product(
            barcode=self.barcode_entry.text(), 
            name=self.name_entry.text())
        session.add(product)
        session.commit()

        self.view_product.display_products()
        self.clear_textboxes()
```



The layout\_addWidget functions come from utils.py




The EditProduct widget manages the edit section. The edit section works as follows: you must input a barcode, then press the load button, then edit.





```python
class EditProduct(QtWidgets.QWidget):

    def __init__(self, view_product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view_product = view_product
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.old_barcode_label = QtWidgets.QLabel('Enter old barcode')
        self.old_barcode_entry = QtWidgets.QLineEdit()
        self.new_barcode_label = QtWidgets.QLabel('Enter new barcode')
        self.new_barcode_entry = QtWidgets.QLineEdit()
        self.name_label = QtWidgets.QLabel('Enter Name')
        self.name_entry = QtWidgets.QLineEdit()
        self.load_button = QtWidgets.QPushButton('Load')
        self.edit_button = QtWidgets.QPushButton('Edit')

        self.load_button.clicked.connect(self.load_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)
        
        layout_addWidget(self.layout, [
            self.old_barcode_label, 
            self.old_barcode_entry, 
            self.new_barcode_label, 
            self.new_barcode_entry,
            self.name_label, 
            self.name_entry,
            self.load_button,
            self.edit_button
            ])

        self.setLayout(self.layout)

    def clear_textboxes(self):
        self.old_barcode_entry.setText('')
        self.new_barcode_entry.setText('')
        self.name_entry.setText('')

    def load_button_clicked(self):
        check_barcode = self.old_barcode_entry.text()
        record = session.query(Product).filter(Product.barcode == check_barcode).first()
        self.new_barcode_entry.setText(check_barcode)
        self.name_entry.setText(record.name)

    def edit_button_clicked(self):
        check_barcode = self.old_barcode_entry.text()
        record = session.query(Product).filter(Product.barcode == check_barcode).first()
        
        record.barcode = self.new_barcode_entry.text()
        record.name = self.name_entry.text()

        self.view_product.display_products()
        self.clear_textboxes()
```



DeleteProduct manages the delete section





```python
class DeleteProduct(QtWidgets.QWidget):

    def __init__(self, view_product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view_product = view_product
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.barcode_label = QtWidgets.QLabel('Enter barcode')
        self.barcode_entry = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Delete')

        self.button.clicked.connect(self.button_clicked)

        layout_addWidget(self.layout, [
            self.barcode_label, 
            self.barcode_entry,
            self.button
            ])

        self.setLayout(self.layout)

    def clear_textboxes(self):
        self.barcode_entry.setText('')

    def button_clicked(self):
        check_barcode = self.barcode_entry.text()
        session.query(Product).filter(Product.barcode == check_barcode).delete()
        self.clear_textboxes()
        self.view_product.display_products()
```



ViewProduct is the display area





```python
class ViewProduct(QtWidgets.QWidget):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop)
        

        self.data_area = QtWidgets.QWidget()
        self.data_area_layout = QtWidgets.QVBoxLayout(self.data_area)
        self.data_area_layout.setAlignment(QtCore.Qt.AlignTop)
        self.display_products()

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(self.data_area)
        self.scroll_area.setWidgetResizable(True)

        layout.addWidget(self.scroll_area)

    def clear_area(self):
        for i in reversed(range(self.data_area_layout.count())): 
            self.data_area_layout.itemAt(i).widget().setParent(None)

    def display_products(self):
        self.clear_area()
        products = session.query(Product).all()

        record_string = '''
        <table>
            <tr>
                <th>id</th>
                <th>barcode</th>
                <th>name</th>
            </tr>
        '''
        self.data_area_layout.addWidget(QtWidgets.QLabel('PRODUCTS'))

        for product in products:
            record_string += '''
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            '''.format(product.id, product.barcode, product.name)
        record_string += '''
        </table>'''
        self.data_area_layout.addWidget(QtWidgets.QLabel(record_string))
```



Then the main window using all these widgets





```python
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        # win initialisations
        self.layout = QtWidgets.QGridLayout()
        self.window = QtWidgets.QWidget()
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)
        self.setWindowTitle('Products')
        self.setWindowIcon(QtGui.QIcon(app_path('pics/icon.png'))) 

        self.view_product_widget = ViewProduct()
        self.add_product_widget = AddProduct(self.view_product_widget)
        self.edit_product_widget = EditProduct(self.view_product_widget)
        self.delete_product_widget = DeleteProduct(self.view_product_widget)

        layout_addWidget(self.layout, [
            (self.add_product_widget, 0, 0),
            (self.edit_product_widget, 0, 1),
            (self.delete_product_widget, 0, 2),
            (self.view_product_widget, 0, 3),
            ])
```



And finally to finish, we have our main





```python
if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
```



template.spec
-------------




The spec file is normally generated using the command pyinstaller main.py




However you can save it as template.spec





```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
         ( './pics/*', 'pics' ),
         ( './db/*', 'db' ),
         ]

a = Analysis(['main.py'],
             datas = added_files,
             pathex=['<project_folder_path>'],
             binaries=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='icon.ico' )

```



The added\_files variable adds everything in the designated folder, it's one of the tricks to get our app working. Notice the wildcard operator (\*).





```python
added_files = [
         ( './pics/*', 'pics' ),
         ( './db/*', 'db' ),
         ]
```



then we add it in





```python
a = Analysis(['main.py'],
             datas = added_files, # here
```



Run instructions
----------------




Make sure you have the required packages. Run 





```python
python -m pip install -r requirements.txt
```



To test if all is well, run python main.py and see if the app appears




Next we generate our main.spec using





```python
pyinstaller main.py -F
```



-F tells pyinstaller that we need a single file executable




Now add this after block\_cipher





```python
added_files = [
         ( './pics/*', 'pics' ),
         ( './db/*', 'db' ),
         ]
```



Then change this





```python
a = Analysis(['main.py'],
             ...
             binaries=[],
             datas=[],
             ...
```



to this





```python
a = Analysis(['main.py'],
             ...
             binaries=[],
             datas=added_files,
             ...
```



You might want to change the last part where console=True to





```python
console=False,
icon='icon.ico' )
```



In short we copied template.spec's content into main.spec keeping pathex= intact.




Build your executable using 





```python
pyinstaller main.spec
```



You will get two new folders





```python
project_folder/
    db/
        items.db
    pics/
        icon.png
    build/ # new
        ...
    dist/
        main.exe # new
    base.py
    main.py
    models.py
    utils.py
    template.spec
    main.spec
    icon.ico
    requirements.txt
    README.md
```



Under dist/ you should see your executable




Dealing with headaches!
-----------------------




Normally you should have a working executable file, however i've discovered that while the exec file can work well on your PC, it might not work so well on another person PC due to some internal hardcoding of paths. The issue apparently varies from PyQt5 version to version. In case you encounter this error, downgrade some 0.0.01 version back or forward.




Words of caution
----------------




This app is without safety nets and was intended as a packaging demo. 







*You can download the repo here: [PyQt5\_CRUD](https://github.com/Abdur-rahmaanJ/PyQt5_CRUD) . Anything unclear, mail me at <arj.python at gmail dot com>*



