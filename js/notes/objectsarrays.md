# Basic Objects and Arrays
## Objects
You can get and set values for a key in an object with _two_ access syntaxes.
Standard subscripting with `[]` like on Python dictionaries, but also the `.` operator like Python modules.
Both are ways to "reach inside".
```js
var fruitToPrice = {
    "apple": 0.99,
    "pear": 1.50
};
fruitToPrice["apple"];  //> 0.99
fruitToPrice.apple;  //> 0.99
fruitToPrice["pear"] = 2.0;
fruitToPrice.pear = 2.0;
```

## Arrays
You can get and set values at an index in an array just like Python, using `[]` subscripting.
Arrays also have a length property.
```js
var fruits = ["apple", "pear"];
fruits[0];  //> "apple"
fruits[1] = "banana";
fruits.length;  //> 2
```
