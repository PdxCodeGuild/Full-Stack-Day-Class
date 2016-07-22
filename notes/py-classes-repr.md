# Class String Representation

Python doesn't assume to know how to convert an instance of your class to a string.

```py
class AddressBookEntry:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

me = AddressBookEntry('David', '503-555-9895')
print(me)  # <__main__.AddressBookEntry object at 0x1043772e8>
```

Write a **magic repr** function in your class to define how to _represent_ your object as a string.
It must have the signature `__repr__(self)` and _return_ a string.
It _should not print_.

```py
class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return 'AddressBookEntry({!r}, {!r})'.format(
            self.name,
            self.phone_number
        )

me = AddressBookEntry('David', '503-555-9895')
print(me)  # AddressBookEntry('David', '503-555-9895')
```

You should _always_ write a magic repr method.
This will enable you to debug using print.

What should you string representation look like?
It should be an unambiguous _literal_ representation of all the data in an instance of your class.
I recommend it look like a call to your class' constructor.

> AddressBookEntry('David', '503-555-9895')
>
> AddressBookEntry(name='David', phone_number='503-555-9895')

You should remember that any attributes you're interpolating into the string representation should be reprs themselves!
Use `{!r}` instead of just `{}` in your formatting string.
