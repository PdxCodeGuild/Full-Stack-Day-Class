# Django Init

Django applications have to follow a very specific source and module structure.

```text
PROJECT_NAME/
    DJANGO_APP_NAME/
        __init__.py
        admin.py
        conftest.py
        settings.py
        static/
            DJANGO_APP_NAME/
                YOUR_LOGO.png
                YOUR_STYLE.css
                YOUR_EVENT_HANDLERS.js
                ...
        templates/
            DJANGO_APP_NAME/
                YOUR_INDEX.html
                YOUR_PROFILE_PAGE.html
                ...
        urls.py
        views.py
        wsgi.py
        YOUR_LOGIC_CODE.py
        YOUR_MODULE/
            ...
        ...
    manage.py
    pytest.ini
    ...
```

I will call the `DJANGO_APP_NAME` directory the **Django application root**.
For our basic projects, `DJANGO_APP_NAME` should be the same as `PROJECT_NAME`.

Basically _all_ of the files you need to make are in this _inner_ directory.
This is a common source of things not working.

Use the following steps to setup your Django app.
You should commit all of these files.

If you are on macOS or Linux, I have a bash script that will perform all of the following steps for you: [django-init.sh](/bin/django-init.sh).

## 0. Setup Python App

First, follow the [standard Python application files](/notes/py-app-structure.md).
Install the `django` package in your virtualenv.

## 1. Create Django App

The Django package gives you a script to setup this structure.
Run this command from inside your _project root_.

```bash
django-admin startproject DJANGO_APP_NAME .
```

**Note the separate period at the end.**

You'll _only have this script_ from inside a virtualenv that has Django installed.

## 2. Install App

Open up `settings.py` and add whatever app name you chose to the `INSTALLED_APPS` variable.

```py
INSTALLED_APPS = [
    'DJANGO_APP_NAME',
    'django.contrib.admin',
    ...
]
```

## 3. Update Git Ignore

Ensure that your project root `.gitignore` file contains `db.sqlite3`, `staticfiles`, and `mediafiles`.
Consult [this example file](/demos/example_gitignore) or [notes on Git ignore](/notes/git-ignore.md).

## 4. Create Views

Create an empty `views.py` in the Django application root for your [views](/notes/django-views.md).

```bash
touch DJANGO_APP_NAME/views.py
```

## 4. Create Models

Create an empty `models.py` in the Django application root for your [models](/notes/django-models.md).
Set up some of the initial built-in models by migrating right off the bat.

```bash
touch DJANGO_APP_NAME/models.py
python manage.py migrate
```

Remember to [migrate](/notes/django-models.md#migrating) whenever you update your models.

## 5. Connect Doctests

We'll be using the [py.test](http://docs.pytest.org/en/latest/) to run our doctests.
First, install `pytest` and `pytest-django` then remember to re-freeze your requirements.

```bash
pip install pytest pytest-django
pip freeze > requirements.txt
```

To do that, we need to set up two files.

Put the following in `pytest.ini` in your project root, replacing `DJANGO_APP_NAME` only with your actual name:

```
[pytest]
addopts = --doctest-modules
testpaths = DJANGO_APP_NAME
DJANGO_SETTINGS_MODULE = DJANGO_APP_NAME.settings
```

In `DJANGO_APP_NAME/conftest.py` put the contents of [this pytest configuration file](/demos/example_conftest.py).

You can then run tests with `pytest` or in PyCharm by adding a "Python tests -> py.test" run configuration and selecting your Django application root as the "target".

## 6. Create Templates Directory

Create an empty [templates](/notes/django-templates.md) directory for your HTML.
Yes, it's redundant, but under `templates` in your Django application root, you should make another directory named your app name.

```bash
mkdir -p DJANGO_APP_NAME/templates/DJANGO_APP_NAME
```

## 7. Create Static Files Directory

Create an empty [static files](/notes/django-static-files.md) directory for images, CSS, and JS.
Yes, it's redundant, but under `static` in your Django application root, you should make another directory named your app name.

```bash
mkdir -p DJANGO_APP_NAME/static/DJANGO_APP_NAME
mkdir -p staticfiles
```

Add to the bottom of `settings.py`.

```py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## 8. Create Media Files Directory

If your Django application needs to handle user uploads or **media**, setup a local directory to store and server those files out of.

```bash
mkdir -p mediafiles
```

Then add to the bottom of `settings.py`.

```py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
```
