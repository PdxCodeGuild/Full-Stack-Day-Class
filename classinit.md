# Class Init
Since classes store structured values, the most basic operation is setting up those values.
Python gives us a streamlined way to write a function that sets up initial values into an instance.

It's called a **constructor function**.
It's a function with the name `__init__`, pronounced **magic init** (also called "double-under init" or "dunder init"):
```python
class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
```

It should always take in a first argument named `self`, then any _other_ arguments you want to store as attributes in an instance.

When you define a magic init for a class, it changes how you instantiate the class.
You now _need_ to pass all of those _other_ arguments when you call the type name:
```python
me = AddressBookEntry()  # throws TypeError
me = AddressBookEntry('David', '507-555-9895')
you = AddressBookEntry('Helen', '507-555-1234')
```

Magic init is called with an _empty instance_ passed in as `self`, and all the other arguments from the type name call.
Magic init's job is to store all of those arguments inside this empty instance.

So before we had:
```python
me = AddressBookEntry()
me.name = 'David'
me.phone_number = '507-555-9895'
```

Now we magically use the magic init method to do that for us.
```python
me = AddressBookEntry('David', '507-555-9895')
you = AddressBookEntry('Helen', '507-555-1234')
print(me.name)  # David
print(you.name)  # Helen
```

Magic functions are called "magic" because Python has them fill magical roles.
There's _no way_ for you to write code that makes an arbitrary function behave like they do.
