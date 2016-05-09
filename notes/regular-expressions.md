# Regular Expressions
**Regular expressions** or **regexps** are a mini programming language to match text.

The programs themselves are also text, which live in another program that is also text.
This can be confusing.

When writing out regexps literals in Python, always use the `r` prefix, for "raw".
This causes it to ignore escape sequences for the _string literal_ itself so you don't have to double escape.
```py
r'Hello\.'  #> 'Hello\\.'
```

It's important to note that regular expressions are _not_ a standardized language.
Each implementing language does them slightly differently.
Regular expressions in JS are slightly different than those in Python.
I'll describe the totally portable syntax here.

There is also [more advanced syntax](https://docs.python.org/3/library/re.html).

Use a [regexp debugging tool](https://regex101.com) to help you understand what you're matching.

## Character Match
Most characters match themselves.

```re
david s
```

> **david s**

> David s

> hello **david s**

> hello **david s** today

## Special Characters
There are some special characters that don't match themselves.
* `^` matches the beginning of a line
* `$` matches the end of a line
* `.` matches any character

```re
^fire
```

> **fire** hydrant

> no fire here

```re
fire$
```

> wood **fire**

> fire wood

```re
davi.
```

> **david**

> **davix**

## Repeats
There are some special characters that mark how many times the previous character should repeat.
* `?` means one or zero times
* `*` means zero or more times
* `+` means at least one time

```re
hot?dogs?
```

> **hodog**

> **hotdogs**

```re
sna+cks
```

> **snacks**

> sncks

> **snaaaaaacks**

## Escapes
If you want literally any special characters use `\` in front of it.

```re
Hello\.
```

> **Hello.**

> Hellox

## Captures
You can group together parts of a match into a **capture**, which is like a "sub-match", using parentheses `()`.
You can then use the repeat modifiers on the whole capture.
When the regular expression library matches text, it will save which parts of the text match each capture by the order they appear (1, 2, etc.).

```re
(hot+)+dogs
(...)-(...)-(....)
```

> **hotdogs**

> **hothothotdogs**

### Named Captures
Instead of just remembering the text that matched each capture by the order it appears in the whole regular expression, you can also use a **named capture**.
It is still a sub-match specified in parentheses `()`, but with `?P<NAME>` first inside.

```re
(?P<first_name>.+) (?P<last_name>.+)
```

> **bob dole**

## Classes
Groups of characters that are used in the same sorts of ways are called **classes**.
* `\d` matches digits
* `\s` matches spaces of all kinds
* `\w` matches word characters

```re
\d+\w\d+
```

> **1\t2**

> **111 2**
