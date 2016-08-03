# Basic CSS

CSS is a **declarative** way to style the structure you specified in your HTML.
You give a list of **rule sets** and the web browser figures uses a set of rules to figure out how things are styled.

Similar to HTML, you are not giving a list of instructions for the computer to run line-by-line, unlike Python.

## Rule Set

A rule set is a **selector** which specifies which elements in a document match, then a set of **rule declarations** which are **properties** and **property values** separated by `:` and ending in a semicolon `;`.

```css
/* p is the selector, it selects all <p> elements. */
p {
    /* color is the property, red is the value. */
    color: red;
    /* font-size is the property, 15px is the value. */
    font-size: 15px;
}

/* p is the selector, it selects all <blockquote> elements. */
blockquote {
    font-family: monospace;
}
```

## Logistics

CSS should live in a separate `.css` file for reusability.
You can instruct your HTML to use some external CSS via a `link` element in your `head`.
For simple sites, have all the CSS live in a `site.css` file.

The `rel` attribute must be `stylesheet`, saying that we're "linking up a stylesheet" and the `href` attribute must be the path to the CSS file.

```html
<head>
    <link rel="stylesheet" href="site.css">
</head>
```
