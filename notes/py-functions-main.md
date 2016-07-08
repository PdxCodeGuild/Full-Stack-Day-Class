# Main Function

Functions generate a new scope.
That means that variables newly defined in a function only exist in that function body, and variable names in the function body that clash with ones outside are actually different variables.

It also turns out that variables defined outside a function _can_ be accessed from inside a function.
This code runs without error.

```python
name = 'David'
def greeting():
    return 'Hello, ' + name

print(greeting())
```

This is an example of a function "taking input" without using an argument for it.
Don't do this!
**Only take inputs via arguments and return an output via a return value.**

To ensure that this structure causes an error, wrap the main part of your code in a function called `main()` and then immediately call it.

```python
def greeting():
    return 'Hello, ' + name  # Throws NameError

def main():
    name = 'David'
    print(greeting())

main()
```

Instead, ensure that your functions only take inputs via arguments.

```python
def greeting(name):
    return 'Hello, ' + name

def main():
    name = 'David'
    print(greeting(name))  # Hello, David

main()
```

Don't forget to immediately call `main()` at the end of your file.
Otherwise you've just defined a function and not said "go"!
