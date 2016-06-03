"""Converts a word to Pig Latin."""

VOWELS = 'aeiouy'

word = input('Word? ')

if word[0] not in VOWELS:
    out_word = word[1:] + word[0] + 'ay'
else:
    out_word = word + 'yay'

print('{} in Pig Latin is {}'.format(word, out_word))
