title: Python: Running makefile on windows using git mingw bash
slug: python-running-makefile-on-windows
pub: 2020-11-21 07:50:49
authors: arj
tags: build tools, windows, gnu make
category: devops
related_posts: venv-usage-on-windows-activate-and-deactivate,publishing-using-uv,rye-package-manager

Linux owners configure makefiles so as to have easy commands to perform operations such as `make dependencies` to pip install required packages. Here are the dry simple steps to run makefiles in Python projects on Windows.

1. Download [git for windows](https://git-scm.com/download/win). You should get git bash, git gui etc
2. Download the [mingw GUI setup](https://sourceforge.net/projects/mingw/files/Installer/mingw-get-setup.exe/download). Install it wherever you want. After running the setup you should get a screen like that:


![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/setup.exe_.png)
3. On continuing you should get under **all packages**. Search for make, class bin. Right click and select mark for installation


![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/setup.exe_.png)
4. Under installation, select apply changes


![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/apply_changes.png)
5. Confirm by clicking on apply


![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/confirm_apply.png)
6. My git for windows' migw is installed at `C:\Program Files\Git\mingw32` and my mingw get is installed at `C:\MinGW`. We need to merge the contents on the mingw32 folder with the MinGW. Ctrl+a to select all folder in MinGW then right click and copy. Then go to mingw32 folder and click paste. When asking is merge, say yes. If same files skip



- Verify if there is `venv/` in project gitignore. If not add it and reapply gitignore by using the following command [(see accepted answer)](https://stackoverflow.com/questions/19663093/apply-gitignore-on-an-existing-repository-already-tracking-large-number-of-file)

- create a new virtual environent.



```python
python -m venv venv

```

9. activate the env



```python
cd venv
cd scripts
. activate

```

note the space between . and activate

10. cd back `cd ../..`



now try out any command listed [here](https://github.com/pandas-dev/pandas-blog) for example `make dependencies`

Forgot to say under bin rename `mingw-get.exe` to `make.exe`

Anything mail me <arj.python at gmail dot com>


