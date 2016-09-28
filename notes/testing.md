# Automated Testing

You've been writing code by breaking your problems down into steps, putting each step in a function, then calling that function in isolation, printing the result, and manually checking if the answer is correct.

Let's get the computer to check this for you!
You can write **test functions**, functions that test the proper working of your **feature functions**.

Referring to having to write tests, an old coworker of mine said:

> Writing correct code is so hard, you have to try twice.

Tests should run the function they want to test with some _explicit inputs_ and **assert** that the return value matches an _explicit expected output_.
The assert will raise an exception if the evaluation is not true.

```python
def convert_feet_to_miles(feet):
    return feet / 5280

def test_convert_feet_to_miles():
    found = convert_feet_to_miles(5280)
    expected = 1
    assert found == expected

test_convert_feet_to_miles()
```

## Why

Current best practices puts testing as one of the major enforcers of software quality.
Why write test code?

* Rigor -- Python checks that output is correct, perfectly, every time
* Speed -- Python can compare outputs faster than you can
* Completeness -- Instead of just having one print statement for the most recent thing you've been testing, continually test all your work
* Regressions -- Change old code and test that it didn't break any old things that were working
* Understanding -- Code that is easy to test tends to be simple to understand and will increase the quality of the rest of your code

Test even your simple code.
**The simpler a function is, the easier it is to test.**

## Running Tests

We could write out all of these test functions and run them manually like we did above.

But don't.

Use a **testing framework** that automatically discovers and runs your tests for you.
