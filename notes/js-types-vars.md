# Basic Types and Variables

JS includes similar built-in types to Python.

## Basic Types

Here are an overview of the basic types and literals to form them.

### Numbers

Numbers are all floats.
Even if you don't include a decimal point.

```js
4.5
10
-100.0
```

### Strings

Strings are single quoted sequences of characters.

```js
'Hello!'
'wow'
```

### Booleans

Identical true and false values.
The literals are lower case.

```js
true
false
```

### Null

Similar to `None` in Python, this is a _deliberate_ non-value.

```js
null
```

### Undefined

Unlike anything in Python, undefined is an _uninitialized_ value.

```js
undefined
```

### Objects

Objects are like dictionaries in Python.
They are an unordered map from _only string_ **properties** (like keys) to values.

```js
{
    apple: 0.99,
    pear: 1.50
}
{}  // Empty object.
```

Only use quotes on the property names if they are not valid variable names:

```js
{
    'funny name': 100
}
```

### Arrays

Arrays are like lists in Python.
They are ordered sequences of items.

```js
[1, 2, 3]
["a", "b", "c"]
[]  // Empty list.
```

## Variables

Variables in JS must be **declared** before they are used.

To declare a variable, use the `var` keyword, then the variable name, then an initialized value, one on each line.

```js
var name = 'David';
var fruitToPrice = {apple: 0.99};
var FEET_PER_MILE = 5280;
```

Once a variable is declared, you don't use `var` to reference it.

```js
'Hi, ' + name;  //> 'Hi, David'
```

Proper JS style has variable names in `camelCase` with the first letter lowercase.
If your variable is storing something that is semantically constant, it should be in `CONSTANT_CASE`.
