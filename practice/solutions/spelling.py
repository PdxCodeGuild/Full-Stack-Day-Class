"""Check that a word follows "I before E except after C"."""
word = input('Word? ')

ie_index = word.find('ie')
if ie_index > 0:
    follows = word[ie_index - 1] != 'c'
else:
    follows = True

print(follows)
