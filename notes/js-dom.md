# Basic Document Object Model

The browser provides a JS object "view" of the HTML called the **document object model** or **DOM**.
This is the global `document` object.

```js
document.url;  //> 'http://www.google.com/'
```

Every element (`<h2>`), attribute (`class="style"`), and inner text (`Section!`) is a sub-object on `document`.
These sub-object are called **nodes**.
All of the nodes look like a tree.

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

You'll get a node structure like:

*   Document

    *   `html` Element

        *   `body` Element

            *   `header` Element

                *   `h1` Element

                    * Inner Text - "Page!"

            *   `section` Element

                *   `id` Attribute

                    * Value - "s-one"

                *   `h2` Element

                    *   `class` Attribute

                        * Value - "style"

                    *   Inner Text - "Section!"

`document` is actually a pretty complex object since you can have multiple children and ordering.

The DOM _is the rendered web page_.
If you change the DOM, you change what is shown!

This allows you to programmatically change the page from your JS in response to things.
This is super powerful.
