# Lodash

JS is made way better by using some utility libraries.
The first one we'll learn about is [Lodash](https://lodash.com).
It provides tons of utility functions for all of the data transformations you might dream of.

To include it, add another `script` tag before your script which will cause the browser to download and parse all of Lodash before your code.

```html
<script src="http://cdn.jsdelivr.net/lodash/4.11.2/lodash.js"></script>
<script src="your.js"></script>
```

To use Lodash, you access the global variable named `_` and call functions on it.

```js
_.filter([1, 2, 3, 4, 5, 6], function (num) { return num % 2 == 0; });  //> [2, 4, 6]
_.includes([1, 2, 3], 3);  //> true
```

Read through [the available functions](https://lodash.com/docs) and think about using them.
You'll heavily use `forEach`, `includes`, `map`, `keys`, `values`, `toPairs`.

Lots of them are very "functional" and will use [functions as values](/notes/js-functions-anon.md) heavily.

I find using them to be cleaner and more consistent than their array prototype versions.
I encourage you to use the Lodash versions instead.

## Common functions

* `forEach()`
* `keys()`
* `values()`
* `map()`
* `filter()`
* `minBy()`
* `groupBy()`
* `countBy()`
* `pad()`
* `join()`
* `without()`
