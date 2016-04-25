# Data Transforms
Similar to a list comprehension, JS arrays have a **map** method.
You pass in the function that you want called once on each input item that will return a corresponding item in the output array.
```js
var priceInCents = [100, 150, 400];
var priceInDollars = priceInCents.map(function(i) { return i / 100; });
```

That is equivalent to the following Python:
```py
price_in_cents = [100, 150, 400]
price_in_dollars = [i / 100 for i in price_in_cents]
```

The function given to map does not have to be a anonymous function literal, you can pass in a named function without calling it.
```js
var convertCentsToDollars = function(cents) {
    return cents / 100;
};
var priceInCents = [100, 150, 400];
var priceInDollars = priceInCents.map(convertCentsToDollars);
```
