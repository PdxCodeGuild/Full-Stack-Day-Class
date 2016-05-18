# Iterating
## Over Objects
Use Lodash's `forOwn`.

## Over Arrays
If you only want to simply go over each element and run some code _without output_, use `forEach`.
```js
var l = [1, 2, 3];
_.forEach(l, function(i) {
    console.dir(i);
});
```

If you want to do any sort of _aggregating output_, use `reduce`.
```js
_.reduce()
```
