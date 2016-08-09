# Practice: Color

Save your solution in a directory in `practice/` named `color`.
Your HTML file should be named `index.html` and your JS file named `site.js` in that directory.

Make a `Color` type.
Implement a `Color(r, g, b)` constructor where the values are between 0 and 255.
Implement the following prototype methods:

* `blendAdd(other)` that returns a new color that sums the components of the two colors, ensuring they stay between 0 and 255
* `toHex()` that returns the CSS hex code as a string of the color like `#FF13C9`

```js
var yellow = new Color(255, 255, 0);
yellow.toHex();  //> '#FFFF00'
var purple = new Color(255, 0, 255);
purple.toHex();  //> '#FF00FF'
var white = yellow.blendAdd(purple);
white.toHex();  //> '#FFFFFF'
```
