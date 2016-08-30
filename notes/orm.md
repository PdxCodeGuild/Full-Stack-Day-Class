# Object Relational Mapper

An **object relational mapper** gives a DB a slick Python interface.

You can write Python classes that represent the **models** you care about on your site.
They are the nouns.

```py
from django.db import models


class User(models.Model):
    user_name = models.CharField()
    email = models.CharField()
    sign_up_date = models.DateTimeField()
```

An ORM will be able to automatically create database tables that can hold the information in instances of your model.
Database tables looks like spreadsheets.
For the above example:

```
user_name, email, sign_up_date
"David", "david@david.com", "2016-01-01"
"Helen", "helen@helen.com", "2015-05-01"
...
```

An ORM will then wrap selecting and modifying instances in the database in nice Python functions:

```py
david = User.objects.filter(email='david@david.com')
david.user_name = 'DavidS'
david.save()
```

This prevents you from needing to learn **SQL** or **structured query language**.
That is the low-level, text based interface to databases and can be tedious to use because it requires converting to and from language-native data types.
