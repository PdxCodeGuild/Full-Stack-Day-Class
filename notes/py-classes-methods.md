# Type Methods

Classes allow you to define **type methods** on them.
They are functions defined in the class body.
Their first argument is always `self`, which is an instance of that class.

```py
class PhoneNumber:
    """Class which stores a normalized phone number."""

    def __init__(self, phone_str):
        self.phone_str = normalize_phone(phone_str)

    def has_area_code(self):
        """Return if the stored number has an area code.

        >>> pn = PhoneNumber('5075559895')
        >>> pn.has_area_code()
        True
        >>> pn = PhoneNumber('5559895')
        >>> pn.has_area_code()
        False
        """
        return len(self.phone_str) > 7
```

Start by writing all of your functions _outside_ of classes.
Only move ones into the class itself that follow these guidelines:

*   Type methods _must_ take in an instance of the class.
    Only put in functions that are so strongly associated with the class that they would never work on another type.

*   For type methods, you need to _already have_ an instance of the class.
    This means functions that find an instance or make a new instance _should not_ be type methods.
