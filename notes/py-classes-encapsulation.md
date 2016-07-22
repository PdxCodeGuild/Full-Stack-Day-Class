# Encapsulation

Remember how functions defined an interface?
One person can work on implementation. One person can work on use.
They agree on a contract, they don't need to worry directly about each other's work.

Classes have a stronger sense of an interface called **encapsulation**.
All of the type methods of a class work together to separate implementation from use.
Then the person that uses the type doesn't care about the data structures inside, just how the functions behave.

Do you know how `dict`s work?
Doesn't matter.
You know what `.update()` and `d[k]` does.

```py
class PhoneNumber:
    def __init__(self, phone_str):
        ...

    def get_area_code(self):
        ...

    def send_text(self, message):
        ...
```

You don't care if I implement that class as

```py
class PhoneNumber:
    def __init__(self, phone_str):
        self._tokens = phone_str.split('-')

    def get_area_code(self):
        self._tokens[0]
```

or

```py
class PhoneNumber:
    def __init__(self, phone_str):
        self._phone_str = phone_str

    def get_area_code(self):
        self._phone_str[:4]
```

In fact, sometimes many separate types all have the same type functions.
That's why the short form of class method calling is cool!
You don't have to know the exact class that the instance has!

The type methods fulfill a **type interface** by all having the same type method names and saying they can be used in the same way.

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
        >>> l.length()
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

Feel free to check private attributes in your doctests.
There should be implementation tests.
