"""Asks the user for a Blackjack pair, scores it, and gives hitting advice."""
card_1 = input('First card value? ')
card_2 = input('Second card value? ')

if card_1 == 'A':
    value_1 = 1
elif card_1 == '10' or card_1 == 'J' or card_1 == 'Q' or card_1 == 'K':
    value_1 = 10
else:
    value_1 = int(card_1)


if card_2 == 'A':
    value_2 = 1
elif card_2 == '10' or card_2 == 'J' or card_2 == 'Q' or card_2 == 'K':
    value_2 = 10
else:
    value_2 = int(card_2)

if card_1 == 'A' and value_2 + 11 <= 21:
    value_1 = 11
if card_2 == 'A' and value_1 + 11 <= 21:
    value_2 = 11

value_total = value_1 + value_2

if value_total < 17:
    response = 'Hit'
elif value_total == 21:
    repsone = 'Blackjack!'
else:
    response = 'Stay'

print(str(value_total) + ' ' + repsone)
