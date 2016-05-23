# Python Style

There are lots of ways to write Python with identical meaning.
In general, whitespace is ignored.

```py
name       = input(   )
age=int(input()        )
next_year    =  (age +
    1   )
print (name   + " will be " +    str( next_year) + ' next year')
```

But if everyone wrote Python the same way, it'd be less thinking and confusing.

That's why places that write Python have a **style guide**.

Python as a whole language has a style guide called [PEP-8](https://www.python.org/dev/peps/pep-0008/).
Skim it and follow it.

```py
name = input()
age = int(input())
next_age = age + 1
print(name + ' will be ' + str(next_year) + ' next year')
```

We will be following PEP-8, but with a few more criteria:

* Strings will always be single quoted.
