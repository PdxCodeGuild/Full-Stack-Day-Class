# Named Tuples

Python has a immutable, sized, named selection called a **named tuple**.

```py
>>> from collections import namedtuple
>>> namedtuple('PersonEntry', ['phone', 'address'])
<class '__console__.PersonEntry'>
>>> PersonEntry = namedtuple('PersonEntry', ['phone', 'address'])
>>> PersonEntry('David', '503-555-9999')
PersonEntry(phone='David', address='503-555-9999')
>>> x = PersonEntry('David', '503-555-9999')
>>> x.phone
'David'
>>> x = PersonEntry('503-555-9999', 'David')
>>> x.phone
'503-555-9999'
>>> x.name
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    x.name
AttributeError: 'PersonEntry' object has no attribute 'name'
>>> x.
  File "<input>", line 1
    x.
     ^
SyntaxError: invalid syntax
>>>
>>> x = PersonEntry('503-555-9999', '123 Main')
>>> x.address
'123 Main'
>>> x.address = 'askdljf'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    x.address = 'askdljf'
AttributeError: can't set attribute
>>> x = PersonEntry('503-555-9999')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    x = PersonEntry('503-555-9999')
TypeError: __new__() missing 1 required positional argument: 'address'
>>>
```
