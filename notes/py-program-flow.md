# Program Flow

The kinds of programs you write in Python are **imperative**:
you have to give the computer explicit instructions for how to do work.

Your `.py` file is a list of instructions.
Each line is a **statement** or one instruction.
Python runs files from top to bottom, _one line at a time_.

To communicate values between lines, you _have to save them in variables_ and reference them later.
You can only access values that you've stored _previously_, not in the future.
The list of previously-stored variables that you can access is called the **current scope**.
_All_ of your variable and function names must have values by the time the code runs.
If you try to access a variable you haven't given a value to yet, you get a `NameError`.

```py
miles = 300
miles_per_gallon = 30
cost_per_gallon_of_gas = 2.50

gallons_needed = miles / miles_per_gallon
road_trip_cost = gallons_needed * cost_per_gallon_of_gas
```

On each line, Python evaluates expressions from _left to right_ and _inner to outer_.
Inner expressions are turned into values and passed into their containing expressions.

```py
x = max(4 * 2, abs(-4 * 3))
#       - 1st  #> 4
#           - 2nd  #> 2
#       ----- 3rd  #> 8
#                  -- 4th  #> -4
#                       - 5th  #> 3
#                  ------ 6th  #> -12
#              ----------- 7th  #> 12
#   ----------------------- 8th  #> 12
y = x / (2 + x)
#   - 1st  #> 12
#        - 2nd  #> 2
#            - 3rd  #> 12
#        ----- 4th  #> 14
#   ----------- 5th  #> 1.167
```

Remember, **all expressions are equivalent**.
Any can be used in the slot for any other one.

* Literal specifies its own values
* Variable refers to the value within
* Operator results in its return value
* Function call results in its return value
