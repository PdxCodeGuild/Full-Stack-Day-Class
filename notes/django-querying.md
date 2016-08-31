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

To retrieve a single specific object, use `.get()`.
It accepts similar filters to `.filter()`.
In general, only use it to select on ID, since you're guaranteed to only have a single item.

```py
Business.objects.get(id=1)  #> Business(name='PDX Code Guild', founded=2012)
```

## Field Lookups

The Django ORM has a built-in slick language that allows you to construct complicated queries to select just the model objects you want.

There are [a lot of suffixes you can give to field names](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#field-lookups) that let you specify complex operators on existing fields.
All of the suffixes start with double underscore `__`.

```py
Business.objects.filter(name__contains='PDX')
Business.objects.filter(founded__gte=2000)
```

If you have multiple criteria that you want to all be satisfied (as an "and"), specify all of them.

```py
Business.objects.filter(name__contains='PDX', founded__gte=2000)
```

The double underscore also lets you "follow" relationships.

```py
Employee.objects.filter(works_at__name__contains='PDX')  #> [Employee(works_at=Business(name='PDX Code Guild', founded=2012), name='David Selassie', email='david@pdxcodeguild.com')]
```

You can also use `.exclude()` and pass all the same arguments to _not_ the filter.

To construct complicated logical queries, you can use a method chaining calling style to string together calls to `.filter()` and `.exclude()` to continually hone the result set.

```py
Employee.objects.filter(name__iexact='david')
  .exclude(name_icontains='selassie')
  .filter(works_at__name__contains='PDX')
```

To produce complicated "or" operations, use a [Q object](https://docs.djangoproject.com/en/1.10/topics/db/queries/#complex-lookups-with-q-objects).
