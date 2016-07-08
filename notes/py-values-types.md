# Values and Types

Programming is transforming data, so we need some way of representing data.
A **value** is an abstract individual piece of data or fact or idea.
It has no meaning on it's own.
Values are the _concrete nouns_ of programming.

**Literals** are when you _literally write_ some values in your source code:

```py
5
-100
'fox'
'David'
3.14
0.05
```

Every value is of a single **type**.
A type is a _kind_ of value or a way to _interpret_ them.

Three basic types are:

* **Integers** are whole numbers.
* **Strings** are ordered sequences of characters in single quotes `''`.
* Floating point numbers or **floats** are decimal numbers.

You can sometimes represent similar ideas in multiple types:

```py
42
42.0
'42'
```

These are all distinct values with distinct types and thus distinct interpretations.

Sometimes the interpretation of the type allows useful, but unexpected values.
A string can have _no_ characters in it, called the **empty string**:

```py
''
```

A string literal that contains an apostrophe will break unless you escape the apostrophe with a backslash `\`.

```py
'can\'t'
```
