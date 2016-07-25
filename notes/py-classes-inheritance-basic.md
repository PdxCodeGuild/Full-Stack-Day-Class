# Basic Inheritance

Python classes have the concept of **inheritance**.
This means that the type methods of a class can be pre-filled from a different **base class**.

We are not going to really write code that uses inheritance in this course, but I want you to be aware of the concept since you will see it in some code we encounter, but not need to modify it.

To have a new class inherit from an old one, put the old class name in parentheses `()` after the new class name.

```py
class OldDog:
    def __init__(self, name):
        self._name = name

    def say_hi(self):
        return 'Hello. My name is {}.'.format(self._name)

    def shake(self):
        return 'Shakes!'


class NewDog(OldDog):
    def shake(self):
        return 'No. I will not.'


davids_dog = OldDog('Fido')
helens_dog = NewDog('Milo')
davids_dog.say_hi()  #> 'Hello. My name is Fido.'
davids_dog.shake()  #> 'Shakes!'
helens_dog.say_hi()  #> 'Hello. My name is Milo.'
helens_dog.shake()  #> 'No. I will not.'
```

You'll see this as a way to:

* Keep existing type method functionality, but **override** and change some of it.
* Mark a class as belonging to a category of types.
* Imbue a class with super magical behavior, where normal Python statements do cool things (see [metaclasses](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)).
