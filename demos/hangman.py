def calculate_hidden_letters(word, guessed_letters):
    return set(word) - set(guessed_letters)


def replace_letters_with_slots(word, hidden_letters):
    word_with_slots = str(word)
    for letter in hidden_letters:
        word_with_slots = word_with_slots.replace(letter, '_')
    return word_with_slots


def calculate_wrong_letters(word, guessed_letters):
    return set(guessed_letters) - set(word)


secret_word = 'puppy'.lower()
guessed_letters = set()
max_wrong_guesses = 6


allow_guessing = True
while allow_guessing:
    hidden_letters = calculate_hidden_letters(secret_word, guessed_letters)
    wrong_letters = calculate_wrong_letters(secret_word, guessed_letters)

    word_is_revealed = len(hidden_letters) < 1
    guesses_remaining = max_wrong_guesses - len(wrong_letters)

    word_with_slots = replace_letters_with_slots(secret_word, guessed_letters)
    formatted_wrong_letters = ', '.join(wrong_letters)

    print('Secret Word:', word_with_slots)
    print('Wrong:', formatted_wrong_letters)
    print('Guesses Left:', guesses_remaining)

    if guesses_remaining > 0 and not word_is_revealed:
        new_guess = input('Enter a letter > ').lower()[0]
        guessed_letters = guessed_letters | {new_guess}
    else:
        allow_guessing = False

print('The secret word was', secret_word)
