# Practice: Grocery

Save your solution in a Django app, directory in `practice/`, and in a branch all named `grocery`.
This means there will be a directory `~/codeguild/practice/grocery/grocery`.

Write a very simple HTTP API that returns the price of various items in the grocery in a few different currencies.

Have support for the following currencies:

* USD
* EUR
* CNY
* JPY

Let's define that API.
In `views.py` and `urls.py` make routes for:

*   `GET /product/PRODUCT_NAME/price` should respond with the price in dollars.
    The response should look like `PRODUCT_NAME is AMOUNT dollars`.
    Return a `404 NOT FOUND` if trying to get an unknown product.

*   `GET /product/PRODUCT_NAME/price/CURRENCY` should respond with the price in that currency.
    The response should look like `PRODUCT_NAME is AMOUNT CURRENCY`.
    Return a `404 NOT FOUND` if trying to get an unknown product, and a `400 BAD REQUEST` if trying to convert to an unknown currency.

In `models.py`, add the following data:

```py
PRODUCTS = [
    {
        'name': 'apple',
        'price_dollars': 1.0,
    },
    {
        'name': 'pear',
        'price_dollars': 1.5,
    },
    {
        'name': 'grape',
        'price_dollars': 0.75,
    },
]
```

Then write a data lookup function `lookup_product_for_name(name)`
Throw a `KeyError` if that product isn't found.

In `logic.py` write out the following functions:

*   `price_for_product_name(name)`
    Throw a `KeyError` if the product isn't found.
    Use the model function you just wrote.

*   `convert_currency(in_amount, in_currency, out_currency)`
    Look up some exchange rate constants.
    Throw a `ValueError` if the output currency isn't found.

This structure walks you through the MVC pattern, and I'll be giving you feedback on having your more complex projects follow it too.
