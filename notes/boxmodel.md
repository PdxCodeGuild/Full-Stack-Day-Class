# Box Model and Sizing
The **box model** is the basis for how elements are sized and laid out.

Every element has a:
* **Width** and **Height** -- core size of content
* **Padding** -- extra space between core and border
* **Border** -- visible outline of some thickness
* **Margin** -- extra space between border and neighboring elements

![Box Model Diagram](boxmodel.png)

Margins _overlap_.
They are like specifying a minimum distance between elements.

They can be specified on _all sides_ using their named properties:
```CSS
p {
    width: 100px;
    height: 100px;
    padding: 5px;
    border: solid 1px black;
    margin: 10px;
}
```

There are also separate properties for each side for padding, border, and margin:
```CSS
p {
    padding-top: 10px;
    border-bottom: none;
}
```

**Block elements** start on a new line and take up as much _horizontal_ space as possible by default.
They can have all of their dimensions explicitly set.

**Inline elements** continue the current line and only take up _minimal_ width and height for the contents.
They flow like text in a word processor.
They don't have an explicit width and height.

You can also specify **percent sizes**.
They allow you to specify a percentage of the property value in the _parent_ element.
```css
p {
    width: 50%;
}
```

For more detailed information consult the [Box Model Chapter](http://learn.shayhowe.com/html-css/opening-the-box-model/) of Learn to Code HTML & CSS.
