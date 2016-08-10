# Events and Callbacks

JS files are only executed at one time, when the browser parses the `script` tag.
How do we run code at other times?

The browser has a set of kinds of **events** that can happen _to elements_.
It lets you give it a function, named a **callback** or **event handlers**, to call when that event happens.
You can register that callback function on the first parse through the JS.

## Registering Event Handlers

jQuery has `on()` function to register callbacks for specific events on specific elements.
You pass it an event name and then a callback function.

```js
$('button').on('click', function() {
  $('body').css('background', 'blue');
});
```

There are [many event names](http://api.jquery.com/Types/#Event), but the big one's you'll use are "click", "mousemove", "keydown", and "submit".

The callback can take one optional argument, which is an object that contains facts about the event.

```js
$('button').on('click', function(event) {
  event.target.id();  //> "big-button"
});
```

You can look in the [event object docs](http://api.jquery.com/category/events/event-object/) for all the things you can do with that object.

### Disabling Defaults

Sometimes the event you want to check has a default action by the browser.
Clicking a link or submitting a form load a new page by default.
In you callback, if you take in the event object, you can tell it to disable the default behavior with `event.preventDefault()`.

```js
$('a').on('click', function(event) {
  // Prevent this link from actually going anywhere.
  event.preventDefault();
  // Then do all of the other stuff you want in your callback.
});
```

## Event Bubbling

HTML is a hierarchy.
Every event **bubbles** up the page hierarchy.

If your page was:

```html
<!DOCTYPE html>
<html>
    <body>
        <ul>
            <li>Hi!</li>
        </ul>
    </body>
</html>
```

And you click on the `li`, events will be fired on:

1. `li`
1. `ul`
1. `body`
1. `html`

Realize that an event does not stop bubbling when a handler is found; it will always go all the way up the hierarchy.

## Ready

What if the elements we want to register callbacks on don't exist yet?
This could happen if your script tag is before the `body`.

You can use another callback!
jQuery lets you give `ready` a callback that can setup all of the handlers.

```js
function registerEventHandlers() {
  $('button').on('click', function () {
    $('body').css('background', 'blue');
  });
}
$(document).ready(registerEventHandlers);
```
