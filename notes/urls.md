# URLs

A **uniform resource locator** or URL is a specially formatted string which specifies a generic **resource**.
That resource might be the HTML of a web page, or a video file, or some CSS, or any generic content.
It's an abstract concept.

A basic URL looks like:
```
http://host[:port]/path[?query]
```

* The `http://` tells your web browser that it should use the **HTTP protocol** to talk to the server.
* The **host** is the address of the computer that knows the content of the page.
* The optional **port** is a number that is basically the specific application on the computer.
By default, HTTP servers run on port 80.
* The **path** is a string that says what content the server should give you back; it looks like a filesystem path and is hierarchical.
It does _not contain the leading slash_; the slash is the separator.
* The **query** is a string that contains extra "arguments" using the format below.

Both the path and query string are free-form and are the only part of the URL the web server actually sees;
the rest are for routing.
They tend to look like described above, but can be any arbitrary string.

## Query Strings

**Query strings** are specially formatted ways of specifying key-value pairs as sort of "arguments" for a URL.
```
key1=value1&key2=value2
```

If the keys or the values themselves contain any URL characters, they are escaped via [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters).
```
motto=love%3Dblind&favorite_icecream=ben%20%26%20jerry%27s
```

This format can't handle nested data mappings.
