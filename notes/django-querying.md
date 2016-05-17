# Querying

Once a model instance can be saved, you can get them back!
There are a set of functions on the _model classes themselves_ which allow you to query for existing instances.

To retrieve all previously saved items, use `.all()`.

```py
Business.objects.all()  #> [Business(name='PDX Code Guild', founded=2012), Business(name='Voodoo Donut'), founded=2002)]
```

To search and filter for just some items use `.filter()`.
Give it a keyword argument of the field name to filter to it.

```py
Business.objects.filter(name='PDX Code Guild')  #> [Business(name='PDX Code Guild', founded=2012)]
```

There are [a lot of suffixes you can give to field names](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#field-lookups) that let you specify complex operators on existing fields.
All of the suffixes start with double underscore `__`.

```py
Business.objects.filter(name__contains='PDX')
Business.objects.filter(founded__gte=2000)
```

The double underscore also lets you "follow" relationships.

```py
Employee.objects.filter(works_at__name__contains='PDX')  #> [Employee(works_at=Business(name='PDX Code Guild', founded=2012), name='David Selassie', email='david@pdxcodeguild.com')]
```

You can also use `.exclude()` and pass all the same arguments to _not_ the filter.
