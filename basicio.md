# Basic IO
Thus far we've only been moving values _invisibly_ inside the program.

The following Python outputs _nothing_:
```python
name = 'David'
'Hi, ' + name
```

We have to _explicitly_ make values be print to or read from the terminal.
That is the only way to interface with the users of your program!

This is called **input / output** or **IO**.
Python gives us two functions to do that.

`print` prints an expression to the terminal as a string.
```python
print(value)
```

`input` waits for typing on the keyboard and returns the string of what was typed when "enter" is pressed.
```python
input()
```

Just calling `input` on it's own will _throw away_ the value from the keyboard.
You have to assign the value into a variable to save it for later.
```python
name = input()
```
