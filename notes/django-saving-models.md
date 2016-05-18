# Instantiating and Saving Models

To create a new model instance, call the class name, just like a normal Python class.
All of the fields become _keyword_ constructor arguments.

```py
code_guild = Business(name='PDX Code Guild', founded=1876)
voodoo = Business(name='Voodoo Donut', founded=2002)

david = Employee(
    works_at=code_guild,
    name='David Selassie',
    email='david@pdxcodeguild.com',
)
```

You can get or set field values by using normal Python class attribute access.

```py
code_guild.name  #> 'PDX Code Guild'
code_guild.founded = 2012
code_guild.id  # Some random, unique int.
```

Any time you create a new instance or change any of the fields, and are done operating on it, you need to **save** the instance.
This is like saving the data in a global variable, but instead puts it in the DB.
We can [query](/notes/django-querying.md) the DB to retrieve it later on another request.

Call `.save()` on the instance.

```py
code_guild.save()
voodoo.save()

david.save()
```

Only call save when all of the logical changes you want to make to that instance are done.
_Don't_ call save after each individual change.

To delete an instance, call `.delete()`.
You do not have to call `.save()` after deleting.

```py
david.delete()
```
