# Javascript Basics
JS is another structured, procedural programming language.
Statements are executed one at a time from top to bottom within a function and functions can call each other.

```js
"use strict";

/*
This function makes a greeting as a string
for a person given a name as a string.
*/
var makeGreeting = function (name) {
    return "Hi, " + greeting;
}

var name = "David";
// This is a comment.

console.log(makeGreeting(name));
```

Each statement must end with a `;`.

Blocks of code are delineated by braces `{}`.
Indentation is ignored by the interpreter.

There are two kinds of comments.
Single line comments start with `//` and comment out the remainder of the line.
Multi-line comments start with `/*` and end with `*/` and can span multiple lines.

Every JS file we write should be in **strict mode**.
This makes the behavior of variables less complicated.
At the top of every JS file, add:
```js
"use strict";
```

## The Good Parts
JS is a messy language.
It was rushed to implementation, and is often inconsistent.

I am teaching you a _subset_ of the language and specific patterns that are easy to understand within it.
There are many "flexibilities" in the language that you might come across: semicolons are optional, `var` is optional, etc.
But **follow the guidelines here**.
They are more likely to produce correct code.
