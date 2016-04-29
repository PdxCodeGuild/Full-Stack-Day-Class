# Anonymous Functions
Functions _are just values_!
They are values that represent _instructions_.

We saw this a little in Python with [sorting by key](../../notes/sorting.md).

Often times you only care about using a function as a value immediately, so there's _no need_ to give it a name.
This is called an **anonymous function**.
This is easy to do in JS, just don't assign your function to a variable.

The array prototype function `map` produces an output array with the return values of calling the function argument on each element of the input array.
```js
var namesToAges = {
  'Robyn': 38,
  'Al': 15,
  'Amanda': 90
};
var names = ['Robyn', 'Amanda', 'Al'];

names.map(function (name) {
    return namesToAges[name];
});  //> [38, 90, 15]
```

Also realize that you don't _have_ to pass in function arguments as anonymous ones.
There's no difference between the two.
```js
function getAgeForName(name) {
    return namesToAges[name];
}
names.map(getAgeForName);  //> [38, 90, 15]
```

This is just like passing a literal as an argument vs. passing a variable containing the same value.
```js
String(5);  //> "5"

var x = 5;
String(x);  //> "5"
```
