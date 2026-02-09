title: Python Virtual Environments on Windows: A Complete Guide
slug: venv-usage-on-windows-activate-and-deactivate
pub: 2018-08-10 18:46:37
authors: arj
tags: python, venv, windows, beginners, tutorial
category: virtual environment

If you're starting multiple Python projects, you will quickly run into a problem: one project needs Version 1.0 of a library, while another needs Version 2.0. If you install everything globally, you'll end up with a broken mess.

This is where **Virtual Environments (venv)** come in. They allow you to create isolated "bubbles" for each project, ensuring that your dependencies never clash. In this guide, we'll walk through exactly how to use them on Windows.

---

## 1. Creating the Environment

Open your Command Prompt or PowerShell and navigate to your project folder. Run the following command:

```bash
# General syntax: python -m venv [folder_name]
python -m venv .venv
```

*Note: `.venv` is the standard name for the folder, but you can name it whatever you like (e.g., `myenv`).*

---

## 2. Activating the Environment

Creating the folder isn't enough; you have to tell your terminal to start using it. The activation command depends on whether you are using the old **Command Prompt (CMD)** or the modern **PowerShell**.

### For Command Prompt (CMD):
```cmd
.venv\Scripts\activate
```

### For PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

**How do I know it worked?**
You should see the name of your environment in parentheses at the start of your command prompt line, like this:
`(.venv) C:\Users\Projects\MyProject>`

---

## 3. Installing Packages

Once activated, any package you install using `pip` will be contained entirely within that folder.

```bash
pip install flask
```

If you look inside `.venv\Lib\site-packages`, you will see Flask and its dependencies sitting right there!

---

## 4. Deactivating

When you're done working, or if you want to switch to another project, simply type:

```bash
deactivate
```

Your prompt will return to normal, and you will be back in your global Python environment.

---

## Common Issues on Windows

### "Running Scripts is Disabled" (PowerShell)
If you get a red error in PowerShell saying "Scripts cannot be loaded," it’s because Windows blocks third-party scripts by default. You can fix this by running this command once as an Administrator:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Summary Checklist
1.  **Create:** `python -m venv .venv`
2.  **Activate:** `.venv\Scripts\activate`
3.  **Use:** `pip install ...`
4.  **Finish:** `deactivate`

Mastering virtual environments is the first step toward becoming a professional Python developer. It keeps your computer clean and your projects reproducible!