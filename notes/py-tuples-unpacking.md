# Tuple Unpacking

```py
friends = ['Al', 'Kate']
phone_numbers = ['503-1', '503-2']
pairs = list(zip(friends, phone_numbers))
pairs  #> [('Al', '503-1'), ('Kate', '503-2')]

name, phone = pairs[0]

[(index * 2, name) for index, name in list(enumerate(friends))]
```
