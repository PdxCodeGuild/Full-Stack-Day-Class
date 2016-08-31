# Model Relations

To link together separate entities in a relation, in general you add a field to the _many-ed_ model.
Always pass in a `related_name` kwarg to give the reverse relation a name; it will add a "field" with that name on the other end.

Django then will give you back specific model instances for the _one-d_ link.
For the _many-ed_ link, you get back something that acts like a `QuerySet` and you can request `.all()` of the models.
Examples below.

Before you link together any entities, you need to save them.
This is so Django knows about their unique IDs.
It uses IDs internally to do the relations, but they are never exposed to you.

## One-to-One

On the _child_ entity model, add a `OneToOneField(parent_model_class, related_name=field_name_on_other_model, on_delete=models.CASCADE)`.
That second argument ensures that when you delete either the child or the parent, both are deleted.

```py
from django.db import models


class Person(models.Model):
    name = models.TextField()

    def __repr__(self):
        return 'Student(name={!r})'.format(self.name)


class Resume(models.Model):
    person = models.OneToOneField(Person, related_name='resume', on_delete=models.CASCADE)
    years_employed = models.IntegerField()

    def __repr__(self):
        return 'Resume(years_employed={!r})'.format(self.years_employed)


david = Person(name='David')
david.save()
resume = Resume(person=david, years_employed=15)
resume.save()
david.resume  #> Resume(years_employed=15)
resume.person  #> Person(name='David')
```

## One-to-Many

On the _child_ entity model, add a `ForeignKey(parent_model_class, related_name=field_name_on_other_model)`.

```py
from django.db import models


class Student(models.Model):
    name = models.TextField()
    course = models.ForeignKey(Course, related_name='students')

    def __repr__(self):
        return 'Student(name={!r})'.format(self.name)


class Course(models.Model):
    name = models.TextField()

    def __repr__(self):
        return 'Course(name={!r})'.format(self.name)


day_class = Course(name='Day Class')
day_class.save()
david = Student(name='David', course=day_class)
david.save()
helen = Student(name='Helen', course=day_class)
helen.save()
david.course  #> Course(name='Day Class')
helen.course  #> Course(name='Day Class')
day_class.students.all()  #> [Student(name='David'), Student(name='Helen')]
```

## Many-to-Many

On the _child_ entity model, add a `ManyToManyField(other_model_class, related_name=field_name_on_other_model)`.

You add links to the relationship by using `.add(other_model_instance)` on the field name.
You _must_ save the model that you're linking to before adding it, otherwise you get an obtuse error about IDs.

```py
from django.db import models


class Author(models.Model):
    name = models.TextField()

    def __repr__(self):
        return 'Author(name={!r})'.format(self.name)


class Book(models.Model):
    title = models.TextField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __repr__(self):
        return 'Book(title={!r})'.format(self.title)


herman = Author(name='Herman Melville')
herman.save()
ghost = Author(name='Ghost Writer')
ghost.save()
moby = Book(title='Moby Dick')
moby.authors.add(herman)
moby.authors.add(ghost)
moby.save()
secret = Book(title='Secret Book')
secret.authors.add(ghost)
secret.save()

herman.books.all()  #> [Book(title='Moby Dick')]
ghost.books.all()  #> [Book(title='Moby Dick'), Book(title='Secret Book')]
moby.authors.all()  #> [Author(name='Herman Melville'), Author(name='Ghost Writer')]
secret.authors.all()  #> [Author(name='Ghost Writer')]
```
