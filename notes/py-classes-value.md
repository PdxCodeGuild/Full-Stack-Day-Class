# Value Classes

Classes that implement _equality_ and are treated as _immutable_ are **value types**.
I suggest you make most of your classes behave in this way, and we'll practice this.

How do you make something explicitly immutable?
Don't write functions that modify internal variables.
It also makes them easier to test!

Unfortunately, Python is a super "public" language, so it's hard and verbose to enforce immutability.
But you can write functions that don't do that.

Avoid assigning to inner properties.

```py
class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __eq__(self, other_entry):
      return (
        self.name == other_entry.name and
        self.phone_number == other_entry.phone_number
      )

    def __repr__(self):
        return 'AddressBookEntry({!r}, {!r})'.format(
            self.name,
            self.phone_number
        )


AddressBookEntry = namedtuple('AddressBookEntry', ['name', 'phone_number'])


def update_phone_number(entry, new_phone):
    """Modify in-place an address book entry with a new phone number.

    >>> ci = AddressBookEntry('David', '1234')
    >>> update_phone_number(ci, '5678')
    >>> ci
    AddressBookEntry('David', '5678')
    """
    entry.phone = new_phone
```

Instead, return an updated copy.

```py
def update_phone_number(entry, new_phone):
    """Return an updated address book entry with a new phone number.

    >>> update_phone_number(AddressBookEntry('David', '1234'), '5678')
    AddressBookEntry('David', '5678')
    """
    return AddressBookEntry(entry.name, new_phone)
```
