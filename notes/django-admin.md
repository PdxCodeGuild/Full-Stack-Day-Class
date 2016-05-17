# Admin Site

## 1. Create Admin User

In your virtualenv.

```bash
python manage.py createsuperuser
```

## 2. Register Models

In `DJANGO_APP_NAME/admin.py`, call `django.contrib.admin.site.register(model_class)` on all of your model classes.

```py
from django.contrib import admin

from . import models

admin.site.register(models.Business)
admin.site.register(models.Employee)
```
