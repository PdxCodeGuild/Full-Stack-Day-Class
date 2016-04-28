# JS in the Browser
We will be running all of our JS through a web browser.
Since a browser only loads HTML pages, add to it a `script` tag with a `src` attribute that is a path to a JS file to execute.

JS is parsed and run as soon as the `script` is found.
For this reason, you should include your `script` at the _end of the body_.
This prevents the running of JS from slowing down your page from initially appearing.

HTML:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <!-- The whole page. -->

        <script src="source.js"></script>
    </body>
</html>
```

JS:
```js
console.log('Hello!');
```

This will feel clunky at first, as we're not interacting with the HTML, but will feel natural when doing so.
