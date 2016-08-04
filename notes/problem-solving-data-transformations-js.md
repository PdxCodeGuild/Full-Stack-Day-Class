# Data Transforms

Here are the highlights of how to do the data transforms we talked about in Python via Lodash in JS.
There are _many_ more functions that do specific, related things, so do look at the [Lodash docs](https://lodash.com/docs).

## Mapping

Similar to a list comprehension, Lodash gives you the **map** method.
You pass in the function that you want called once on each input item that will return a corresponding item in the output array.

```js
var priceInCents = [100, 150, 400];
var priceInDollars = _.map(priceInCents, function(i) { return i / 100; });  //> [1.0, 1.5, 4.0]
```

That is equivalent to the following Python:

```py
price_in_cents = [100, 150, 400]
price_in_dollars = [i / 100 for i in price_in_cents]
```

Lodash also gives you `mapKeys` and `mapValues` which is like a dict comprehension:

```js
var nameToAge = {Mel: 45, Robert: 39}
var currentYear = 2016
var nameToBirthYear = _.mapValues(nameToAge, function(age) {
    return currentYear - age;
});
```

## Filtering

Lodash gives you `filter`.

```js
_.filter([10, 99, 5, 104], function(num) { return num >= 50; });  //> [99, 104]
```

## Sorting

Lodash gives you `sortBy`.

## Reducing

JS gives you the for-loop and you can use an aggregating variable.
Lodash gives you `min()`, `max()`, `sum()`, and `reduce()`.

`reduce()` is cool.
Because of scoping, `forEach()` can modify variables in the outer scope.

```js
var sum = 0;
var l = [1, 2, 3];
_.forEach(l, function(i) {
    // This overwrites "sum" which will only exist in the scope of the function.
    sum += i;
});
sum;  //> 0
```

If you want to do any sort of _aggregating output_, use `reduce()`.
It's a super cool function.
Reduce takes three arguments: sequence, function to call on each item that updates a running total, and the starting running total.

To calculate a sum

```js
var total = _.reduce(
    [1, 2, 3],  // Thing to iterate over.
    function(runningTotal, item) {  // Function called on each number in the array.
        return runningTotal + item;  // Returns an updated running total.
    },
    0);  // Initial running total.
total;  //> 6
```

## Grouping

Lodash gives you `groupBy`.

```js
// I know this isn't exactly how you calculate a leap year, but good enough
var isLeapYearToYears = _.groupBy([1999, 2000, 2001, 2004],
    function(year) { return year % 4 == 0; });  //> {'true': [2000, 2004], 'false': [1999, 2001]}
```
