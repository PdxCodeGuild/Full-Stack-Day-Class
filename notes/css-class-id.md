# Classes and IDs

CSS provides a few tools for organizing your style _independent_ of the structure of elements.

## Classes

**Classes** are a way of "tagging" elements.
Multiple elements in a document can belong to the same class.

Fill out the `class` attribute with a space separated list of class names on the elements you want to tag.

```html
<p class="warning">Don't touch a hot stove!</p>
<p class="warning bordered">Don't eat soap!</p>
<h2 class="warning">Don't lose your house keys!</h2>
```

Class names should be in `kebab-case` and can not start with a number:
all lower case with words separated by `-`.

## IDs

**IDs** are unique names for individual elements.
Only one element per document can have an ID.

Fill out the `id` attribute with the unique name.

```html
<p id="stove-warning">Don't touch a hot stove!</p>
<p id="soap-warning">Don't eat soap!</p>
```

IDs should be in `kebab-case` and can not start with a number.
