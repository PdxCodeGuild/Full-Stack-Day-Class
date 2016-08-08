# Prototypes and For-In Loops

So now there are two locations properties could come from:

1. The object itself
1. Any of its prototypes down the chain

A [for-in loop](/notes/js-for-loops.md) goes through _both kinds_ of properties!

If you want the loop to only go over properties that that object directly has, you have to **guard** the for loop.

```js
var x = {a: 1, b: 2};
var valuesTotal = 0;

for (var key in x) {
    // This will only run the body when the property is directly on x.
    if (x.hasOwnProperty(key)) {
        var value = x[key];

        valuesTotal += value;
    }
}
```

In general, for-in loops are only used on objects representing mapped data (as opposed to a structured object), and they don't have a prototype, so this won't cause problems.
The linter still requires you to put it because it clarifies the intent of the loop.

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
