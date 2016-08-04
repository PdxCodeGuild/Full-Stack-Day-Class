# Control Statements

## If Statement

If statements have the same basic structure as Python.
They must have an `if` branch, can contain any number of `else if` branches, and may contain one `else` branch.
The boolean value that is checked is in parentheses `()` followed by the block of code to run.
The `()` are _required_, they are part of the syntax and not for grouping.

```js
var forecast;
if (temp > 90) {
    forecast = 'hot';
} else if (temp > 70) {
    forecast = 'nice';
} else {
    forecast = 'cold';
}
```

## While Loop

While loops have the same structure as Python.
They have a boolean condition in parentheses `()` and will repeatedly run the block of code while the condition is true.
The `()` are _required_, they are part of the syntax and not for grouping.

```js
var num = 0;
while (num < 10) {
    num += 1;
}
```

## For Loops

JS has for loops, but we'll [talk about them later](/notes/js-for-loops.md).
