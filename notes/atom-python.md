# Atom for Python

Let's trick [Atom](/notes/atom.md) out to code Python and give you lots of help.

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
