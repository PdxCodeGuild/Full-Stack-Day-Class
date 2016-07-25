# Type Methods

Classes allow you to define **type methods** on them.
They are functions defined in the class body.
Their first argument is always `self`, which will be an instance of that class.

```py
class PhoneNumber:
    """Class which stores a normalized phone number.

    Instantiate with a string containing the phone number in the format
    XXX-XXX-XXXX or XXX-XXXX.
    """

    def __init__(self, phone_str):
        self.phone_str = phone_str.replace('-', '')

    def has_area_code(self):
        """Return if the stored number has an area code.

        >>> pn = PhoneNumber('503-555-9895')
        >>> pn.has_area_code()
        True
        >>> pn = PhoneNumber('555-9895')
        >>> pn.has_area_code()
        False
        """
        return len(self.phone_str) > 7
```

Remember, the short form of calling type methods places the class instance before the dot operator `.` as the first argument `self`.

```py
my_phone = PhoneNumber('503-555-9895')
my_phone.has_area_code()  #> True
# Same call as, which matches the function signature:
PhoneNumber.has_area_code(my_phone)
```

Both magic methods and normal type methods are defined and behave in the same way regarding `self`.

## Type Method vs Top-Level Method

You _could_ write type methods as top-level functions in the same module.

```py
def has_area_code(phone_number):
    """Return if the stored number has an area code.
    ...
    """
    return len(phone_number.phone_str) > 7
```

And that's fine!
Here are my guidelines for when you should move them into a class.

Start by writing all of your functions _outside_ of classes.
Only move ones into the class itself that follow these guidelines:

*   Type methods _must_ take in an instance of the class.
    Only put in functions that are so strongly associated with the class that they would never work on another type.

*   For type methods, you need to _already have_ an instance of the class.
    This means functions that find an instance or make a new instance _should not_ be type methods.

I do suggest your place functions related to a class but that can't be type methods as top-level functions in the same module.

```py
class PhoneNumber:
    """Class which stores a normalized phone number."""
    ...


# Can't live in the class because doesn't take a pre-existing PhoneNumber instance as an input.
def lookup_phone(name):
    """Return a phone number for someone's name."""
    ...
```
