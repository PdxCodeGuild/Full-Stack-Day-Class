# Models

Django **models** are the structured nouns in your project.
They are implemented as [classes](/notes/py-classes-basic.md), so think back about how you used classes to [model your data](/notes/py-classes-design.md).

Each model is implemented as a list of **fields** with explicit types.
Unlike normal Python class attributes, those fields are **typed**.
This means that there are restrictions on what kinds of values can go in them.

To make a model, create a new class in `DJANGO_APP_NAME/models.py`, then reference `django.db.models.Model`.
Then, instead of using a constructor or magic init to describe all of the fields, you create class variables with the field types.

Implement both magic string and magic repr on all of your model classes.
Django uses magic string to show a short description of your class instances on the admin site, and you still need to implement magic repr so you can print debug.

```py
from django.db import models


class Business(models.Model):
    name = models.TextField()
    founded = models.DateField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Business(name={!r}, founded={!r})'.format(self.name, self.founded)


class Employee(models.Model):
    works_at = models.ForeignKey(Business)
    name = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Employee(works_at={!r}, name={!r}, age={!r}, email={!r})'.format(
            self.works_at,
            self.name,
            self.age,
            self.email,
        )
```

Every model is automatically given a unique ID field called `id`.
You don't need to explicitly add that.

## Field Types

* `TextField()`
* `IntegerField()`
* `FloatField()`
* `DateField()`
* `DateTimeField()`
* `BooleanField()`

Try to use the most specific type possible.
There are some that do double checking of validity.

* `EmailField()`

There are [many more field types you can read about in the Django docs](https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types).

## Migrating

Whenever you change fields on or create new models, you have to **migrate** the existing DB.
A migration is a set of instructions for how to use and save instances of your models.
Django will make them for you!

Basically, whenever you change `DJANGO_APP_NAME/models.py` run these two commands in your virtualenv.
You need to specify your Django app name when you make migrations.

```bash
python manage.py makemigrations DJANGO_APP_NAME
python manage.py migrate
```

This creates a history of how all of your models have changed in the `DJANGO_APP_NAME/migrations` directory.
Commit this whenever it changes.

Do _not_ commit the `db.sqlite3` file that is created.
That contains the actual DB data and is not part of your project code.
