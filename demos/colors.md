# Demo: Colors

Write a simple HTTP API that responds with a plain text list of things that are a given color at `GET /things/COLOR`.
Return a `404 NOT FOUND` if there are no things of that color.

Use the following "database" of colored things:

```py
THINGS_AND_COLORS = [
    ('chair', 'blue'),
    ('dog', 'yellow'),
    ('sky', 'blue'),
    ('orange', 'orange'),
    ('blueberry', 'blue'),
    ('sun', 'yellow'),
    ('night', 'black'),
]
```

[Source](/demos/colors)
