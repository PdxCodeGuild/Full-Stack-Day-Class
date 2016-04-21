# Control Statements
## If Statement
If statements have the same structure as Python.
They must have an `if` branch, can contain any number of `else if` branches, and may contain one `else` branch.
The boolean value that is checked is in parentheses followed by the block of code to run.
```js
var forecast;
if (temp > 90) {
    forecast = "hot";
} else if (temp > 70) {
    forecast = "nice";
} else {
    forecast = "cold";
}
```

## While Loop
While loops have the same structure as Python.
They have a boolean condition in parentheses and will repeatedly run the block of code while the condition is true.
```js
var num = 0;
while (num < 10) {
    num += 1;
}
```

## For and For-In Loops
There are two for loops in JS.

One goes over keys of an object.
_Do not use_ this for arrays.
```js
var x = {"a": 1, "b": 2};
var sum = 0;
for (var key in x) {
    var value = x[key];
    sum += value;
}
```

The other allows you to set a **initialization expression**, a **loop condition**, and a **update expression**.
Use this to go through arrays.
```js
var x = [1, 2, 3];
var sum = 0;
for (var i = 0; i < 10; i += 1) {
    var value = x[i];
    sum += value;
}
```
