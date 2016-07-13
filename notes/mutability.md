# Mutability

There are two kinds of values in Python, mutable and immutable.

**Immutable** values are constant.
Their **identity** is the same as their value.

You can change which integer is assigned to a variable, but you can't change the value of `7`, understandably.

```py
x = 7  # The box labeled "x" has 7 in it.
x = 5  # The box labeled "x" now has 5 in it. But we didn't "change 7".
# There is no command like:
# 7.increment() which changes the "value of 7".
```

Strings are also immutable.
Not because it doesn't make sense to "edit" a string, but because Python arbitrarily enforces this.
You get a `TypeError` if you try to modify a string.

```py
x = 'David'  # The box labeled "x" has 'David' in it.
x = 'Helen'  # The box labeled "x" now has 'Helen' in it. But we didn't "change David".
# We can't modify the string itself:
x[0] = 'Z'  # Throws TypeError
```

Every re-assignment of a variable changes the identity of the value within.

**Mutable** values can change without changing their identity.
Most containers, like lists, are mutable.

Assignment isn't the only way to modify the value of a variable.

```py
x = [4, 5]  # The box labeled "x" has the list #4325270728 in it. That list has [4, 5] in it.
x.append(6)  # Add 6 to that list #4325270728. The box labeled "x" is unchanged!
x  #> [4, 5, 6]
```

## Two Models

This seems fine, but represents a separate model of computation.

Most of the code we've seen thus far has had explicit inputs and outputs.
The code promises to not modify the input arguments when calculating the return value!
This new model doesn't have return values, instead modifies the input arguments!

How do you know which is going to happen?
_Look at the documentation._

If a method returns `None`, but seems like it should do something, it probably is mutating the input.
Most container type methods mutate the container in-place.
Most top-level functions return a modified copy of the input.

My advice:
**Avoid mutating methods.**

Almost all mutating container methods have an immutable version.

* `x + [6]` is better than `x.append(6)`
* `reversed(x)` is better than `x.reverse()`

## Trouble

Bugs happen when you expect your code will use one model, and instead it uses another model.

This function looks like it will leave the input untouched, but doesn't.

```py
def add_my_name(names):
    """Takes in a list of names and returns it with David appended."""
    names.append('David')
    return names

friends = ['Kate', 'Al']
friends_and_me = add_my_name(friends)
friends_and_me  #> ['Kate', 'Al', 'David']
# But, unfortunately:
friends  #> ['Kate', 'Al', 'David']
```

Try really hard to document your functions truthfully and tell the user about all mutations.
**Don't return and mutate.**
Read other people's docs carefully.
