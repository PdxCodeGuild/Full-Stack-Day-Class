# Advanced Problem Solving
Use the following three ideas to help you solve problems.

They seem to make problems become longer and more complex, but **I cannot stress strongly enough** that these techniques will help.

## Be Aggressively Reductionist
Break every problem down into a hierarchy of _sub-problems_ until you're at a level where the solution exists.

* Solve inner-most sub-problems first
* Make every sub-problem a function
* Work step-by-step up hierarchies
* Use your previous solutions as you work up

E.g. Solve the "item-level" problem before the "list-level" problem.
Solve how to pick out the year from a single date and put that in a function.
Only then solve converting a list of dates to a list of years using the function you just wrote.

## Double-Check Mental Model
Data is invisible unless you print it.
_Print out_ the result of each individual operation to double check it is returning what you expect.

* Ensure you can print out your data in a readable format; write a function to do so if necessary
* Double check the operators and library functions are behaving as you expect
* Do this on an operation-by-operation basis
* Avoid long strings of operations; assign to variables after each step to print

## Test Isolated Pieces
Test each sub-problem or instruction in a sub-problem _in isolation_.

* Manually run and print out results of each sub-problem (easy since a function)
* Copy and paste the exact input you want
