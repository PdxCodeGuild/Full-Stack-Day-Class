# Basic String Methods

The Python string type gives you lots of built-in methods to manipulate strings.
Here are some of the major ones, in addition to [sequence operators](/notes/py-sequence-operators.md).

There are also tons more you can read about in the [string type docs](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Split

Split a string into a list of strings by a **delimiter**.

```py
'a b c'.split()  #> ['a', 'b', 'c']
'a  b    c'.split()  #> ['a', 'b', 'c']
'a\nb\tc'.split()  #> ['a', 'b', 'c']
'a,b c'.split(',')  #> ['a', 'b c']
'a-b--c'.split('--')  #> ['a-b', 'c']
```

## Join

Join a list of strings by another string.

```py
', '.join(['a', 'b'])  #> 'a, b'
'-'.join([503, 555, 1234])  #> Throws TypeError. Convert list items to strings first.
```

## Strip

Takes characters off the beginning and end of a string.
If an argument is given, it is the _set_ of characters to remove.

```py
'  hi '.strip()  #> 'hi'
'hi\n'.strip()  #> 'hi'
'  hi mom '.strip()  #> 'hi mom'
'==hi--'.strip('-=')  #> 'hi'
```

## Replace

You can replace a **substring**, or contiguous run of characters, with another string.
As a trick, if the other string is the empty string, you can delete all instances of the substring.

```py
'david'.replace('d', 's')  #> 'savis'
'xxxhix'.replace('xxx', '$')  #> '$hix'
'Mississippi'.replace('ss', '')  #> 'Miiippi'
```

## Case Conversion

Strings are case sensitive.
You can convert between cases.

```py
'Hello'.lower()  #> 'hello'
'Hello'.upper()  #> 'HELLO'
```

## Formatting

I'll [explain this on it's own](/notes/py-string-format.md).
