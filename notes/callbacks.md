# Callbacks and Events
JS files are only executed at one time, when the browser parses the `script` tag.
How do we run code at other times?

During that initial parsing, we can tell the browser about existing functions and tell it when it should run those functions.
This is called giving the browser a **callback**.

The browser has a set list of kinds of **events** it knows how to look for, and lets you specify callbacks, called **event handlers** for them.

When those callbacks run, they can modify the _global state_ of the page and make things happen.

## Registering Event Handlers
jQuery gives you the `on()` function to register event handlers on specific events on specific elements.
You pass it an event name and then a function that will be called when that event happens.
```js
$("button").on("click", function () {
    $("body").css("background", "blue");
});
```

There are [many event names](http://api.jquery.com/Types/#Event), but the big one's you'll use are "click", "mousemove", "keydown", and "submit".

The handler function can take one optional argument, which is an object that contains facts about the event.
```js
$("button").on("click", function (event) {
    event.target.id();  //> "big-button"
});
```
You can look in the [event object docs](http://api.jquery.com/category/events/event-object/) for all the things you can do with that object.

## Ready
We also have one problem with registering event handlers, the elements we want to listen on _haven't been created yet_!
Our JS is parsed wherever the `script` tag is, which might before the rest of the HTML, so we need to delay our registering until that is done.
That is done with another callback on the part of the DOM that is already there, the `document` itself.

```js
var registerEventHandlers = function () {
    $("button").on("click", function () {
        $("body").css("background", "blue");
    });
};

$(document).ready(function () {
    registerEventHandlers();
});
```
