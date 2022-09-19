title: Upload your package to Pypi
slug: upload-your-package-to-pypi
pub: Tue, 07 Jan 2020 19:27:36 +0000


To upload your project to Pypi, this assumes you have your setup.py ready




cd into your package directory and type





```python
python setup.py sdist
```



then install twine if you don't have it





```python
python -m pip install twine
```



then create an account on pypi




then type, providing your username and password





```python
twine upload dist/*
```



It should now be uploaded!



