# CSS Values

There are a few common types of values that CSS properties can have.
For each of those common types, there are a few different common units or ways of expressing them.

## Colors

Often you want to describe a color.
There are a few ways of representing one.

### Named Colors

There is a suite of named colors.
Use the color name in bare words.

```css
p {
    color: blue;
}
```

There are [a ton of them](http://www.somacon.com/p142.php).

### Hex Colors

Colors can also be specified as a `#RRGGBB` two digit hex triplet.
In hex, each digit goes from `0` to `9` then `A` to `F` for 16 "digits".

```css
p {
    /* Black */
    color: #000000;
    /* White */
    color: #FFFFFF;
    /* Red */
    color: #FF0000;
}
```

### Color Functions

Colors can also be specified using the `rgb()` or `hsl()` functions.

`rgb(red, green, blue)` is specified using three values between `0` and `255`.

`hsl(hue, saturation, lightness)` is specified as an angle between `0` and `359`, and two percentages between `0%` and `100%`.
The percent character `%` is required.

```css
p {
    color: rgb(0, 255, 0);
    color: hsl(180, 100%, 50%);
}
```

Both of these also have an "alpha version", which also takes an an **alpha value** or transparency between `0` and `1`, where `0` is fully visible and opaque.

```css
p {
    color: rgba(0, 255, 0, 0.75);
    color: hsla(180, 100%, 50%, 0.75);
}
```

## Lengths

Units of length can be specified in a few ways.

### Pixels

```css
section {
    width: 30px;
}
```

### Percentages

Percentages are sizes relative to the corresponding size of the _parent element_.

```html
<body>
    <section>
        <p>Hi!</p>
    <section>
</body>
```

```css
section {
    /* Will be 75% the width of the <body>, which is not necessarily the screen. */
    width: 75%;
}

p {
    /* Will be 75% the width of the <section>. */
    width: 75%;
}
```

### Ems

Ems are relative to the _current element's_ text size.
So if you have `1.0em` in an `h1` (which has big text) means something different that

Use ems for typographic measurements and layout, e.g. line spacing, font size, paragraph margins. Use pixels for whole document layout, e.g. borders, section margins, etc.

```css
/* Effective padding around the <header> will be 200px. */
header {
    font-size: 100px;
    padding: 2.0em;
}

/* Effective padding around <p> will be 100px. */
p {
    font-size: 50px;
    padding: 2.0em;
}
```
