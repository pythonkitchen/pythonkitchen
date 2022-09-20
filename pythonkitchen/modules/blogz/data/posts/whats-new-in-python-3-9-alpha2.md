title: What's New in Python 3.9 alpha2?
slug: whats-new-in-python-3-9-alpha2
pub: Tue, 24 Dec 2019 09:27:17 +0000
authors: Abdur-RahmaanJ

Python is set to release a new version next year, the shiny 3.9. This one omitted the sys.argv change rolled back in alpha2 Here's our take of the most noticeable changes:




### Keyword Arguments Get Some Boost




improved





```python
sebastian@seberg-x1 ~/python-dev/bin
 % ./python3 -m timeit -s 'i = 4' 'i.to_bytes(length=5, byteorder="big", signed=True)'
1000000 loops, best of 5: 205 nsec per loop
sebastian@seberg-x1 ~/python-dev/bin
 % ./python3 -m timeit -s 'i = 4' 'i.to_bytes(length=5, byteorder="big", signed=True)'
1000000 loops, best of 5: 207 nsec per loop
```



original





```python
sebastian@seberg-x1 ~/python-dev/bin
 % ./python3 -m timeit -s 'i = 4' 'i.to_bytes(length=5, byteorder="big", signed=True)'
1000000 loops, best of 5: 221 nsec per loop
sebastian@seberg-x1 ~/python-dev/bin
 % ./python3 -m timeit -s 'i = 4' 'i.to_bytes(length=5, byteorder="big", signed=True)'
1000000 loops, best of 5: 218 nsec per loop
```



###  Audit hooks added for [`sys.excepthook()`](https://docs.python.org/3.9/library/sys.html#sys.excepthook) and [`sys.unraisablehook()`](https://docs.python.org/3.9/library/sys.html#sys.unraisablehook)




Audit hooks were added in PEP 578. It basically allows you to monitor low-level details. It's aim is to monitor behaviors of Python scripts more accurately. Example of use in the wording of the PEP:





>  Auditing bypass can occur when the typical system tool used for an action would ordinarily report its use, but accessing the APIs via Python do not trigger this. For example, invoking "curl" to make HTTP requests may be specifically monitored in an audited system, but Python's "urlretrieve" function is not. 
> 
> 




###  Calling `replace` on a code object now raises the `code.__new__` audit event.




 The code object is returned when using the in-built compile() function on some codes. The corresponding C code:





```python
   if (PySys_Audit("code.__new__", "OOOiiiiii",
                    co_code, co_filename, co_name, co_argcount,
                    co_posonlyargcount, co_kwonlyargcount, co_nlocals,
                    co_stacksize, co_flags) < 0) {
        return NULL;
    }
```



###  Thread stack size set to 8 Mb for debug builds on Android




An initiated script crashes on Android API 24 but only in debug mode. The maximum recursion limit was reduced from 1000 to 100.




In Python you can't recurse more than some limit. 





```python
>>> import sys
>>> sys.getrecursionlimit()
1000
```



 The above patch was implemented by defining THREAD\_STACK\_SIZE to 8mb





```python
define THREAD_STACK_SIZE    0x800000
```



###  Added `__floor__` and `__ceil__` method to float object




Was not previously implemented. Also added tests.




###  Use of `python -m pip` instead of `pip` to upgrade dependencies in venv




In [cpython](https://github.com/python/cpython/tree/d9aa216d49423d58e192cd7a25016f90fe771ce7)/[Lib](https://github.com/python/cpython/tree/d9aa216d49423d58e192cd7a25016f90fe771ce7/Lib)/[venv](https://github.com/python/cpython/tree/d9aa216d49423d58e192cd7a25016f90fe771ce7/Lib/venv)/**\_\_init\_\_.py** alongsize some other changes, the below update sets python -m pip install as default for dependencies upgrade





```python
        if sys.platform == 'win32':
            python_exe = os.path.join(context.bin_path, 'python.exe')
        else:
            python_exe = os.path.join(context.bin_path, 'python')
        cmd = [python_exe, '-m', 'pip', 'install', '--upgrade']
        cmd.extend(CORE_VENV_DEPS)
        subprocess.check_call(cmd)
```



###  Excape key also closes IDLE completion windows




Many keys are used in auto completion. The escape key was just added 





```python
KEYPRESS_SEQUENCES = ("<Key>", "<Key-BackSpace>", "<Key-Return>", "<Key-Tab>",
                      "<Key-Up>", "<Key-Down>", "<Key-Home>", "<Key-End>",
                      "<Key-Prior>", "<Key-Next>", "<Key-Escape>")
```






That's was my funnified personal pick!



