# Tuple Unpacking

```py
friends = ['Al', 'Kate']
phone_numbers = ['507-1', '507-2']
pairs = list(zip(friends, phone_numbers))
pairs  #> [('Al', '507-1'), ('Kate', '507-2')]

name, phone = pairs[0]

[(index * 2, name) for index, name in list(enumerate(friends))]
```
