# Basic Casting

Python gives you built-in functions to change the type of a value, keeping the meaning _as close as possible_.
These functions are called **casting functions**.

The functions are named after the type you _want_.

```py
str(5)  #> '5'
int('5')  #> 5
float('5')  #> 5.0
```

If the _meaning_ of the input value can't be represented in the output type, you get an error.

```py
int('hello')  #> throws ValueError
```

Sometimes the meaning of the input is _close enough_ and the cast works.

```py
int(5.5)  #> 5
```
