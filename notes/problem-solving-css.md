# CSS Problem Solving

Here are some starter tips for planning out and writing your CSS.

* Style the `body` if you want something to apply text styling to everything
* Start with just element selectors; come up with defaults for every element, if there are reasonable defaults
* Come up with "consistent exceptions" because of HTML structure and select on structure
* Come up with "consistent exceptions" to the element selectors and make classes
* Classes could be thought about as **mixins**; sets of attributes you want to apply arbitrarily to elements, e.g. "warning"
* Use unique ID for specific single exceptions on the page; avoid these
* Avoid using IDs for elements that are already unique: `html`, `body`, if your page contains a single `header`

Use the simplest selectors and rulesets possible.
Avoid:

* Specifying defaults on a type, then overriding most of them with classes
* Classes when type or structure selectors will do
* IDs when type or structure selectors will do

Read through [this front-end tutorial](http://learn.shayhowe.com/html-css/writing-your-best-code/) for more tips on how to write good HTML & CSS.

## "Normalizers" or "CSS Resets"

Some people have produced CSS files that "reset" browser defaults or supposedly "normalize" CSS across different browsers.

**You do not need these here.**
Do not use them in your problems.

For one, we're only developing for Chrome in this class and the things they normalize are very minor.
For two, when you're learning CSS they are a large amount of added complexity from ~50 bonus rulesets makes it much more difficult to learn the basics correctly.
