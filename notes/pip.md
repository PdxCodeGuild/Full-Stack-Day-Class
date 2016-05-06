# Pip
**Pip** is the Python package installer.
It is very easy to use.

All of these commands start with `pip`, then a sub-command name, then some arguments.

Remember, most of the time you want to run these commands [inside a virtualenv](virtualenv.md).
If you run in a virtualenv, you install packages inside it.
If you run outside a virtualenv, you install system-wide.

## Searching
You can search for all packages with a name or description containing some query text:
```bash
pip search QUERY
```

## Installing
To install the latest version of a package:
```bash
pip install NAME
```

If you need a very specific version of a package you can specify a [version specifier](https://www.python.org/dev/peps/pep-0440/#version-specifiers).
```bash
pip install 'NAME==1.2.3'
```

## Uninstalling
To remove a specific package:
```bash
pip uninstall NAME
```
