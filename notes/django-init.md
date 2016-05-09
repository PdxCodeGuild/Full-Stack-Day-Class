# Django Init
Django applications have to follow a very specific source and module structure.
```
YOUR_APP/
    manage.py
    YOUR_APP/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

I will call the top level `YOUR_APP` directory the **repository root** and the inner `YOUR_APP` directory the **application root**.

The Django package gives you a script which will set this up for you.
Run this command from inside the directory you setup for this application.
```bash
django-admin startproject YOUR_APP .
```
You'll only have access to this script from inside a virtualenv that has Django installed.

These should live alongside the [standard Python application files](py-app-structure.md).

You should commit all of these files.
