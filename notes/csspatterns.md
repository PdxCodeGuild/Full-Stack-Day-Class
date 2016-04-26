# CSS Patterns
Here are some starter tips for planning out and writing your CSS.

* Style the `body` if you want something to apply text styling to everything
* Start with just element selectors; come up with defaults for every element, if there are reasonable defaults
* Come up with "consistent exceptions" to the element selectors and make classes
* Classes could be thought about as **mixins**; sets of attributes you want to apply arbitrarily to elements, e.g. "warning"
* Use unique ID for specific single exceptions on the page; avoid these
* Avoid using IDs for elements that are already unique: `html`, `body`, if your page contains a single `header`

Use the simplest selectors and rulesets possible.
Avoid:
* Specifying defaults on a type, then overriding most of them with classes
* Classes when type selectors will do
* IDs when structure selectors will do

Read through [this front-end tutorial](http://learn.shayhowe.com/html-css/writing-your-best-code/) for more tips on how to write good HTML & CSS.
