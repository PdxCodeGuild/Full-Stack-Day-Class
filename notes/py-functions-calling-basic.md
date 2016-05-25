# Function Calling

Operators are the super basic verbs of programming represented by symbols.
But there are only so many symbols.

**Functions** give a name to a set of instructions that transform multiple input arguments to a single return value.

```
argument value -\
argument value --+- function --> return value
argument value -/
```

Python gives us a function called `max`.
It returns the bigger of the two input arguments.

To use a function, you **call**.
Provide the **name** of the function, then an `()`, then a comma separated list of expressions to **pass** as inputs, then a `)`.
The `()`s are _required_ to make the function actually go.

```py
max(5, 9)  #> 9
```

The _order_ of the arguments is important.
Depending on the function, it might _interpret_ the values of the arguments differently.

E.g. Python gives us another function called `pow`.
It takes two arguments:
the first is the base, the second is the exponent.

```py
pow(3, 2)  #> 9
pow(2, 3)  #> 8
```

If the output of a function doesn't depend on any input values, it can take _no_ arguments also!

```py
make_gettysburg_address()  #> "Four score and seven years..."
generate_random_month()  #> "April"
```

A function call is another expression, along with literals and operators with input values, and thus interchangeable with all other expressions.

```py
num_apples = max(5, 9) + 1
side_of_square = pow(area_of_square, 0.5)
```
