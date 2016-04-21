# Functions and Calling
Functions are created by using the `function` keyword, then a list of argument variable names in parentheses separated by commas, then a `{}` enclosed block of statements to execute that may have a `return` statement.
A created function is then assigned to a name via a normal assignment statement, just like a variable.
Functions are called just like in Python.
```js
var addTwo = function(x) {
    var two = 2;
    return x + two;
};  // Note the semicolon. This is just assignment.
addTwo(5);  //> 7
```

Functions in JS create a scope just like in Python.
The variable `two` is not accessible outside the function above.

Proper JS style has function names in `camelCase` with the first letter lowercase.
