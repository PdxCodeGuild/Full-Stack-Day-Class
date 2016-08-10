# Element Creation

jQuery also allows you to use `$` to create _new elements_.
Instead of a selector, pass _well-formed_ HTML.
It returns an element set containing that new element.

```js
var newImage = $('<img>');  // Returns an element set containing a new empty image element.
var newParagraph = $('<p>Hi!</p>');  // Returns an element set containing a new empty paragraph element.

// Neither of these work. Not well formed HTML.
// This does a selection.
var newImage = $('img');
// This paragraph tag should be closed.
var newParagraph = $('<p>');
```

This new element is **detached** from the DOM tree.
It is not on the page, and won't be shown.
_Yet_.
