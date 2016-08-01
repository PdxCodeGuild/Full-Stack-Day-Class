# Floats

The most basic layout tool is **float**.
This causes an element to be fixed to a top corner of the parent element.
The remaining inline elements flow _around_ the floated element.

CSS:

```css
section {
    width: 150px;
}

img {
    float: left;
}
```

HTML:

```html
<section>
    <img src="elmo3.gif">
    <p>Here's some text about Elmo that will flow around the image.</p>
<section>
```

## Quirks

If you want to specify something to not flow around a float, and instead begin underneath it, you have to **clear** that element.
[Read about clearing](http://learnlayout.com/clear.html).

If your floated item is bigger than the un-floated content, you will have to **clearfix** the containing element so that it grows to be the size of the float. [Read about clearfixing](http://learnlayout.com/clearfix.html).
