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
