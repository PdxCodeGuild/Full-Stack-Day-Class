# Practice: Completer

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `completer`.
Your HTML file should be named `index.html` and your JS file named `site.js` in that directory.

Many UIs have something like "autocomplete".
You start typing the prefix of a word and it gives a list of suggestions that match that prefix that you might want to type.
Let's implement the logic for that.

Make a `Completer` type.
Implement a basic `Completer()` constructor that takes no arguments.
Implement the following prototype methods:

* `addCompletion(str)` that adds a new, unique valid completion
* `removeCompletion(str)` that removes a valid completion
* `complete(prefix)` that returns an array of all valid completions that start with the given prefix, in any order

E.g.

```js
var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('banana');
// Only previously added completions that start with the given prefix are returned.
fruitCompleter.complete('a');  //> ['apple', 'avocado']
fruitCompleter.complete('b');  //> ['banana']
fruitCompleter.removeCompletion('apple');
fruitCompleter.complete('a');  //> ['avocado']
```

## Advanced

Let's modify the completer so that it learns which completions are used most often and suggests those.

Implement a new prototype method:

* `selectCompletion(str)` that adds weight to a valid completion, all completions start at zero weight

Modify:

* `complete(prefix)` that returns an array of all valid completions that start with the given prefix in order of descending weight, ties are broken by alphabetical order

E.g.

```js
var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('anise');
fruitCompleter.addCompletion('banana');
// All completions have zero weight, so all are in alphabetical order.
fruitCompleter.complete('a');  //> ['anise', 'apple', 'avocado']
fruitCompleter.selectCompletion('avocado');
// Avocado now has the most weight so is first, alphabetical order otherwise.
fruitCompleter.complete('a');  //> ['avocado', 'apple', 'anise']
fruitCompleter.selectCompletion('apple');
fruitCompleter.selectCompletion('apple');
// Apple now has the most weight, avocado next, then anise still has zero.
fruitCompleter.complete('a');  //> ['apple', 'avocado', 'anise']
```

## Super Advanced

Implement a separate **fuzzy completer** `FuzzyCompleter` which will take a possibly misspelled prefix and still give you completions.
I don't have a specific algorithm in mind for you to use, but come up with a function that specifically scores the "distance" between two prefixes.
Looking at [edit distance](https://en.wikipedia.org/wiki/Edit_distance) should be a good starting place.

Implement a new prototype method:

* `fuzzyComplete(prefix)`

```js
var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('anise');
fruitCompleter.fuzzyComplete('spp');  //> ['apple']
```
