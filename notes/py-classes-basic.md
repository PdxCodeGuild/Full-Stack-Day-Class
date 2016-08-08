# Basic Classes and Objects

A **class** defines a template or **type** for a _complex structured value_ that is a collection of labeled _inner values_ in your code.
For example:

* A "playing card" value has a suit and a card number
* An "address book entry" value has a name and a phone number
* An "image" value has a width and a height and some image data.
* A "user" with a name and email address.

Each of these could be represented as a class.
The inner variables are labeled with names and are called **attributes** or **fields**.

Why not use a tuple or dict for structured values?
Named attributes are easier to read and and you can enforce the structure is correct.

The types you make are like the types you've seen already: strings, ints, etc.

Similar to defining a function with `def`, you define a class via `class`, then a name, then a list of functions.
To start, we'll have no functions:

```py
class AddressBookEntry:
    pass  # A statement that does nothing.
```

## Instantiating

Similar to how defining functions doesn't run them, defining a class _doesn't_ make space for your structured value.
To actually _make space_ for your value, you have to **instantiate** the class, which looks like calling the type as a function.
The returned value is an **instance** or **object** of your type:

```python
me = AddressBookEntry()
```

Then you can actually fill the instance with data for each attribute name.
You can then reach into them and set and get inner attributes with the dot operator `.`.
Each instance has totally separate attributes:

```py
class AddressBookEntry:
    pass

me = AddressBookEntry()
you = AddressBookEntry()
me.name = 'David'
me.phone_number = '503-555-9895'
you.name = 'Helen'
you.phone_number = '503-555-1234'
print(me.name, me.phone_number)  # David 503-555-9895
print(you.name, you.phone_number)  # Helen 503-555-1234
```

Remember, the class just defines the structure, the template, what labels are valid.
Each _instance_ is where the values are held.
You also have to store the instances in variables to remember what how they're supposed to be interpreted.

## Basic Naming

Class names have the same rules as variable names.

Proper Python style has classes in `WordCase`:
words are capitalized and run together.

The built in types `int`, `dict`, `set`, etc. don't follow this rule.
You'll deal.
