# Basic Classes and Objects
A **class** defines a template or **type** for a _structured value_ containing _inner values_ in your code.
For example:
* A "playing card" value has a suit and a card number
* An "address book entry" value has a name and a phone number
* An "image" value has a width and a height and some image data.
* A "user" with a name and email address.

Each of these could be represented as a class.
The inner variables all have names and are called **attributes** or **fields**.

Why not use a tuple or dict for structured values?
Named fields are easier to read and and you can enforce the structure is correct.

The types you make are like the types you've seen already: strings, ints, etc.

Similar to defining a function with `def`, you define a class via `class`, then a name, then a list of functions.
To start, we'll have no functions:
```python
class AddressBookEntry:
    pass  # A statement that does nothing.
```

## Instantiating
Similar to how defining functions doesn't run them, defining a class _doesn't_ make space for your structured value.
To actually _make space_ for your values, you have to **instantiate** the class, which looks like calling the type as a function.
The returned value is an **instance** or **object** of your type:
```python
me = AddressBookEntry()
```

Then you can actually set the attributes your structured value will have.
You can then reach into them and set and get inner attributes with the dot operator `.`.
Each instance has totally separate attributes:
```python
class AddressBookEntry:
    pass

me = AddressBookEntry()
you = AddressBookEntry()
me.name = 'David'
me.phone_number = '507-555-9895'
you.name = 'Helen'
you.phone_number = '507-555-1234'
print(me.name, me.phone_number)  # David 507-555-9895
print(you.name, you.phone_number)  # Helen 507-555-1234
```

Remember, the class just defines the structure, the template.
Each _instance_ is where the values are held.
You also have to store the instances in variables to remember what how they're supposed to be interpreted.

## Basic Naming
Class names have the same rules as variable names.

Proper Python style has classes in `CamelCase`:
words are capitalized and run together.

The built in types `int`, `dict`, `set`, etc. don't follow this rule.
You'll deal.
