# Anonymous Functions

Functions _are just values_!
They are values that represent _instructions_.

We saw this a little in Python with [sorting by key](/notes/sorting.md).

The array prototype function `map` produces an output array with the return values of calling the function argument on each element of the input array.

```js
var namesToAges = {
  'Robyn': 38,
  'Al': 15,
  'Amanda': 90
};
var names = ['Robyn', 'Amanda', 'Al'];

function getAgeForName(name) {
    return namesToAges[name];
}
names.map(getAgeForName);  //> [38, 90, 15]
```

Often times you only care about using a function as a value immediately, so there's _no need_ to give it a name.
This is called an **anonymous function**.
This is easy to do in JS, just don't give your function a name.

```js
names.map(function(name) {
    return namesToAges[name];
});  //> [38, 90, 15]
```

This is just like passing a literal as an argument vs. passing a variable containing the same value.

```js
var x = 5;
String(x);  //> "5"

String(5);  //> "5"
```

Remember anonymous functions are still just function definitions, they _don't run_ the code yet.
To drive this home, you can do strange things like this:

```js
function (x) {
    return x + 2;
}(4);  //> 6

function addTwo(x) {
    return x + 2;
}
addTwo(4);  //> 6
```
