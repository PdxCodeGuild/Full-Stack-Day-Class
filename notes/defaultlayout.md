# Default Layout
By default, block level elements appear left-justified on their own "rows", have the full width of the parent element, and have a height just big enough to contain the children.
Containment does _not_ include the margin; it does include the core content, padding, and border.

```html
<!-- This body will be the full width of the page and the height of the section. -->
<body>
    <!-- This section will the full width of the body and the height of two lines. -->
    <section>
        <p>This is one line high and the full width of the page.</p>
        <p>This is one line high and the full width of the page.</p>
    </section>
</body>
```

Notice that _width_ is top-down and _height_ is bottom-up.
This is because you want to have page length be a function of _content_ existing, not you adding up heights correctly.
This has consequences for [solving layout problems](layoutproblemsolving.md).
