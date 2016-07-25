# Encapsulation

Remember how functions defined an interface?
One person can work on implementation, another person can work on use.
They agree on a contract, they don't need to worry directly about each other's work.

Classes have a similar concept called **encapsulation** for data.
All of the type methods of a class work together to separate _implementation_ from _use_.
Then the person that uses the type doesn't care about the data structures inside, just how the whole class behaves through its functions.

Do you know how `dict`s work?
Doesn't matter.
You know what `.update()` and `d[k]` does.

You don't care if I implement a `PhoneNumber` class using tokens or a string internally.

```py
class PhoneNumber:
    """Class which stores a normalized phone number.

    Instantiate with a string containing the phone number in the format
    XXX-XXX-XXXX.
    """

    def __init__(self, phone_str):
        self._tokens = phone_str.split('-')  #> ['503', '555', '1234']

    def get_area_code(self):
        """Return the area code of the phone number.

        >>> pn = PhoneNumber('503-555-1234')
        >>> pn.get_area_code()
        503
        """
        return self._tokens[0]
```

or

```py
class PhoneNumber:
    """Class which stores a normalized phone number.

    Instantiate with a string containing the phone number in the format
    XXX-XXX-XXXX.
    """

    def __init__(self, phone_str):
        self._phone_str = phone_str.replace('-', '')  #> '5055551234'

    def get_area_code(self):
        """Return the area code of the phone number.

        >>> pn = PhoneNumber('503-555-1234')
        >>> pn.get_area_code()
        503
        """
        return self._phone_str[:4]
```

## Private Attributes

There's one wrinkle to enforcing encapsulation, where the user doesn't know about the way the data is structured inside.
Python doesn't have **private attributes**.
Anyone can access any field and mess up your internal data.

```py
class ManualList:
    """A simple list that keeps track of its length."""

    def __init__(self):
        self.items = []
        self.item_count = 0

    def add(self, item):
        """Add a new item to the list.

        >>> l = ManualList()
        >>> l.add(5)
        >>> l.items
        [5]
        >>> l.item_count
        1
        """
        self.items.append(item)
        self.item_count += 1

    def length(self):
        """Return the length of the list.

        >>> l = ManualList()
        >>> l.add(5)
        >>> l.length()
        1
        """
        return self.item_count


l = ManualList()
l.add(5)
l.length()  #> 1
l.item_count = 99
l.length()  #> 99
# Wrong!
```

Attributes that you don't want modified by the user of the class, prefix them with an underscore `_`.

```py
class ManualList:
    """A simple list that keeps track of its length."""

    def __init__(self):
        self._items = []
        self._item_count = 0
```

This is just a _convention_ though, it doesn't programmatically stop anyone from modifying the attributes.

Feel free to check private attributes in your doctests or perhaps in same module functions.
But otherwise, if you see yourself using and underscore `_` attribute, be weary!
