# Underscore
JS is made way better by using some utility libraries.
The first one we'll learn about is [Underscore](http://underscorejs.org).
It provides tons of utility functions for all of the data transformations you might dream of.

To include it, add another `script` tag before your script which will cause the browser to download and parse all of Underscore before your code.
```html
<script src="http://underscorejs.org/underscore.js"></script>
<script src="your.js"></script>
```

To use Underscore, you access the global variable named `_` and call functions on it.
```js
_.filter([1, 2, 3, 4, 5, 6], function (num) { return num % 2 == 0; });
```

Read through [the available functions](http://underscorejs.org/) and think about using them.
You'll heavily use `each`, `map`, `keys`, `values`, `pairs`.

Lots of them are very "functional" and will use [functions as values](anonfunctions.md) heavily.

I find using them to be cleaner and more consistent than their array prototype versions.
I encourage you to use the Underscore versions instead.
