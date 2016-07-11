# Optional and Keyword Arguments

Thus far, we've been passing arguments functions **by position**.
When you call a function, there is a set number of arguments you have to give every time, and the order of them determines how the function interprets them.

`pow` takes two arguments and the first is the base and the second is the exponent.

```py
pow(3, 2)  #> 9
pow(2, 3)  #> 8
```

Some functions take **optional positional arguments**.
They are for arguments that have a **default value**, but the caller might want to override on occasion.

```py
'Title'.center(9)  #> '  Title  '
'Title'.center(9, '=')  #> '==Title=='
```

Some functions take **optional keyword arguments**.
You label each input value with the named slot you want it to go in, then an equals with no spaces, then the value you want in the slot.

```py
print('Hello', end='')
```

This is a way of passing in some optional arguments without needing to specify all of them!
That would be necessary if position was the only way to pass in values.
