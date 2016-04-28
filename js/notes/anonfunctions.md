# Anonymous Functions
Functions _are just values_!
They are values that represent _instructions_.

We saw this a little in Python with sorting:
```python
names_to_ages = {
  'Robyn': 38,
  'Al': 15,
  'Amanda': 90
}
names = ['Robyn', 'Amanda', 'Al']

def get_age(name):
  return names_to_ages[name]

# No ()s! Gives function as value.
sorted(names, key=get_age)  # ['Al', 'Robyn', 'Helen']
```

Often times you only care about using a function as a value immediately, so there's _no need_ to give it a name.
This is called an **anonymous function**.
This is easy to do in JS, just don't assign your function to a variable.
```js
var namesToAges = {
  'Robyn': 38,
  'Al': 15,
  'Amanda': 90
};
var names = ['Robyn', 'Amanda', 'Al'];
names.sort(function (name1, name2) {
    return namesToAges[name1] - namesToAges[name2];
});
```

Also realize that you don't _have_ to pass in function arguments as anonymous ones.
```js
function getAgeForName(name1, name2) {
    return namesToAges[name1] - namesToAges[name2];
}
names.sort(getAgeForName);
```

```py

str(5)

x = 5
str(x)

```
