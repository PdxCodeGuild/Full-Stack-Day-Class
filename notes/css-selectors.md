# CSS Selectors

CSS uses **selectors** to decide which elements should have style rulesets applied.

## Simple Selectors

There are three simple selectors: **type**, **class**, and **ID**.
They match on types or attributes of a _single_ element.

### Type

To select all elements of a given type, use the tag name as a plain symbol.

CSS:

```css
p {
    color: blue;
}
```

HTML:

```html
<p>Blue!</p>
<p>Blue!</p>
<blockquote>Not.</blockquote>
```

### Class

To select all elements in a given class of any type, use a period `.` then a class name.

CSS:

```css
.ice-cold {
    color: blue;
}
```

HTML:

```html
<p>Not.</p>
<p class="ice-cold">Blue!</p>
<blockquote class="ice-cold">Blue!</blockquote>
```

### ID

To select a specific single element by it's ID of any type or class, use a pound sign `#` then the ID.

CSS:

```css
#one-blue-thing {
    color: blue;
}
```

HTML:

```html
<p>Not.</p>
<p id="not-blue-thing">Not.</p>
<blockquote id="one-blue-thing">Blue!</blockquote>
```

## Operators

Selectors can also include operators, which allow you to match on document structure or combinations.

### Descendant

If you separate simple selectors by a _space_, it will match all elements for which the simple selectors match _in order_ down the document hierarchy.

CSS:

```css
.outer .inner {
    color: blue;
}
```

HTML:

```html
<p class="inner">Not.</p>
<p class="outer inner">Not.</p>
<blockquote class="outer">
    <p>Not.</p>
    <p class="inner">Blue!</p>
</blockquote>
```

### And

If you separate simple selectors _without a space_, it will match elements for which all the simple selectors match.

```css
p.yellow.blue {
    color: green;
}
```

HTML:

```html
<blockquote class="yellow">Not.</blockquote>
<p class="yellow blue">Green!</p>
<blockquote class="yellow">
    <p class="blue">Not.</p>
</blockquote>
```

## Advanced Selectors

Read through the [Mozilla CSS selectors reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#Selectors) for more exciting ones.
