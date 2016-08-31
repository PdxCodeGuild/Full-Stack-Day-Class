# Admin Site

Django automatically builds for you an **admin interface** that lets you do basic model manipulation.
It lives at `/admin/` by default (note that route in `urls.py` that the setup script gives you).

For the admin site to work, there are some setup steps.

## 1. Setup Admin Database

The admin app uses the database to manage users, so we need to ensure that it's setup.
My [init script](/notes/django-init.md) does this for you.

```bash
python manage.py migrate
```

## 2. Create Admin User

Since the admin site is all powerful, it is behind a login.

Create an admin user with this script.
It will prompt you for user name, email address, and password.
You'll use this when logging in on just this Django project.

```bash
python manage.py createsuperuser
```

It seems to be picky that your password is secure.
Feel free to use the username:password `admin:brassmonkey` for your practice problems.

## 3. Register Models

You have to tell the admin app explicitly about each of the models it should generate UIs for.

In `DJANGO_APP_NAME/admin.py`, call `django.contrib.admin.site.register(model_class)` on all of your model classes.

```py
from django.contrib import admin

from . import models

admin.site.register(models.Business)
admin.site.register(models.Employee)
```
