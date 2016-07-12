# Advanced Problem Solving

First, do a refresher of [basic problem solving](/notes/problem-solving-basic.md).

## Program Structure

At a high level, your program should follow this rubric of three big parts.

### 1. Setup

Set any constants that are fixed with every run.

### 2. Define Step Functions

Define a function for _each step_ of your problem.
Have them take explicit input arguments and output return values.
Use [stubbing](/notes/stubbing.md) if necessary.

### 3. Define Main Function

Define a function that is the main steps of your program.
It should delegate to all of the previously defined step functions.

_Immediately call your main_ function as the last statement in the program.

## Function Structure

Within each function, wether that be the main or a single step, you should follow this rubric.

### 1. Input

Process input from the arguments or the user.
Each function should _only do one_: take arguments or get `input()`.

The main function should delegate to a step function to actually get user input.
Other processing functions might need to do some prep on the input arguments to use them effectively.

### 2. Transform

Do work!
Solve your problem!
Transform your input values into output values.

Your code should look like piping values through transformation functions and storing them in intermediate variables.

Avoid printing here unless you're debugging.
It is confusing to keep track values if you're printing them out and they're changing.

### 3. Output

Print out or return labeled answers that came from your transform step.
Each function should _only do one_: call `print()` or `return` a value.

## Example

```py
def prompt_for_name():
    """Prompt the user for their name and return it as a string."""
    return input('What is your name? ')


def create_greeting(name):
    """From a string name, return a greeting to that name."""
    return 'Hi, {}!'.format(name)


def print_greeting(greeting):
    """Pretty print out a greeting centered in ====.

    ======Hi, David!======
    """
    print(greeting.center(20, '='))


def main():
    """Run greeting program.

    Prompt for name, then greet the user.
    """
    name = prompt_for_name()

    greeting = create_greeting(name)

    print_greeting(greeting)


main()
```
