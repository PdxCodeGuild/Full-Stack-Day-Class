"""Asks for a name and age, then greets the user with their age next year."""
# 1. Setup
# No setup for this problem.

# 2. Input
print('What is your name?')
name = input()
print('What is your age?')
# input() returns only strings, but my age is best thought # about as a number,
# so I'll cast it to an int.
age = int(input())

# 3. Transform
# Let me figure out all of my outputs.
next_year_age = age + 1
greeting = 'So nice to meet you, ' + name + '!'
next_year_reminder = 'Next year, you will be ' + str(next_year_age) + '!'

# 4. Output
print(greeting)
print(next_year_reminder)
