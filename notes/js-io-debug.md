# Debug Output

You can use `console.dir()` to log _objects_ to the browser console.

```js
var name = "David";
var message = "Hello, " + name;
console.dir(message);
```

Note that this is _not just printing them_.
It will actually give you an interactive debug view of the object.
Use the drop-down arrows to see and explore a list of the properties and sub-objects.

```js
var productToPrice = {
    "apple": 0.99,
    "pear": 1.50
};
console.dir(productToPrice);
```

If you want to have something that looks more like the object literal printed, use `console.log()`.

```js
console.log(productToPrice);
```
