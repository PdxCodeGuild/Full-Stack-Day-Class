# Box Model and Sizing

The **box model** is the basis for how elements are sized and laid out.

Every element has:

* **Content** -- inner material
* **Padding** -- space between core and border
* **Border** -- visible outline outside of padding of some thickness
* **Margin** -- space outside of border and neighboring elements

The "visual size" of the element includes the content, padding, and border.

![Box Model Diagram](/notes/layout-box-model.png)

## Content Size

You can explicitly set the content size using the **width** and **height** properties.
Remember, this sizes the inner content, so the whole element will appear _bigger_ if there is padding and a border.

You can also specify **percent sizes**.
They allow you to specify a percentage of the appropriate dimension of the _parent_ element.

```css
p {
    width: 50%;
}
```

## Padding, Border, and Margin Size

They can be specified for _all sides_ using their simply-named properties:

```css
p {
    padding: 5px;
    border: solid 1px black;
    margin: 10px;
}
```

There are also separate properties for each side for padding, border, and margin:

```css
p {
    padding-top: 10px;
    border-bottom: none;
}
```

For more detailed information consult the [Box Model Chapter](http://learn.shayhowe.com/html-css/opening-the-box-model/) of Learn to Code HTML & CSS.

## Box Sizing

If you want the browser to calculate the sum of widths of borders and paddings for your, you can change the `box-sizing` property to `border-box`.
Then `width` will set the inner content width taking into account borders and padding.

![Box Sizing Diagram](/notes/layout-box-model-sizing.png)

```css
div {
    box-sizing: border-box;
}
```
