# Testing
You've been writing code by breaking your problems down into steps, putting each step in a function, then calling that function in isolation, printing the result, and manually checking if the answer is correct.

Let's get the computer to check this for you!
You can write **test functions**, functions that test the proper working of other ones.

Tests should run the function they want to test with some _explicit inputs_ and **assert** that the return value matches an _explicit expected output_.

```python
def convert_feet_to_miles(feet):
    return feet / 5280

def test_convert_feet_to_miles():
    found = convert_feet_to_miles(5280)
    expected = 1
    assert found == expected
```
