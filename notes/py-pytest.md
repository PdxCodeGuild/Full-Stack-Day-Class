# PyTest

Pytest is the testing framework we'll be using to run tests.
It is not part of the standard library, but you can easily install it using `pip install pytest`.

## Structuring Test Code

To test your code, it has to be put in a module, and you have to have separate testing modules.

Follow these instructions:

1.  Prepare the feature code [as a module](/notes/py-modules-create.md):
    Put the "main" parts in `if __name__ == '__main__':` so they won't run when imported.

1.  Create a parallel module _for the tests_ in the same directory with the same name, prefixed with `test_`.

1.  In that test module, write your actual test functions with assertions.
You will _import_ your feature code and use the dot operator to access the feature functions to test.

E.g. If your feature code is in `converter.py`

```python
def convert_feet_to_miles(feet):
    return feet / 5280

if __name__ == '__main__':
    feet = 9000
    miles = convert_feet_to_miles(feet)
    print('{} feet is {} miles!'.format(feet, miles))
```

Then in `test_converter.py` in the same directory put

```python
import converter

def test_convert_feet_to_miles():
    found = converter.convert_feet_to_miles(5280)
    expected = 1
    assert found == expected
```

Pytest also lets you group your test functions into classes for organization.

```python
import converter

class TestFeetConversion:
    def test_convert_feet_to_miles():
        found = converter.convert_feet_to_miles(5280)
        expected = 1
        assert found == expected
```

## Running Tests

You can run tests from the command line by using the `py.test` command:

```bash
py.test test_converter.py
```

You can also get PyCharm to run Pytest tests by:

1. Making a new "Python tests" / "py.test" run configuration
1. Put your test Python file name as the "target", e.g. `test_converter.py`
1. Set the working directory to the parent directory of the test file

## Test Naming Conventions

For Pytest to automatically find all of your test functions, they have to be named according to a pattern:

1. Test modules must begin with `test_` or end with `_test`
1. Test class names must begin with `Test`
1. Test function names must begin with `test_`

Might as well make them all begin with "test".
