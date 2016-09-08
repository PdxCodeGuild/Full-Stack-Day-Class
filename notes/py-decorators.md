# Decorators

Often, you might want to add validation or verification to function input and output.
Until now, you'd write a "main" function that explicitly calls validator and then your verb function.

```py
def validate_age(age):
    if age < 0:
        raise ValueError('impossible age: {!r}'.format(age))


def say_happy_birthday(age):
    return "You're {} years old!".format(age)


def validate_and_say_happy_birthday(age):
    validate_age(age)
    say_happy_birthday(age)


validate_and_say_happy_birthday(9)  #> "You're 9 years old!"
```

Since each main function is just calling `validate_age()` then a verb function, you could have a Python function that programmatically generates the main!

```py
def make_validate_age(verb_func):
    def main_func(age):
        validate_age(age)
        verb_func(age)
    return main_func


validate_and_say_happy_birthday = make_age_validate_main(say_happy_birthday)

validate_and_say_happy_birthday(9)  #> "You're 9 years old!"
```

Remember, when you define a function, it's looking up the names of each function in the current scope.
Usually that scope is module level global.

```py
def add_two(x):
    return x + 2

do_mystery_math = add_two

def add_three(x):
    return do_mystery_math(x) + 1

add_three(5)  #> 8
```

But it could be a function!

```py
def outer(do_mystery_math):
    def add_three(x):
        return do_mystery_math(x) + 1
    return add_three(5)  #> 8

outer(add_two)  #> 8
```

Hopefully that makes the above code more scrutable.

Since this is such a common operation, Python has a feature called **decorators** to streamline those "main making functions".
Prefix your function definition with the at symbol `@` and the main making function name and Python will **wrap** your function for you.

```py
@make_validate_age
def say_happy_birthday(age):
    print("You're {} years old!".format(age))
```

That code is exactly equivalent to defining a hidden function and then calling the decorator function and saving the resulting "main" function as the original name:

```py
def __say_happy_birthday(age):
    print("You're {} years old!".format(age))


say_happy_birthday = make_validate_age(__say_happy_birthday)
```
