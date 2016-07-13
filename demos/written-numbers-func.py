"""Convert a number in base-10 into a written out number in English."""


def prompt_for_number():
    """Prompt the user for a number in base-10 and return it as an int."""
    return int(input('A number between 0 and 99: '))


def get_tens_digit(num):
    """Return the tens digit of a number.

    The number must be less than 100.
    """
    return num // 10


def get_ones_digit(num):
    """Return the ones digit of a number."""
    return num % 10


def tens_digit_to_word(tens_digit):
    """From the tens digit, return the word representing that."""
    if tens_digit == 9:
        tens_word = 'ninety'
    elif tens_digit == 8:
        tens_word = 'eighty'
    elif tens_digit == 7:
        tens_word = 'seventy'
    elif tens_digit == 6:
        tens_word = 'sixty'
    elif tens_digit == 5:
        tens_word = 'fifty'
    elif tens_digit == 4:
        tens_word = 'forty'
    elif tens_digit == 3:
        tens_word = 'thirty'
    elif tens_digit == 2:
        tens_word = 'twenty'
    else:
        tens_word = ''
    return tens_word


def ones_digit_to_word(ones_digit):
    """From the ones digit, return the word representing that."""
    if ones_digit == 9:
        ones_word = 'nine'
    elif ones_digit == 8:
        ones_word = 'eight'
    elif ones_digit == 7:
        ones_word = 'seven'
    elif ones_digit == 6:
        ones_word = 'six'
    elif ones_digit == 5:
        ones_word = 'five'
    elif ones_digit == 4:
        ones_word = 'four'
    elif ones_digit == 3:
        ones_word = 'three'
    elif ones_digit == 2:
        ones_word = 'two'
    elif ones_digit == 1:
        ones_word = 'one'
    else:
        ones_word = 'zero'
    return ones_word


def assemble_word_regular(tens, ones, tens_word, ones_word):
    """Convert a regular number (<= 10 or >= 20) to words."""
    if ones == 0:
        return tens_word
    elif tens == 0:
        return ones_word
    else:
        return tens_word + '-' + ones_word


def assemble_words_irregular(ones, ones_word):
    """Convert an irregular number (> 10 and < 20) to words."""
    if ones == 1:
        output = 'eleven'
    elif ones == 2:
        output = 'twelve'
    elif ones == 3:
        output = 'thirteen'
    else:
        output = ones_word + 'teen'
    return output


def assemble_words(tens, ones, tens_word, ones_word):
    """Convert any number to words.

    Performs any irregular conversions.
    """
    if tens == 1:
        output = assemble_words_irregular(ones, ones_word)
    else:
        output = assemble_word_regular(tens, ones, tens_word, ones_word)
    return output


def main():
    """Convert a number in base-10 into a written out number in English.

    Ask for the number, find its digits, then assemble them into a compound
    English number, then print it out.
    """
    num = prompt_for_number()

    tens = get_tens_digit(num)
    ones = get_ones_digit(num)
    tens_word = tens_digit_to_word(tens)
    ones_word = ones_digit_to_word(ones)
    output = assemble_words(tens, ones, tens_word, ones_word)

    print(output)


main()
