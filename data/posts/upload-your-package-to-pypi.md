title: Upload your package to Pypi
slug: upload-your-package-to-pypi
pub: 2020-01-07 19:27:36
authors: arj
tags: pypi, packaging, software delivery
category: devops
related_posts: publishing-using-uv,rye-package-manager,copy-files-to-aws-ec2


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



