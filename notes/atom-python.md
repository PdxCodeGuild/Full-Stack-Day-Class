# Atom for Python

For this class you will be using [Atom](https://atom.io) as the text editor of choice.
Even if you are more familiar with other coding text editors, please use Atom in this course.
This is so you all will have access to the same tools and can help each other out.

Let's trick Atom out to code Python and give you lots of help.

## Linter

First, let's install a Python **linter** that will warn you in the editor when you make mistakes.
Immediate feedback is useful.

```bash
pip install flake8 pep8-naming flake8-quotes flake8-import-order flake8-docstrings
apm install linter linter-flake8
```

Then save [Flake8's config](/.flake8) in `.flake8` in your repo root.

## Formatter

Second, let's install a formatter.
It will automatically make your code conform to proper Python style, so you don't have to do tedious edits.

```bash
pip install yapf isort
apm install python-yapf python-isort
```

Then save [YAPF's config](/.style.yapf) in `.style.yapf` in your repo root.
