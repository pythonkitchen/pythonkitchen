title: Why I Prefer Rye: Rye v/s PDM v/s Poetry
slug: why-rye-over-pdm-poetry
pub: 2024-03-14 07:00:00
authors: arj
tags: rye, package management, toolchain
category: devops
related_posts: install-pipx-mint-ubuntu,publishing-using-uv,venv-usage-on-windows-activate-and-deactivate

Rye is impressive both as a package manager and as an onboarding tool for Python projects. I have done quite some workshops/sessions and one main pain point is getting Python up and running. Rye in addition to managing dependencies, also manages Python versions. And, being written in Rust guarantees some out-of-the-world speed. It also imports the cargo experience to Python.

Rye can be used on Windows, Mac and Linux. A typical install of Rye also installs Python by default.

```
$ curl -sSf https://Rye-up.com/get | bash
```

Rye is thoughtful and comes with these commands:

```
$ rye self update
$ rye self uninstall
```

To create a project:

```
$ rye init project
$ cd project
```

After adding dependencies, we have to sync it with the virtual env.
The add command adds it to pyproject.toml

```
$ rye add requests
$ rye sync
```

If we want to run commands like flask run for example, Rye has the run command. `Rye run <cli>`/

```
$ rye run flask run
```

If you want to run `flask run` only, you just have to activate the virtual environment.

You can check installed python versions using

```
$ rye toolchain list # try adding --downloadable
```

Rye supports locking but as always, it's platform-specific.

Rye also allows you to publish your package.

```
$ rye build
$ rye publish
```

Rye, true to the cargo spirit has the fmt command XD

```
$ rye fmt
$ rye lint
```

It is to be noted that you can manage Python versions on your PC via Rye.

Last, but not least, you can add your own command alias for other commands and env variables and add submodules managed by Rye.

## Rye v/s PDM v/s Poetry

I tried PDM and Poetry but never settled on them for daily usage. Rye in contrast caught my approval.


|  | PDM | Poetry | Rye |
| :--- | :--- | :--- | :--- |
| Install not needing Python | x |  | x |
| Can publish | x | x | x |
| Lock file | x | x | x |
| Multiple resolvers |  |  | x |
| Easing Rust development |  |  | x |
| Formatting tools included |  |  | x |
| Can install and manage Python versions |  |  | x |


- Rye intro: [https://www.youtube.com/watch?v=q99TYA7LnuA](https://www.youtube.com/watch?v=q99TYA7LnuA)
- Rye docs: [https://rye-up.com/](https://rye-up.com/)