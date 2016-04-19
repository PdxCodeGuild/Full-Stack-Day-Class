# Auto Margins
If you explicitly set a width of a block element and then set margins to `auto`, you'll get a centered column of block elements.

CSS:
```css
body {
    width: 75%;
    /*The first number is top-bottom margins, the second left-right.*/
    margin: 0px auto;
}
```

HTML:
```html
<body>
    <p>All of this will appear in the middle 75% of the page.</p>
    <p>As many block elements as you have.</p>
</body>
```
