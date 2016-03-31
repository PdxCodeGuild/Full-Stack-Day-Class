# Class String Casting
Python doesn't assume to know how to convert your type to a string.
```python
class AddressBookEntry:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

me = AddressBookEntry('David', '507-555-9895')
print(me)  # <__main__.AddressBookEntry object at 0x1043772e8>
```

Write a **magic str** function in your class to define how to cast to a string.
It must have the signature `__str__(self)` and return a string.
```python
class AddressBookEntry:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

  def __str__(self):
    return 'AddressBookEntry({}, {})'.format(
      self.name,
      self.phone_number
    )

me = AddressBookEntry('David', '507-555-9895')
print(me)  # 'AddressBookEntry(\'David\', \'507-555-9895\')'
```

You should always write a magic string method.
This will enable you to debug easily using print debugging.

What should you string representation look like?
I encourage you to return a string version of the call to the constructor.
> AddressBookEntry('David', '507-555-9895')
> AddressBookEntry(name='David', phone_number='507-555-9895')
