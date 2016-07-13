"""Validate a credit card number."""


def prompt_for_digits():
    """Prompt a user to enter a credit card number.

    Spaces are ignored in the number.
    Returns the number as a list of int digits.
    """
    card_num_str = input('Enter a credit card number: ').replace(' ', '')
    return convert_digit_str_to_list(card_num_str)


def convert_digit_str_to_list(digit_str):
    """Convert a string of single digits to a list of ints.

    >>> convert_digit_str_to_list('1234')
    [1, 2, 3, 4]
    """
    return [int(d) for d in digit_str]


def get_check_digit(digits):
    """Return the check digit / last digit off a list of digits.

    >>> get_check_digit([1, 2, 3])
    3
    """
    return digits[-1]


def get_info_digits(digits):
    """Return the information-bearing digits from a full credit card number.

    Basically, excludes the last digit, which is the check digit.

    >>> get_info_digits([1, 2, 3])
    [1, 2]
    """
    return digits[:-1]


def double_alternating_digits(digits):
    """Double every other digit in a list of them.

    Doubles the first digit.

    >>> double_alternating_digits([1, 1, 2, 2])
    [2, 1, 4, 2]
    """
    return [
        d * 2 if i % 2 == 0 else d
        for i, d
        in enumerate(digits)
    ]


def wrap_over_9_digits(digits):
    """Return a list with any elements greater than 9 reduced by 9.

    >>> wrap_over_9_digits([8, 9, 10, 11])
    [8, 9, 1, 2]
    """
    return [d - 9 if d > 9 else d for d in digits]


def get_ones_digit(num):
    """Return the ones digit of a number.

    >>> get_ones_digit(98)
    8
    """
    return num % 10


def validate_digits(digits):
    """Return if a list of digits that form a credit card number is valid.

    >>> validate_digits([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
    True
    >>> validate_digits([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 0])
    False
    """
    check_digit = get_check_digit(digits)
    info_digits = get_info_digits(digits)

    reversed_info_digits = list(reversed(info_digits))
    doubled_info_digits = double_alternating_digits(reversed_info_digits)
    wrapped_info_digits = wrap_over_9_digits(doubled_info_digits)
    found_check_sum = sum(wrapped_info_digits)
    found_check_digit = get_ones_digit(found_check_sum)

    return found_check_digit == check_digit


def main():
    """Prompt for a credit card number, validate it, and print out if it's
    valid.
    """
    digits = prompt_for_digits()
    is_valid = validate_digits(digits)
    print(is_valid)


main()
