# CSS Values

## Colors

### Named Colors

### Hex Colors

### Color Functions

## Sizes

### Pixels

### Percentages
Percentages are relative to the _parent element_.

```html
<body>
    <section>
        <p>Hi!</p>
    <section>
</body>
```

```css
section {
    width: 75%;
}

p {
    width: 75%;
}
```

### Ems
Ems are relative to the _current text size_.
So if you have `1.0em` in an `h1` (which has big text) means something different that

Use ems for typographic measurements and layout, e.g. line spacing, font size, paragraph margins. Use pixels for whole document layout, e.g. borders, section margins, etc.

```css

header {
    font-size: 100px;
    padding: 2.0em;
}

p {
    font-size: 50px;
    padding: 2.0em;
}
```
