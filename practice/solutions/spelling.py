"""Check that a word follows "I before E except after C"."""
word = input('Word? ')

if 'ie' in word:
    index = word.find('ie')
    if index > 0:
        follows = word[index - 1] != 'c'
elif 'ei' in word:
    index = word.find('ei')
    if index > 0:
        follows = word[index - 1] == 'c'
else:
    follows = True

if follows:
    follows_str = 'does'
else:
    follows_str = "doesn't"

print('{} {} follow the rule'.format(word, follows_str))
