# JSON
**JSON** or **JavaScript Object Notation** is a data serialization format.
A **serialization format** is a way to turn an in-memory data structure into a string and back.
You might use it to move data between your back-end Python code and your front-end JS code.

JSON is basically a _string_ containing a JS object literal.
That literal can only contain strings, numbers, booleans, arrays, and other objects.
```json
{
    "name": "David",
    "phone": "507-555-9895",
    "siblings": 2.0,
    "female": false,
    "citiesLivedIn": [
        {"name": "Portland"},
        {"name": "Oakland"}
    ]
}
```
Note that it's _just the object_.
There's no `var` or `;` or anything.

Basically every programming language contains versions of those data structures, so an instance of your data can be loaded into memory from a string in any language.

## JavaScript
In JS, if you have some data, you can use the `JSON.stringify` function to turn it into JSON.
This is kind of boring because JSON is based on JS, so it just looks like the literal.
```js
var david = {
    "name": "David",
    "phone": "507-555-9895",
    "siblings": 2.0,
    "female": false,
    "citiesLivedIn": [
        {"name": "Portland"},
        {"name": "Oakland"}
    ]
};
JSON.stringify(david);  //> "{\"name\":\"David\",\"phone\":\"507-555-9895\",\"siblings\":2,\"female\":false,\"citiesLivedIn\":[{\"name\":\"Portland\"},{\"name\":\"Oakland\"}]}"
```

Then use `JSON.parse`, to turn a JSON string your got somewhere into an object you can use.
Again, kind of boring.
```js
var jsonString = "{\"apple\":1.5,\"pear\":0.99}";
JSON.parse(jsonString);  //> {"apple": 1.5, "pear": 0.99}
```

## Python
Python gives you the `json` module with `dumps` and `loads` to do the same thing.
```py
import json

product_to_price = {
    'apple': 1.5,
    'pear': 0.99,
}
json.dumps(product_to_price)  #> '{\"apple\":1.5,\"pear\":0.99}'
json_string = ""
json.loads(json_string)  #>
```

Because Python has slightly different base data structures, some types [are converted](https://docs.python.org/3/library/json.html#py-to-json-table).
Also realize that some types can't be represented perfectly, Python sets are represented as arrays in JSON, Python class instances don't have any default JSON representation.
