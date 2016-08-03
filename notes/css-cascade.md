# The Cascade and Specificity

All declarations in a rule set **cascade** down the hierarchy of the document until they are overridden by declarations from a more **specific** rule set.

CSS:

```css
body {
    color: blue;
}
```

HTML:

```html
<body>
    This text will be blue.
    <p>So will this text.</p>
    <div>
        <p>Anywhere down the hierarchy.</p>
    </div>
</body>
```

Only the most specific value for conflicting property applies.
Conflicts are not "the whole rule set or nothing".
To find the most specific rule set, look at (in-order of precedence):

1. Closest in the cascade
1. Most ID selector matches
1. Most Class selector matches
1. Most Type selector matches

For more information on selector specificity check out [Getting to Know CSS](http://learn.shayhowe.com/html-css/getting-to-know-css/#combining-selectors).

## Example

CSS:

```css
body {
    color: blue;
}

p {
    color: red;
}

.warning {
    color: yellow;
    font-style: italic;
}

#special {
    color: cyan;
}
```

HTML:

```html
<body>
    This text will be blue.
    <p>But this text is in a p, so red.</p>
    <p class="warning">This will be yellow and in italics.</p>
    <p class="warning" id="special">The ID selector overrides the color, so this is cyan, but the italics from the class stay.</p>
</body>
```
