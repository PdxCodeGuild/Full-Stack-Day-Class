# Practice: Credit Card

Save your solution as `practice/credit-card.py`.

Write a function which returns whether a string containing a credit card number is valid as a boolean.
Write as many sub-functions as necessary to solve the problem.
Write doctests for each function.

Steps to validate a credit card number:

1.  Slice off the last digit.
    That is the **check digit**.

1.  Reverse the digits.

1.  Multiply the even-indexed reversed digits by two.

1.  Subtract nine from numbers over nine.

1.  Sum all subtracted values.

1.  Take the 1s digit of that sum.

1.  If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
1. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
1. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
1. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
1. 85
1. 5
1. True
