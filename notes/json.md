# JSON

**JSON** or **JavaScript Object Notation** is a data serialization format.
A **serialization format** is a way to turn an in-memory data structure into a blob of bytes and back.
Use it if you want to move structured data between your back-end Python code and your front-end JS code, since the only way for the server to communicate with the browser is via the blobs of data in HTTP request bodies.

JSON is basically a _string_ containing a JS object literal with quoted property names.
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

You'll also have ~3 data structures with your data:

1. Django models
1. Python dict containing JSON-encodable copy of the data
1. String of the JSON transported over the wire
1. JS object containing the JSON-encodable copy of the data
