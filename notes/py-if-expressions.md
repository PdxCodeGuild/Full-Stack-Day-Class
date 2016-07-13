# If Expressions

Often times if statements are deciding which of two values to "return".

```py
if temp > 70:
    weather = 'Nice'
else:
    weather = 'Cold'
```

Python gives us a slick way to inline this called an **if-expression**.

```py
weather = 'Nice' if temp > 70 else 'Cold'
```

This is great because it's an expression!
You can use it in all sorts of tiny places where only simple expressions are allowed like comprehensions.

```py
# Even numbers are doubled, odd numbers are tripled.
[
    i * 2 if i % 2 == 0 else i * 3
    for i
    in [1, 2, 3, 4]
]  #> [3, 4, 9, 8]
```

Avoid chaining too many of these together!
Function calls are also expressions and can capture much more complicated behavior easily.
Just define a function if you're worried about readability.

```py
def weather_for_temp(temp):
    """Return the weather forecast as a string for a temp."""
    if temp > 80:
        weather = 'Hot'
    elif temp > 60:
        weather = 'Nice'
    else:
        weather = 'Cold'


temps = [90, 65, 50, 80]
weather = [weather_for_temp(temp) for temp in temps]  #> ['Hot', 'Nice', 'Cold', 'Nice']
```
