# Element Hierarchy

Have the hierarchy of your HTML reflect how you are thinking about the structure of the page.
Have uniform containing elements for all of the concepts on your page.

E.g. Have titles for a section live inside the section.
Don't mix `section`s and `div`s for top-level parts of the page.

Avoid:

```html
<h1>Page Title</h1>
<ul><li>Nav Option</li></ul>
<h2>Article One Title</h2>
<p>Article text.</p>
<h2>Article Two Title</h2>
<p>Article text.</p>
```

Instead:

```html
<header>
    <h1>Page Title</h1>
    <ul><li>Nav Option</li></ul>
</header>
<article>
    <h2>Article One Title</h2>
    <p>Article text.</p>
</article>
<article>
    <h2>Article Two Title</h2>
    <p>Article text.</p>
</article>
```
