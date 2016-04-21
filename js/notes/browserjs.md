# JS in the Browser
We will be running all of our JS through a web browser.
Since a browser only loads HTML pages, add to it a `script` tag with a `src` attribute that is a path to a JS file to execute.

HTML:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <script src="source.js"></script>
    </head>
</html>
```

JS:
```js
console.log('Hello!');
```

JS runs as soon as it is included.

This will feel clunky at first, as we're not interacting with the HTML, but will feel natural when doing so.
