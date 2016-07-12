# Functions

We want to write our own functions.
Why?

* Structure -- label steps in your code with meaning
* Reuse -- define once, run many, fix once
* **Interface** -- use without knowing implementation, defines a _contract_

Before you can use a function, you have to **define** it.
First comes `def`, then the **name** of the function, then a list of **input arguments** in `()`, a `:`, then an indented block of instructions.
That block can have a **return statement**, which specifies what value the function should _output_.

```py
def calc_road_trip_time(miles, mph):
    return miles / mph
```

Then, anywhere later in that code you can call the function you made!

```py
travel_time_1 = calc_road_trip_time(100, 50)
travel_time_2 = calc_road_trip_time(130, 55)
```

Each call to your function causes the Python to jump up to the body of the function and run it, filling in the values at the call site _in-order_ into the argument variables in the function definition.
Then once the function is done, the return value is placed back at the call site.

So for the above example, it's as if

```py
miles = 100
mph = 50
travel_time_1 = miles / mph
miles = 130
mph = 55
travel_time_2 = miles / mph
```

This allows you to **parameterize** the function and have it work any values!

**Only take inputs via arguments and return an output via a return value.**
Think about your problem in terms of little steps that have inputs and outputs.

Functions don't have to take in any arguments if there's nothing in the program that would change their output.
You've seen `input()` as an example.

```py
def gettysburg_address():
    return 'Four score and seven...'
```

Remember, defining _does not run the function!_
You still have to call with parentheses after its name to make it go.
