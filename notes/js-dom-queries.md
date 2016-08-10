# DOM Queries

jQuery gives you one global function to find DOM nodes.
It is `$`.
Pass it a CSS selector to get an **element set** (also called a **jQuery object**) of all matching elements.
It does _not_ return an array.

```js
var allItems = $('li');  // Returns an element set of all of the "li" elements.
var pictureElement = $('#my-picture');  // Returns an element set of just the element with ID "my-picture".
var allYellowDivs = $('div.yellow');
```

There are other [more advanced selectors](http://api.jquery.com/category/selectors/).
They go beyond even what CSS provides.
