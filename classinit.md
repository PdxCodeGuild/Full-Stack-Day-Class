# Class Init
Since classes store structured values, the most basic operation is setting up those values.

Before we had:
```python
class AddressBookEntry:
  def setup(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number
```

Python gives us a streamlined way to write a function that sets up initial values.
It's called a **constructor** and has the name `__init__`, pronounced **magic init** (also called "double-under init" or "dunder init"):
```python
class AddressBookEntry:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number
```

Magic init is given all the arguments passed when calling the type and should setup the scope using them.
```python
me = AddressBookEntry('David', '507-555-9895')
```

Note that magic init _does not_ return the object.
It is given an object that is already made and it's job is just to do setup.

Magic functions are called "magic" because Python has them fill magical roles.
There's _no way_ for you to write code that makes an arbitrary function behave like they do.
