# JavaScript Basics

**JavaScript** or **JS** is another structured, procedural programming language.
Statements are executed one at a time from top to bottom within a function and functions can call each other.

This might _feel_ totally new, but it contains all of the same concepts as Python.
Your knowledge will be very transferable.

JS lives in files with a `.js` extension.

```js
'use strict';

/*
This function makes a greeting as a string
for a person given a name as a string.
*/
var makeGreeting = function (name) {
    return 'Hi, ' + greeting;
}

var name = 'David';
// This is a comment.

console.log(makeGreeting(name));
```

Each statement must end with a `;`.

Blocks of code are delineated by braces `{}`.
Indentation is ignored by the interpreter, but our [style guide](/notes/js-style.md) says blocks are indented two spaces.

There are two kinds of comments.
Single line comments start with `//` and comment out the remainder of the line.
Multi-line comments start with `/*` and end with `*/` and can span multiple lines.

Every JS file we write should be in **strict mode**.
This makes the behavior of variables less complicated.
At the top of every JS file, add:

```js
'use strict';
```

## The Good Parts

JS is a messy language.
It was implemented in ten days, and is often inconsistent.

I am teaching you a _subset_ of the language and specific patterns that are easy to understand within it.
There are many "flexibilities" in the language that you might come across: semicolons are optional, `var` is optional, etc.
But **follow the guidelines here**.
They are more likely to produce correct code.

## The Culture

Because JS is the _only_ native language you can run on a web browser, it has immense value and is very accessible.
Because it's initial implementation was very basic and inconsistent, people have produced tons of code to assist.

I'm not exactly sure why, but there is a strong "independent streak" in the JS community.
There are sometimes tens of packages that do equivalent things for pretty core operations (testing, string manipulation, modules, UI frameworks, async packages), language features are being added to specs at a breakneck pace that duplicate functionality provided by packages, and tooling seems to be constantly re-invented.

IMHO it's kind of a hard-to-keep-up-with shit-show, but that is by no means a universal thought.
It is exciting to have your code be very accessible and impactful and be able to draw upon lots of existing work.
