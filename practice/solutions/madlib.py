"""Ask a user for madlib words and then fill in and print out the completed
madlib.
"""
print('A adj, please:')
adj1 = input()
print('A noun, please:')
noun1 = input()
print('Another noun, please')
noun2 = input()

madlib = 'A ' + adj1 + ' ' + noun1 + ' jumps over the ' + noun2 + '!'

print(madlib)
