# Default Layout

**Block elements** start on a new line and take the full horizontal width of their parent by default.
They can have all of their dimensions explicitly set.

**Inline elements** continue the current line and only take up minimal width and height for the contents.
They flow like text in a word processor.
They don't have an explicit width and height.

The web browser **flows** the page by going through the elements, gives them a width, then starts filling in content vertically.

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
This is so you don't have to already know the height of your _content_; the whole point is the browser does that for you.
This has consequences for [solving layout problems](/notes/problem-solving-layout.md).

## Margin Collapse

_Vertical_ margins collapse.
If two elements are after each other, the distance between the borders will be the maximum vertical margin.
It's like specifying a minimum vertical distance between elements.

Horizontal margins do not collapse.

If you want equal spacing between a matrix of items in a container, you can specify the left/right container padding to be half the spacing, the left/right item margin to be half the spacing, and the top/bottom item margin to be the full spacing.
