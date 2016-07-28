# Note Conventions

## Placeholders

Things in `CONSTANT_CASE` that are not part of Python code (e.g. shell commands or any other text), it's meant as a **placeholder** for a real name, usually written in `snake_case`.

```
pip install PACKAGE
```

## Optional

Any time a part of a string of text contains square brackets `[]`, that part of the text is optional.

```
http://host[:port]/
```

Except for inside of Python code!
Square brackets mean something then.

```py
name_to_age['david']  # Not optional! Does something.
```

## Values

In Python code, when I put a comment chevron `#>` it means the previous line's value is equal to the literal after the comment chevron.

```py
5 + 6  #> 11
x = pow(3, 4)  #> 81
```
