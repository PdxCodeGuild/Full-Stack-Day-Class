# Practice: ATM
Write a program that functions as a simple ATM for a single account.

An account will be a class: it will have a field for the balance.

Write functions for the account class that:
* Deposit to the account.
* Check if enough funds for a withdrawal.
* Withdraw an allowed amount.
* Calculate 0.5% interest on the account.

Implement a user interface that lets a user pick each of those actions and updates the account.
After each action it will print the balance.

## Advanced
* Save the account balance to a file after each operation.
Read that balance on startup so the balance persists across program starts.
* Add to each account class an account ID number.
* Allow the user to open more than one account.
Let them perform all of the above operations by account number.
