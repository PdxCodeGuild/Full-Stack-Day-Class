# Query Strings

**Query strings** are specially formatted ways of specifying key-value pairs as sort of "arguments" for a URL.

```
key1=value1&key2=value2
```

If the keys or the values themselves contain any URL characters, they are escaped via [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters).

```
motto=love%3Dblind&favorite_icecream=ben%20%26%20jerry%27s
```

This format can't handle nested data mappings.
