# Continuations

Python style says that lines shouldn't be more than 80 characters.
This is so each statement is simple and you can imagine it in your mind.

Here are a few techniques to make your code easier to follow.

## 1. Use Variables

First, avoid having long lines in the first place.
Variables are free, so use them all the time!
Whenever you have a concept in a program, put it in a named variable, which will break apart long lines and make the code easier to understand.

```py
road_trip_cost = miles / miles_per_gallon * cost_per_gallon_of_gas
```

```py
gallons = miles / miles_per_gallon
road_trip_cost = gallons * cost_per_gallon_of_gas
```

## 2. Use Parentheses

If you can't avoid the long line, Python will allow you to span a long expression across multiple ones if it is in parentheses.
You can add in no-op parentheses to allow this.

```py
message = 'This is a super long string'
biggest = max(1, 2, 3, 4, 5, 6)
```

Continuation lines should be indented to align with the first character after the opening paren.

```py
message = ('This is a super ' +
           'long string')
biggest = max(1, 2, 3,
              4, 5, 6)
```

If that still doesn't make the line short enough, you can return right after the opening paren and indent only four spaces.

```py
message = (
    'This is a super ' +
    'long string'
)
biggest = max(
    1, 2, 3,
    4, 5, 6,
)
```

## Beware String Literal Joining

Python has a mysterious feature called **string literal joining**.
It will automatically concatenate string literals _without a plus operator_.

```py
message = 'This is a super ' 'long string'
```

I would avoid using it because it's not uniform.
You can't use it to concatenate string variables.
It also silently might swallow other errors.
