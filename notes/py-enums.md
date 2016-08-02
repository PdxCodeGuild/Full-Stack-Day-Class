# Enums

If you ever have a variable that has a few different discrete options for values, you have an **enum** or enumeration.

Often times in Python you'd use strings or ints.

```py
stoplight_color = 'red'
if stoplight_color == 'green':
    press_gas()
```

Instead of using string literals, define a set of constants for each possible value.

```py
RED_LIGHT = 'red'
YELLOW_LIGHT = 'yellow'
GREEN_LIGHT = 'green'

stoplight_color = RED_LIGHT
if stoplight_color == GREEN_LIGHT:
    press_gas()
```

Do this because then you get all of the typo checking and consistency that PyCharm gives for variable names.
E.g. this code is broken!
But it doesn't look so.

```py
if stoplight_color == 'Green':
    press_gas()
```

In general, avoid "magic numbers" or "magic strings" and instead use a constant that has a name and ensures you know you're using the right value.
