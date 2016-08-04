# Basic Operators

## Math

All of the math operators are the same.
E.g. `+`, `-`, `%`.

```js
5 + 6;  //> 11
10 % 3;  // 1
```

`+` works as string concatenation.

```js
'How now, ' + 'brown cow?'  //> 'How now, brown cow?'
```

All of the same advanced assignment operators work.
E.g. `+=`.

```js
var y = 6;
y += 2;
y;  //> 8
```

The only new operators you will encounter are `++` and `--` which add and subtract `1`.

```js
var x = 3;
x++;  //> 4
```

Consider using `x += 1`.
`++` and `--` act strange in compound statements.

## Comparison

* `===` is equals (notice it's **triple equals**)
* `!==` is not equals (notice it's **not triple equals**)

```js
var x = 'David';
var y = 'Helen';
x === y;  //> false
x !== y;  //> true
```

All of the other comparison operators are the same.
E.g. `<`.

The ordering operators do not have "triple versions".
E.g. there is no `<==` operator.
Just use the standard versions, `<=`.

You might encounter a "double equals" `==` and `!=` operator.
They are [almost the same](http://www.impressivewebs.com/why-use-triple-equals-javascipt/) as the triple equals versions, but have strange edge cases.
_Avoid_ using the double versions.

## Boolean Logic

* `&&` is and
* `||` is or
* `!` is not (it prefixes what you want to negate)

```js
var x = true;
var y = false;
var z = false;
(x && y) || !z;  //> true
```
