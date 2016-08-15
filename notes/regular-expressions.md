# Regular Expressions

**Regular expressions** or **regexps** are a mini programming language to match text.

The programs themselves are also text, which live in another program that is also text.
This can be confusing.

When writing out regexps literals in Python, always use the `r` prefix, for "raw".
This causes it to ignore escape sequences for the _string literal_ itself so you don't have to double escape.

```py
import re
reg_exp = re.compile(r'Hello, (\w+)', re.I)
match = reg_exp.search('Why hello, Alice.')
# The position in the search string of the match.
match.start()  #> 4
# Captures starting at 1. 0 is the whole string matched.
match.group(1)  #> 'Alice'
```

To write them out in JS, use a regexp literal, which is the pattern surrounded by forward slashes `/`.

```js
var regExp = /hello, (\w+)/i;
// This returns the strangest thing. It's an array, but it has properties "index" and "input".
var match = regExp.exec('Why hello, Alice.');
// The position in the search string of the match.
match.index;  //> 4
// Captures starting at 1. 0 is the whole string matched.
match[1];  //> 'Alice'
```

It's important to note that regular expressions are _not_ a standardized language.
Each implementing language does them slightly differently.
Regular expressions in JS are slightly different than those in Python.
I'll describe the totally portable syntax here.

Check out the [Python docs](https://docs.python.org/3/library/re.html) and [JS docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) to see advanced patterns and provided methods.

Use a [regexp debugging tool](https://regex101.com) to help you understand what you're matching.

## Character Match

Most characters match themselves.

```re
david s
```

> **david s**
>
> David s
>
> hello **david s**
>
> hello **david s** today

## Special Characters

There are some special characters that don't match themselves.

* Carrot `^` matches the beginning of a line
* Dollar sign `$` matches the end of a line
* Dot `.` matches any character

```re
^fire
```

> **fire** hydrant
>
> no fire here

```re
fire$
```

> wood **fire**
>
> fire wood

```re
davi. s
```

> **david s**
>
> **davix s**
>
> davidd s

## Repeats

There are some special characters that mark how many times the previous character should repeat.

* `?` means one or zero times
* `*` means zero or more times
* `+` means at least one time

```re
hot?dogs?
```

> **hodog**
>
> **hotdogs**
>
> **hotdog**

```re
sna+cks
```

> **snacks**
>
> sncks
>
> **snaaaaaacks**

```re
sna*cks
```

> **snacks**
>
> **sncks**
>
> **snaaaaaacks**

## Escapes

If you want literally any special characters use backslash `\` escape in front of it.

```re
Hello\.
```

> **Hello.**
>
> Hellox

## Character Classes

Groups of characters that are used in the same sorts of ways are called **classes**.

* `\d` matches digits
* `\s` matches white space of all kinds
* `\w` matches "word" characters (letters _and_ numbers)

Each group still only matches one character, but repeat characters can be used on them.

```re
\d+\s\w+
```

> **12 a5**
>
> 1f ap
>
> **12\ta**

## Character Sets

If you want to be more discerning than a whole character class, you can use a **set**.
Put all the characters you want to allow in square brackets `[]`.
Each set still only matches one character, but repeat characters can be used on them.

```re
[bp]anana
```

> **banana**
>
> **panana**
>
> pbanana

```re
snack[sx]*
```

> **snacksxsssx**

You can specify **ranges** of characters with dash `-`, so dash must be escaped in a character set.
A super common range is all letters `[a-zA-Z]` since `\w` also includes digits.

```re
My Name Is: [a-zA-Z]+
```

> **My Name Is: David**
>
> My Name Is: C4t

## Captures

You can group together parts of a match into a **capture**, which is like a "sub-match", using parentheses `()`.
You can then use the repeat modifiers on the whole capture.

More useful than that, is when the regular expression library matches text, it will save which parts of the text match each capture by the order they appear (1, 2, etc.).
This is always one-indexed.

```re
(hot+)+dogs
```

> **hotdogs**
>
> **hothotthotttdogs**

```re
(\d\d\d)-(\d\d\d)-(\d\d\d\d)
```

> **123-456-7890**

### Named Captures

Instead of just remembering the text that matched each capture by the order it appears in the whole regular expression, you can also use a **named capture**.
It is still a sub-match specified in parentheses `()`, but with `?P<NAME>` first inside.

```re
(?P<first_name>.+) (?P<last_name>.+)
```

> **bob dole**
