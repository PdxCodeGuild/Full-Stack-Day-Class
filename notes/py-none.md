# None

Python has a special single value called **none**.
It is a value that represents the _absence of a value_.
It's literal is uppercase none.

```py
None
```

**Avoid using none.**
Basically any time you think about None, you could probably be using a better "empty value".

* Empty list
* Empty string
* False

## Existing Code

You'll see it used in a few different situations:

Functions that don't explicitly return a value implicitly return none.

```py
def print_hi():
    print('hi')

x = print_hi()
x  #> None
```

Default function arguments are sometimes set to none to indicate they're unused.

```py
def print_hi(name=None):
    if name is None:
        print('Hi!')
    else:
        print('Hi, ' + name + '!')
```

## Returning None

Avoid returning `None` from lookup or searching functions.
Instead think about returning the empty list or throwing an exception.
Whenever you write a function that could return `None`, you have to specially handle that case in all of the code that uses it!

```py
def find_all_students_in_class(class_name):
    """Returns a list of all students in a class or None."""
    ...


class_students = find_all_students_in_class('dayclass')
if class_students is not None:
    class_last_names = [student.split()[-1] for student in class_students]
else:
    class_last_names = None
```

If you return the empty list, then all processing is streamlined.

```py
def find_all_students_in_class(class_name):
    """Returns a list of all students in a class."""
    ...


class_students = find_all_students_in_class('dayclass')
class_last_names = [student.split()[-1] for student in class_students]
```
