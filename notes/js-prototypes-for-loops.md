# Prototypes and For-In Loops

In order for this loop to work as is does in Python, you have to **guard** the for loop.
That is adding a kind of cryptic if statement in it.

```js
var x = {a: 1, b: 2};
var valuesTotal = 0;

// This is the boilerplate you'll use to iterate through an object.
for (var key in x) {
    // This is required because some properties can come from the prototype.
    // We'll discuss the details of this later.
    if ({}.hasOwnProperty.call(foo, key)) {
        var value = x[key];

        valuesTotal += value;
    }
}
```

If you don't want to remember this, you can use Lodash's `forOwn()`.

```js
var namesToAges = {
    'David': 99,
    'Mel': 80
};
_.forOwn(namesToAges, function(name) {
    var age = namesToAges[name];
    console.log(name + ' is ' + age + ' years old.');
})
```

If you want this loop to modify outside variables, though, you'll have to use `reduce()`.
