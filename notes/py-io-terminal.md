# Terminal IO

Thus far we've only been moving values _invisibly_ inside the program.
The following Python outputs _nothing_.

```py
name = 'David'
'Hi, ' + name
```

We have to _explicitly_ make values be print to or read from the terminal.
That is the only way to interface with the users of your program!

This is called **input / output** or **IO**.
Python gives us two functions to do that.

The `print` function prints an expression to the terminal as a string on it's own line.

```py
name = 'David'
print(name)  # 'David' (without quotes) will appear in the terminal.
```

The `input` function waits for typing on the keyboard and returns the string of what was typed when "enter" is pressed.

```py
input()
```

Just calling `input` on it's own will _throw away_ the value from the keyboard.
You have to assign the value into a variable to save it for later.

```py
name = input()
```
