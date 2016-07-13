# If Expressions

```py
if name == 'David':
    phone = '102893901'
else:
    phone = 'Unknown'
```

```py
phone = '102893901' if name == 'David' else 'Unknown'

[
    letter.upper() if letter == 'd' else letter
    for letter
    in 'David'
    if letter != 'v'
]
```
