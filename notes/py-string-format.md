# String Formatting

When making complex strings, using the plus `+` operator can get clunky.
Instead use **string formatting**.
You supply a **template** string and then the other strings you want interpolated into the template.
Any double braces `{}` will be filled in with the arguments to format _in order_.

```py
'Hello, {}! my name is {}.'.format('David', 'Helen')  #> 'Hello, David! my name is Helen.'
```

You can also modify the way that objects are filled in the template spots using a [special mini-language](https://docs.python.org/3/library/string.html#formatstrings).

```py
price = 10 / 3
'That cost: ${:.2f}'.format(price)  #> 'That cost: $3.33'
```
