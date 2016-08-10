# DOM Manipulation

The global `$` function allows you to select or create elements.
Those might seem unrelated, but realize that they both _return element sets_.

An element set gives you lots of functions to query and modify the selected DOM structures.

Read through [the API docs](http://api.jquery.com) to become familiar with what kind of things you can do.
I'll go over the basics, though.

All of these functions use **mutative method chaining** style.
That means that they modify their input in-place _and_ return the input.
Strange, I know.

E.g. select all paragraphs, add a CSS class, and insert a new child span within each one.

```js
$('p').addClass('yellow')
  .append($('<span></span>'));
```

## Classes

* `.hasClass(className)`

* `.addClass(className)`
* `.removeClass(className)`
* `.toggleClass(className)`
* `.removeClass()` -- all the classes

## CSS

In addition to whole classes, you can get or modify specific CSS properties.

* `.css(propertyName)`

* `.css(propertyName, newValue)`

## Attributes

* `.attr(attrName)`

* `.attr(attrName, newValue)` -- setter

## Elements

* `.before(elementSet)`
* `.after(elementSet)`

* `.prepend(elementSet)` -- called on parent to add children
* `.append(elementSet)` -- called on parent to add children

* `.remove()`

## Form Value

* `.val()`

* `.val(newValue)`

## Generic

```js
$('div').each(function(index, element) {
    $(element).val();
});
```
