# For Loops

There are two for loops in JS.

## For-In over Objects

One goes over keys of an object.
You declare a variable to hold each of the property names with `var`, then `in` then the object to iterate over.
The `()` are _required_, they are part of the syntax and not for grouping.

```js
var x = {a: 1, b: 2};
var valuesTotal = 0;

// This is the boilerplate you'll use to iterate through an object.
for (var key in x) {
    var value = x[key];

    valuesTotal += value;
}
```

**This should not be used for arrays.**
They will work, but they will not produce the desired behavior always.

## For over Arrays

The other allows you to set a **initialization expression**, a **loop condition**, and a **update expression**, each separated by `;`.
The `()` are _required_, they are part of the syntax and not for grouping.

Use that, an index variable, and checking the array length to go through arrays.

```js
var x = [1, 2, 3];
var valuesTotal = 0;

// This is the boilerplate you'll use to iterate through an array.
for (var i = 0; i < x.length; i += 1) {
    var value = x[i];

    valuesTotal += value;
}
```

If we unpacked all of the parts between `;`s in the for loop in Python, it would look like:

```py
x = [1, 2, 3]
values_total = 0

# Init expression:
i = 0
# Loop condition:
while i < len(x):
    value = x[i]

    # Block of the for loop:
    values_total += value

    # Update expression:
    i += 1
```

If you don't want to have to worry about dealing with lengths and incrementing, _without output_, use `forEach()`.

```js
var l = [1, 2, 3];
_.forEach(l, function(i) {
    console.dir(i);
});
```

Because of variable scoping, this won't allow you to modify outside vars, though.
You'll have to use `reduce()`.
