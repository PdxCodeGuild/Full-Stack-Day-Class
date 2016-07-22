# Practice: ATM Interface

Save your solution in a directory in `practice/` named `atm-interface`.

Write a program that functions as a simple ATM for two accounts:

1. Checking account
1. Savings account

An account will be a class named `Account` in a module named `account`: it will have fields for the balance and interest rate.
A newly-instantiated account will have zero balance.

Write functions in the account class that:

* `get_funds()` Return funds available.
* `deposit(amount)` Deposit to the account.
* `check_withdrawal(amount)` Check if enough funds for a withdrawal.
* `withdraw(amount)` Withdraw an allowed amount; raise a `ValueError` if not enough funds.
* `calc_interest()` Calculate and return 0.1% interest on the current account value.

Implement a user interface that lets a user pick each of those actions for a given account and updates the account.
After each action it will print the balance.

I've already written out [some test code](/practice/atm/account_test.py) that will check that your `Account` class behaves as expected.
Save it as `account_test.py` in your solution directory.
These tests should all pass for your `Account` implementation.
Either run `py.test` from the `atm` directory, or setup a PyCharm test Run Configuration.

You should still write doctests for your functions that

## Advanced

With each advanced feature, either add additional doctests for

*   Add a function called `get_standing` have it return a bool with whether the account has less than $1000 in it.

*   Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.

*   Save the account balance to a file after each operation.
    Read that balance on startup so the balance persists across program starts.

*   Add to each account class an account ID number.

*   Allow the user to open more than one account.
    Let them perform all of the above operations by account number.
