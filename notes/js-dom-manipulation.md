# DOM Manipulation

The global `$` function allows you to select or create elements.
Those might seem unrelated, but realize that they both _return element sets_.

An element set gives you lots of functions to query and modify the selected DOM structures.

Read through [the API docs](http://api.jquery.com) to become familiar with what kind of things you can do.
I'll go over the basics, though.

All of these functions use **method chaining** style.
Setter functions modify their input in-place _and_ return the input.
Getter functions return their found value.
Strange, I know.

A general pattern is the default function signature is the _getter_ and the "one longer argument" version is the _setter_.

E.g. select all paragraphs, add a CSS class, and insert a new child span within each one.

```js
$('p').addClass('yellow')
  .append($('<span></span>'));
```

## Inner Text

### Getter

* `.text()`

### Setter

* `.text(newText)`

## Form Value

### Getter

* `.val()`

### Setter

* `.val(newValue)`

```js
$('input#name').val();  //> 'David'
$('input#name').val('Helen');
```

## CSS

In addition to whole classes, you can get or modify specific CSS properties.

### Getter

* `.css(propertyName)`

### Setter

* `.css(propertyName, newValue)`

```js
$('body').css('background-color');  //> 'blue'
$('body').css('background-color', 'blue');  // Returns the element set
```

## Classes

### Getter

* `.hasClass(className)`

### Setter

* `.addClass(className)`
* `.removeClass(className)`
* `.toggleClass(className)`
* `.removeClass()` -- all the classes

## Attributes

### Getter

* `.attr(attrName)`

### Setter

* `.attr(attrName, newValue)` -- setter

## Elements

* `.before(elementSet)` -- call on sibling
* `.after(elementSet)`

* `.prepend(elementSet)` -- called on parent to add children
* `.append(elementSet)` -- called on parent to add children

* `.remove()`

```html
<body>
  <header>...</header>
</body>
```

```js
$('header').after($('<section></section>'));
```

## Generic

You can

```js
$('div').each(function(index, element) {
  index; //> 0; integer of the element in the selection
  $(element).val();
});
```
