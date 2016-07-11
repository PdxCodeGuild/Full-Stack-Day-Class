# Calling Type Methods

Python gives you lots of functions that only work on specific types.
They are so specific to the type, they live _inside_ the type and are called **type methods**.
They _always_ take a first argument of that type.

You use the **dot operator** to reach inside of the type name, and pick out a function, then call it.

```py
str.upper('hello')  #> 'HELLO'
float.is_integer(3.0)  #> True
```

You'll be using type methods so often that there's a **short form** for writing them.
Take the first argument, and put it _before the dot_.

```py
'hello'.upper()  #> 'HELLO'
# If it's a number, you have to use parens to not mess with the dot in floats.
(3.0).is_integer()  #> False
```

Although the **long form** is actually what is happening, and thus I want to show you it, it's proper style to _always use the short form_.
