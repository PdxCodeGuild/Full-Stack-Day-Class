# Regular Expressions
**Regular expressions** or **regexps** are a mini programming language to match text.

The programs themselves are also text, which live in another program that is also text.
This can be confusing.

When writing out regexps literals in Python, always use the `r` prefix, for "raw".
This causes it to ignore escape sequences for the _string literal_ itself so you don't have to double escape.
```py
r'Hello\.'  #> 'Hello\\.'
```

## Basic Match
Most characters match themselves.

```re
david s
```
will match
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
matches
> **fire** hydrant
> no fire here

```re
fire$
```
matches
> wood **fire**
> fire wood

```re
davi.
```
matches
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
matches
> **hodog**
> **hotdogs**

```re
sna+cks
```
matches
> **snacks**
> sncks
> **snaaaaaacks**

## Escapes
If you want literally any special characters use `\` in front of it.

```re
Hello\.
```
matches
> **Hello.**
> Hellox
