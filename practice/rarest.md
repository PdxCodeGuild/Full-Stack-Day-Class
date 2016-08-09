# Practice: Rarest

Save your solution in a directory in `practice/` named `rarest`.
Your HTML file should be named `index.html` and your JS file named `site.js` in that directory.

Given an object that maps names to ages, write a function `findRarestValue(obj)` that returns the rarest (least frequently occuring) age.

```js
var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

// 22 only appears twice; 20 appears three times; 25, four times
findRarestValue(namesToAges);  //> 22
```

## Advanced

Write a function `findRarestKeys(obj)` that returns a list of all the properties with that rarest age.

```js
findRarestKeys(namesToAges);  //> ['Alyssa', 'Stef']
```
