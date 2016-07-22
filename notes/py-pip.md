# Pip and PyPI

**Pip** is the Python package installer.
It looks to the public **Python Package Index** or **PyPI** for a [listing of all known packages](https://pypi.python.org/pypi) and to actually download them.
It is very easy to use.

All of these commands start with `pip`, then a sub-command name, then some arguments.

Remember, most of the time you want to run these commands [inside a virtualenv](/notes/py-virtualenv.md).
If you run in a virtualenv, you install packages inside it.
If you run outside a virtualenv, you install system-wide.

## Search

You can search for all packages with a name or description containing some query text:

```bash
pip search QUERY
```

## Install

To install the latest version of a package:

```bash
pip install NAME
```

If you need a very specific version of a package you can specify a [version specifier](https://www.python.org/dev/peps/pep-0440/#version-specifiers).

```bash
pip install 'NAME==1.2.3'
```

## List

To list all of the packages currently installed:

```bash
pip list
```

## Uninstall

To remove a specific package:

```bash
pip uninstall NAME
```
