# Interfaces and Scope

Functions have to be able to define **interfaces** or **contracts**.
One person can write the function and a different person can use the function _without knowing how it's written_.

A lot of practical things fall out of the requirement that the function _caller_ and _writer_ can't interfere with each other.

Let's say I was told to write a function to convert inches to miles.

```py
def convert_inches_to_miles(inches):
    feet = inches / 12
    miles = feet / 5280
    return miles
```

But what if the person who was calling the function also had a variable named `feet`?
Would jumping up and running the function would mess up all their hard work?!

```py
def convert_inches_to_miles(inches):
    feet = inches / 12
    miles = feet / 5280
    return miles

feet = 7
miles_to_mars = convert_inches_to_miles(50000)
print(feet)
print(miles)
```

_No_. Python ensures that does not happen through **scope**.

Whenever a function is run, all of the variables assigned within it **shadow** any variables in the rest of the program.

So it's as if we wrote

```py
def convert_inches_to_miles(inches):
    feet_inner = inches / 12
    miles = feet_inner / 5280
    return miles

feet = 7
miles_to_mars = convert_inches_to_miles(50000)
print(feet)
print(miles)
```

and all of the variables in the function that would have been overwritten are now different.

In fact, all variables inside the function actually _don't exist_ outside of the function.
The following `NameError`s

```py
def greet(name):
    greeting = 'Hello, ' + name

greet('David')
print(greeting)  # Throws NameError
```
