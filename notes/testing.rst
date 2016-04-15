Testing
=======

You've been writing code by breaking your problems down into steps, putting each step in a function, then calling that function in isolation, printing the result, and manually checking if the answer is correct.

Let's get the computer to check this for you!
You can write **test functions**, functions that test the proper working of other ones.

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

## Why?
Why write test code?
* Rigor -- Python checks that output is correct, perfectly, every time
* Speed -- Python can compare outputs faster than you can
* Completeness -- Instead of just having one print statement for the most recent thing you've been testing, continually test all your work
* Regressions -- Change old code and test that it didn't break any old things that were working

**Test even your simple code.**
The simpler a function is, the easier it is to test.

## Testing Framework
We could write out all of these test functions and run them manually like we did above.
_But don't._
Python provides you with a **testing framework** that automatically discovers and runs all your tests for you.
It lives in the `unittest` module and uses classes for structure.

To use it:
1. Prepare the code **under test** (being tested) as a module.
Put the "main" parts in `if __name__ == '__main__':`.
1. Create a parallel test module with the same name, suffixed with `_test`.
1. In that test module, import `unittest` and make any number of classes that start with `Test` to group your tests.
1. In those classes write your actual test functions.
They will use your imported code under test.

E.g. If your code under test is in `converter.py`
```python
def convert_feet_to_miles(feet):
    return feet / 5280

if __name__ == '__main__':
    feet = 9000
    miles = convert_feet_to_miles(feet)
    print('{} feet is {} miles!'.format(feet, miles))
```

Then in `converter_test.py` put
```python
import unittest
import converter

class ConverterTest(unittest.TestCase):
    def test_convert_feet_to_miles():
        found = convert_feet_to_miles(5280)
        expected = 1
        assert found == expected

if __name__ == '__main__':
    unittest.run()
```
