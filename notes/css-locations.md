# Style Locations

You can specify CSS in _three_ places in your HTML.

## Linked Style

You can give the path to a separate CSS file to be included in your header.

This is the preferred method for specifying style over a whole website.

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

## Internal Style

You can write out CSS that should only be used on the current page in your header.

_Avoid_ unless you're prototyping a single page.

```html
<head>
    <style>
    strong {
        color: red;
    }
    </style>
</head>
```

## Inline Style

You can also specify style on a single element in your HTML.

_Avoid_ unless debugging.

```html
<p>Some <strong style="color: red;">red strong</strong> text.
    Some <strong>strong</strong> text.
</p>
```
