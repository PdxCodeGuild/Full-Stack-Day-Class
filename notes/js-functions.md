# Functions and Calling

Functions are created by using the `function` keyword, then a name, then a list of argument variable names in parentheses separated by commas, then a `{}` enclosed block of statements to execute that may have a `return` statement.
Functions are called just like in Python with parentheses `()` to make them go.

```js
/**
 * Take an number and add two to it.
 */
function addTwo(x) {
    var two = 2;
    return x + two;
}
addTwo(5);  //> 7
```

## JSDoc

Functions should be commented with a [JSDoc](http://usejsdoc.org/about-getting-started.html).
It is a multi-line comment that starts with `/**` (note the two stars).
At least provide a one-line English description of what the function does.
If you want, there are lots of [fancy tags](http://usejsdoc.org/#block-tags) to help annotate parameters.
Feel free to install the Atom package [Docblockr](https://atom.io/packages/docblockr) package to make this easier.

## Scope

Functions in JS create a scope just like in Python.
Remember, the list of variable names creates variables in the scope; e.g. `x` is defined in the function.
The variable `two` is not accessible outside the function above.

If you forget an argument to a function when calling it, it does _not_ produce an error.
That argument gets filled in with `undefined` when the function runs.

```js
/**
 * Return the second argument.
 */
function returnSecond(x, y) {
    return y;
}
returnSecond(1);  //> undefined
```

## Naming

Proper JS style has function names in `camelCase` with the first letter lowercase.
