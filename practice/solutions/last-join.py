"""Rewrites a list of words, joining by commas and "and" resulting in proper
English.
"""
input_str = input('Words? ')
input_list = input_str.split()

joiner = ', '
pair_joiner = ' and '
last_joiner = ', and '

if len(input_list) <= 1:
    joined_str = input_list[0]
elif len(input_list) <= 2:
    joined_str = pair_joiner.join(input_list)
else:
    all_but_last_input = input_list[:-1]
    last_input = input_list[-1]
    joined_str = joiner.join(all_but_last_input) + last_joiner + last_input

print('{} words: {}'.format(len(input_list), joined_str))
