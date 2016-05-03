# URLs
A **uniform resource locator** or URL is a specially formatted string which specifies a generic **resource**.
That resource might be the HTML of a web page, or a video file, or some CSS, or any generic content.
It's an abstract concept.

A basic URL looks like:
```
http://host[:port]/path?query
```

* The **host** is the address of the computer that knows the content of the page.
* The optional **port** is a number that is basically the specific application on the computer.
* The **path** is a string that says what content the server should give you back; it looks like a filesystem path and is hierarchical.
* The **query** is a string that contains extra "arguments".
* The `http://` tells your web browser that it should use the **HTTP protocol** to talk to the server.

## Query Strings
**Query strings** are specially formatted ways of specifying key-value pairs as sort of "arguments" for a URL.
```
key1=value1&key2=value2
```

If the keys or the values themselves contain any URL characters, they are escaped via [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters).
```
motto=love%3Dblind&favorite_icecream=ben%20%26%20jerry%27s
```
