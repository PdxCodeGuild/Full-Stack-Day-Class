# jQuery
**jQuery** is a JS library that simplifies a lot of DOM manipulation tasks.
We will be using it off-the-bat, but realize that there are standard JS built-in [DOM manipulation functions](http://callmenick.com/post/basics-javascript-dom-manipulation).

To include it, add another `script` tag above yours which will cause the browser to download and parse all of the jQuery code before yours.
```html
<script src="https://code.jquery.com/jquery-2.2.3.js"></script>
<script src="your.js"></script>
```

To use jQuery, call the global variable `$`.
You can use it to [select existing elements](domqueries.md) or [create new ones](elementcreation.md).
```js
var allItems = $("li").addClass("red");
var newDiv = $("<div></div>");
```
