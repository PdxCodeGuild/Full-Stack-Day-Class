"""Calculate change.

Calculate the smallest number of coins needed to represent an amount of cents
less than 100.
"""

print('Amount of change to calculate in cents? (< 100) ')
amount_cents = int(input())

cents_left = amount_cents
quarters = cents_left // 25
cents_left = cents_left - quarters * 25
dimes = cents_left // 10
cents_left = cents_left - dimes * 10
nickles = cents_left // 5
cents_left = cents_left - nickles * 5
pennies = cents_left

print(str(quarters) + ' quarters')
print(str(dimes) + ' dimes')
print(str(nickles) + ' nickles')
print(str(pennies) + ' pennies')
