# Basic Classes
A class in Python is a group of functions that _share a scope_ or variables.
When you define a class, you define all the functions that know how to work with that shared scope.
Defining a class creates a **type**.

Since the shared scope is the essence of a class, scopes store variables, and variables store data:
classes represent _nouns_ / data.

You should create new classes when you want to represent a _structured value_ in your code.
For example:
* A "playing card" value has a suit and a card number
* An "address book entry" value has a name and a phone number
* An "image" value has a width and a height and some image data.
* A "user" with a name and email address.

Why not use a tuple for structured values?
We learned tuples are used to bind together values of different interpretation.
True, but classes allow you to _name_ the fields.
For the same reason you should use well-named variables.

The types you make are just like the types you've seen already: strings, ints, etc.

## Defining
Similar to defining a function with `def`, you define a class via `class`, then a name, then a block of function definitions.
Each function in a class takes in the shared scope _as the first argument_.
It is always called `self`.
You access variables inside the scope using the `.` operator.
All other variables you access normally.

```python
class AddressBookEntry:
  def setup(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

  def area_code(self):
    return self.phone_number.split('-')[0]
```

## Basic Naming
Class names have the same rules as variable names.

Proper Python style has classes in `CamelCase`:
words are capitalized and run together.

Yeah, the built in types `int`, `dict`, `set`, etc. don't follow this rule.
You'll deal.

## Instantiating
Similar to how defining functions doesn't run them, defining a class only describes _how_ to use the shared scope, it doesn't make one.
**Instantiating** the type actually makes the scope as a value.
This value is referred to as an **object**.
Instantiating looks like _calling_ the type as a function.

```python
me = AddressBookEntry()
```

## Type Methods
All of the functions we defined in the class are **type methods**.
They're just like `str.lower`.
Remember the "long form"?
```python
str.lower('Hi')  #> 'hi'
```

We can do the same thing!
It looks exactly like the function signature we wrote.
```python
me = AddressBookEntry()
AddressBookEntry.setup(me, 'David', '503-555-9895')
AddressBookEntry.area_code(me)  #> '503'
```

You've been using the "short form" of type methods, though:
```python
'Hi'.lower()  #> 'hi'
```
We can do that too!
```python
me = AddressBookEntry()
me.setup('David', '503-555-9895')
me.area_code()  #> '503'
```

As before, the short form is just taking the first argument and moving it before the dot.
Remember, the _function signatures look like the long form_, but everyone calls type methods using the short form.

## Scope Variables
You can also access all of the variables in the scope of an instance using the dot operator on the instance.
```python
me = User()
me.setup('David', '503-555-9895')
me.name  #> 'David'
```
