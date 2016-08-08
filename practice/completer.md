# Practice: Completer

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `completer`.
Your HTML file should be named `index.html` and your JS file named `site.js` in that directory.

Make a `Completer` type.
Implement a basic `Completer()` constructor that takes no arguments.
Implement the following prototype methods:

* `addCompletion(str)` that adds a valid completion
* `removeCompletion(str)` that removes a valid completion
* `complete(prefix)` that returns an array of all valid completions that start with the given prefix

Use JS's built-in [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp) type to do matching.
Yes, it's a little overkill, but I think it's useful to practice.

## Advanced

Let's modify the completer so that it learns which completions are used most often and suggests those.

Implement:

* `selectCompletion(str)` that adds weight to a valid completion

Modify:

* `complete(prefix)` that returns an array of all valid completions that start with the given prefix in order of descending weight

## Super Advanced

Try implementing a **fuzzy completer** which will take a possibly misspelled prefix and still give you completions.

* `fuzzyComplete(prefix)`
