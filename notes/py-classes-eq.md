# Class Equality

All the Python built-in types have a sense of **equality**:
if the contents are the same, they are equal.

```py
5 == 3  #> False
[1, 2, 3] == [1, 2, 3]  #> True
{'cat': 4, 'snake': 0} == {'cat': 4, 'snake': 0}  #> True
```

But the classes you make, _aren't_ by default.
Python doesn't assume you have the same definition of equals.

You should make them work that way _if it makes sense_, though.
It's much easier to think about.

Write a **magic eq** function in your class to define equality.
It must have the signature `__eq__(self, other)` and _return_ a bool.

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
```

Python will magically call this function for you whenever the first argument to `==` is that type.

```py
me = AddressBookEntry('David', '503-555-9895')
you = AddressBookEntry('Helen', '503-555-2131')

# These two lines run the same code:
me == you  #> False
AddressBookEntry.__eq__(me, you)  #> False
```

Because of this, note:

```py
me == 5  # throws AttributeError
```

I think that's okay.
You should _avoid_ comparing different types.
An error will remind you.

## Not All Classes Have Equality

Not every class makes sense to compare all fields to decide if it's "equal" to another instances.
Some types don't make sense like that.

E.g. an `Account` class that _doesn't_ have a unique ID in it.
If two accounts have the same amount inside, are they "equal"?
