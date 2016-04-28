# Element Creation
jQuery also allows you to use `$` to create _new elements_.
Instead of a selector, pass well-formed HTML.
It returns an element set containing that new element.
```js
var newImage = $("<img>");  // Returns an element set containing a new image element.
var newParagraph = $("<p></p>");  // Returns an element set containing a new paragraph element.
```

This new element is **detached** from the DOM tree.
It is not on the page, and won't be shown.
_Yet_.
