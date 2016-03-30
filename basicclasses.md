# Basic Classes
Remember how modules group functions?
Classes are similar in that they group functions and variables into a **type**.
All those functions operate on a shared set of variables, without needing to pass them in as parameters.

You should create new classes when you want to represent a _fixed, structured value_ in your code.
For example:
* A "playing card" value has a suit and a card number
* An "address book entry" value has a name and a phone number
* An "image" value has a width and a height and some image data.

The types you make are just like the types you've seen already: strings, ints, etc.

## Defining
Similar to defining a function with `def`, you define a class via `class`, then define the functions you want to live in the type in a block.

Every class starts with a function named something funny: `__init__`.
You read this aloud as **magic init** (or double-under / dunder init if you're Googling around).
```python
class PlayingCard:
  def __init__(self, suit_string, value_string):
    self.suit_string = suit_string
    self.value_string = value_string
```

Then to make or **instantiate** a value of that type, call the type name.

```python
a card = PlayingCard('Spades', 'Q')
```

## Methods
