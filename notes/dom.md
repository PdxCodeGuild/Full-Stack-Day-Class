# Basic Document Object Model
The browser provides a JS object "view" of the HTML called the **document object model** or DOM.
This is the global `document` object.

```js
document.url;  //> "http://www.google.com/"
```

Every element (`<h2>`), attribute (`class="style"`), and inner text (`Section!`) is a sub-object on `document`.

If you web page structure looks like:
```html
<html>
    <body>
        <header>
            <h1>Page!</h1>
        </header>
        <section id="s-one">
            <h2 class="style">Section!</h2>
        </section>
    </body>
</html>
```

You'll get a structure _like_:
* Document
  * `html` Element
    * `body` Element
      * `header` Element
        * `h1` Element
          * Inner Text - "Page!""
      * `section` Element
        * `id` Attribute
          * Value - "s-one"
        * `h2` Element
          * `class` Attribute
            * Value - "style"
          * Inner Text

`document` is actually a pretty complex object since you can have multiple children and ordering.
Conveniently browsers give you lots of convenience functions for querying and manipulating the DOM, and thus the actual web page.
