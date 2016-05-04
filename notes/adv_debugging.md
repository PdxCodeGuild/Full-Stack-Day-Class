# Advanced Debugging
Use the following three ideas to help you debug issues in your code.

They might seem to make problems become longer and more complex, but **I cannot stress strongly enough** that these techniques will help.

## Be Aggressively Reductionist
Break every problem down into a hierarchy of _sub-problems_ until you're at a level where the solution exists.
Each of these little solutions should be _separate functions_ with explicit inputs and outputs.

* Solve inner-most sub-problems first
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
    initials = ''.join([name[0] for name in first_last])
    initials_list.append(initials)
  return initials_list

slice_initials_list_from_full_names(['Rachel Raccoon', 'Joe Plumber'])
```

Instead, work on the "item-level" first, and use it on the "list-level"
```python
def slice_initials_from_full_name(full_name):
  first_last = full_name.split()
  return ''.join([name[0] for name in first_last])

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
* Double check that operators and library functions are behaving as you expect
* Double check _inputs_, not just outputs; you can't get the right answer if you're starting with junk
* Do this on an operation-by-operation basis
* Avoid long strings of operations; assign to variables after each step to print

Why doesn't this work?
```python
if
```

Break out each part and inspect individually
```python

```

## Test Isolated Pieces
Test each sub-problem or instruction in a sub-problem _in isolation_.

* Manually run and print out results of each sub-problem (easy, since each is a separate function)
* Use input "literals" to test; avoid having to type in setup

Instead of running your whole program
```python
input_str = input('Type a pig latin sentence: ')
print(convert_sentence_to_pig_latin(input_str))
```

Test each part on it's own first
```python
print(convert_word_to_pig_latin('cat'))
print(convert_word_to_pig_latin('apple'))
```

Then work up to testing the whole program
```python
print(convert_sentence_to_pig_latin('the cat jumps'))
```
