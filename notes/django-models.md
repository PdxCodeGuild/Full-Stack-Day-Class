# Models
Django **models** are the structured nouns in your project.
They are implemented as [classes](basicobjectsclasses.md), so think back about how you used classes to [model your data](classdesign.md).

Each model is implemented as a list of **fields** with explicit types.

To make a model, create a new class, then reference `django.db.models.Model`.
Then, instead of using a constructor or magic init to describe all of the fields, you create class variables with the field types.
```py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## Field Types
There are [many more field types you can read about in the Django docs](https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types).
