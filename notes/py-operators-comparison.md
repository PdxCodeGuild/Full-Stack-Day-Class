# Comparison Operators

All types have the concept of equality.
Two strings could have the same value.
Two booleans could have the same value.

Many types also have a concept of order.
Integers are ordered on the number line.
Strings can be in alphabetical order.
Not all types:
Booleans don't have an order, though.

Python gives us operators that let us check order and equality on types that support it.
They all _return booleans_.

The **equals operator** is `==`.

```py
3 == 3  #> True
'hi' == 'bye'  #> False
True == False  #> False
```

The **less-than operator** is `<`.

```py
5 > 9  #> False
'zebra' > 'aardvark'  #> True
```

The **greater-than operator** is `>`.

```py
5 < 9  #> True
'zebra' < 'aardvark'  #> False
```

The **not-equals operator** is `!=`.

```py
3 != 3  #> False
'hi' != 'bye'  #> True
True != False  #> True
```

There are also **greater-than-or-equal-to** (`>=`) and **less-than-or-equal-to** (`<=`) operators.

The rule-of-thumb from basic operators still applies:
avoid mixing types.
Equals and not-equals do allow you to, though.

```py
'hi' == 6  #> False
'hi' != 6  #> True
```

Most of the other operators don't.

```py
True > 5  #> throws TypeError
'hi' <= 2.2  #> throws TypeError
```

Remember, these are operators, just like `+`!
They just return booleans.
They can take in any expression and can be used as an expression.

```py
names_match = 'Bob' == 'Al'
names_match  #> False
num = 4
is_positive = abs(num) == num
is_positive  #> True
age = 32
print(age == 32)  # Prints True
```
