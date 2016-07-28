# URLs and Paths

A **uniform resource locator** or URL is a specially formatted string which specifies a generic **resource**.
That resource might be the HTML of a web page, or a video file, or some CSS, or any generic content.
It's an abstract concept.

A basic URL looks like:

```
http://host[:port]/path[?query]
```

*   The `http://` tells your web browser that it should use the **HTTP protocol** to talk to the server.

*   The **host** is the netword address of the computer that knows the content of the page.

*   The optional **port** is a number represents the specific application on the computer.
    By default, HTTP servers run on port 80.

*   The **path** is a string that says what content the server should give you back; it looks like a filesystem path and is hierarchical.
    It does _not contain the leading slash_; the slash is the separator.

*   The **query** is a string that contains extra "arguments" using the format below.

Both the path and query string are free-form and are the only part of the URL the web server actually sees;
the rest are for routing.
They tend to look like described above, but can be any arbitrary string.

## Paths

Whenever a web page needs to reference another resource, like an image or stylesheet, it can either be via a full URL, or a **relative path**, these act just like the [filesystem paths](/notes/filesystem.md#paths) you've been using in the terminal.

If the exposed URLs paths of your site look like.

```
/index.html
/images/index.html
/images/one.jpg
```

* From `/index.html` you can refer to `/images/one.jpg` as `images/one.jpg`
* From `/images/index.html` you can refer to `/images/one.jpg` as `one.jpg`
