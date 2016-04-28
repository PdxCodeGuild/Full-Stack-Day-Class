# Prototype Methods
Python had type methods, similarly JS has prototype methods.
Without going into too much detail now, every instance of an object in JS is a "copy" of an original **prototype**, just with real values filled in.
You can look at the prototypes to see what methods are available.

They are accessed just like the short form of Python type methods, using the dot operator.
```js
var name = "David"
name.repeat(3);  //> "DavidDavidDavid"
"   x  ".strip();  //> "x"
```

As a crash course, here are the prototype methods on [strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#Methods_2) and  [arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Methods_2).
You can look at the [full reference for all types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference).

Before you commit all of these to heart, wait until we review [Underscore](underscore.md).
It will provide cleaner versions of many of these functions.

Awkwardly, there aren't really prototype methods for objects in the same way Python dictionaries had type methods.
This is because objects are why prototype methods work, which we'll discuss later.
