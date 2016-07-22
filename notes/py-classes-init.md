# Class Init

Since class instances store labeled, structured values, the most basic operation is setting up those values in a new instance.
Python gives us a streamlined way to require us to have every instance have some values set.

It's called a **constructor function**.
It's a function with the name `__init__`, pronounced **magic init** (also called "double-under init" or "dunder init" if you're googling around):

```py
class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
```

It should always take in a first argument named `self`, then any _other_ arguments you require as attributes on an instance.

Think about what fields are required to represent the _essence of an object_, not just any data that is cursorily related to the object.

Magic init is called with an _empty instance_ passed in as `self`, and all the other arguments from the type name call.
Magic init's job is to store all of those arguments inside this empty instance.
It does _not_ return a value;
it uses the passed-in instance to store the new data.

Before we had to write every time:

```py
me = AddressBookEntry()
me.name = 'David'
me.phone_number = '503-555-9895'
```

Now we magically use the magic init method to do that for us.

```py
me = AddressBookEntry('David', '503-555-9895')
you = AddressBookEntry('Helen', '503-555-1234')
print(me.name)  # David
print(you.name)  # Helen
```

When you define a magic init for a class, it changes how you must instantiate the class.
You now _need_ to pass all of those _other_ arguments when you call the type name:

```py
me = AddressBookEntry()  # throws TypeError
you = AddressBookEntry('Helen', '503-555-1234')
```

Magic functions are called "magic" because Python has them fill magical roles.
There's _no way_ for you to write code that makes an arbitrary function behave like they do.
