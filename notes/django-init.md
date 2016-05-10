# Django Init
Django applications have to follow a very specific source and module structure.
```
PROJECT_NAME/
    manage.py
    DJANGO_APP_NAME/
        __init__.py
        settings.py
        static/
            DJANGO_APP_NAME/
                ...
        templates/
            DJANGO_APP_NAME/
                ...
        urls.py
        views.py
        wsgi.py
        YOUR_LOGIC_CODE.py
        YOUR_MODULE/
            ...
        ...
```

I will call the `DJANGO_APP_NAME` directory the **Django application root**.
For our basic projects, `DJANGO_APP_NAME` should be the same as `PROJECT_NAME`.

Use the following steps to setup your Django app.
These should live alongside the [standard Python application files](py-app-structure.md).
You should commit all of these files.

## 1. Create Django App
The Django package gives you a script to setup this structure.
Run this command from inside your _project root_.
```bash
django-admin startproject DJANGO_APP_NAME .
```
Note the separate period at the end.

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

## 2. Create Views
Create an empty `views.py` in the Django application root for your [views](django-views.md).
```bash
touch DJANGO_APP_NAME/views.py
```

## 3. Create Templates Directory
Create an empty [templates](django-templates.md) directory for your HTML.
Yes, it's redundant, but under `templates` in your Django application root, you should make another directory named your app name.
```bash
mkdir -p DJANGO_APP_NAME/templates/DJANGO_APP_NAME
```

## 4. Create Static Files Directory
Create an empty [static files](django-static-files.md) directory for images, CSS, and JS.
Yes, it's redundant, but under `static` in your Django application root, you should make another directory named your app name.
```bash
mkdir -p DJANGO_APP_NAME/static/DJANGO_APP_NAME
```
