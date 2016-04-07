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

Don't make the "list-level" version of your problem the most basic version
```python
def slice_initials_list_from_full_names(full_names):
  initials_list = []
  for full_name in full_names:
    first_last = full_name.split()
    initials = first_last[0][0] + first_last[1][0]
    initials_list.append(initials)
  return initials_list

slice_initials_list_from_full_names(['Rachel Raccoon', 'Joe Plumber'])
```

Instead, work on the "item-level" first, and use it on the "list-level"
```python
def slice_initials_from_full_name(full_name):
  first_last = full_name.split()
  return first_last[0][0] + first_last[1][0]

def slice_initials_list_from_full_names(full_names):
  return [
    slice_initials_from_full_name(full_name)
    for full_name
    in full_names
  ]

slice_initials_list_from_full_names(['Rachel Raccoon', 'Joe Plumber'])
```

## Double-Check Mental Model
Data is invisible unless you print it.
_Print out_ the result of each individual operation to double check it is returning what you expect.

* Ensure you can print out your data in a readable format; write a function to do so if necessary
* Double check the operators and library functions are behaving as you expect
* Do this on an operation-by-operation basis
* Avoid long strings of operations; assign to variables after each step to print

Why doesn't this work?
```python
def 
```

## Test Isolated Pieces
Test each sub-problem or instruction in a sub-problem _in isolation_.

* Manually run and print out results of each sub-problem (easy since a function)
* Copy and paste the exact input you want
