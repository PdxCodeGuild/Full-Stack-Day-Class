# Data Transforms
Here are the highlights of how to do the data transforms we talked about in Python via Underscore in JS.
There are _many_ more functions that do specific, related things, so do look at the [Underscore docs](http://underscorejs.org/).

## Mapping
Similar to a list comprehension, Underscore gives you the **map** method.
You pass in the function that you want called once on each input item that will return a corresponding item in the output array.
```js
var priceInCents = [100, 150, 400];
var priceInDollars = _.map(priceInCents, function (i) { return i / 100; });  //> [1.0, 1.5, 4.0]
```

That is equivalent to the following Python:
```py
price_in_cents = [100, 150, 400]
price_in_dollars = [i / 100 for i in price_in_cents]
```

Underscore also gives you `mapObject` which is like a dict comprehension but only changes values:
```js
var nameToAge = {'Mel': 45, 'Robert': 39}
var currentYear = 2016
var nameToBirthYear = _.mapObject(nameToAge, function (age) {
    return currentYear - age;
});
```

## Filtering
Underscore gives you `filter`.

## Sorting
Underscore gives you `sortBy`.

## Reducing
Underscore gives you `min` and `max`, but for all of the other operations you're used to, you have to build them by hand with a _very generic_ `reduce`.

Reduce takes three arguments: iterable, function to call on each item that updates a running total, and the starting running total.

To calculate the sum
```js
var total = _.reduce(
    [1, 2, 3],  // Thing to iterate over.
    function (runningTotal, item) {  // Function called on each number in the array.
        return runningTotal + item;  // Returns an updated running total.
    },
    0);  // Initial running total.
total;  //> 6
```

## Grouping
Underscore gives you `groupBy`.
This is so much nicer than appending to a dict of lists in Python.
