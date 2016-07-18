"""Converts between various programming case styles."""
import re

SNAKE_CASE = 'snake'
CAMEL_CASE = 'camel'
CONST_CASE = 'const'
KEBAB_CASE = 'kebab'
CASES = [SNAKE_CASE, CAMEL_CASE, CONST_CASE, KEBAB_CASE]


def prompt_for_var_name():
    """Prompt the user to input a variable name."""
    return input('Variable name? ')


def detect_case(var_name):
    """Detect the case of a variable name and return it.

    >>> detect_case('snake_case')
    'snake'
    >>> detect_case('CamelCase')
    'camel'
    >>> detect_case('kebab-case')
    'kebab'
    >>> detect_case('CONST_CASE')
    'const'
    """
    if '_' in var_name:
        if var_name.isupper():
            return CONST_CASE
        else:
            return SNAKE_CASE
    elif '-' in var_name:
        return KEBAB_CASE
    else:
        return CAMEL_CASE


def normalize_var_name(var_name):
    """
    >>> normalize_var_name('snake_case')
    ['snake', 'case']
    """
    var_case = detect_case(var_name)
    if var_case == SNAKE_CASE:
        return normalize_snake(var_name)
    elif var_case == CAMEL_CASE:
        return normalize_camel(var_name)
    elif var_case == KEBAB_CASE:
        return normalize_kebab(var_name)
    elif var_case == CONST_CASE:
        return normalize_const(var_name)
    else:
        raise ValueError('unknown case {}'.format(var_case))


def normalize_snake(var_name):
    """
    >>> normalize_snake('snake_case')
    ['snake', 'case']
    """
    return var_name.split('_')


def normalize_camel(var_name):
    """
    >>> normalize_camel('CamelCase')
    ['camel', 'case']
    """
    return [word.lower() for word in re.split(r'([A-Z][a-z]*)', var_name) if len(word) > 0]


def normalize_kebab(var_name):
    """
    >>> normalize_kebab('kebab-case')
    ['kebab', 'case']
    """
    return var_name.split('-')


def normalize_const(var_name):
    """
    >>> normalize_const('CONST_CASE')
    ['const', 'case']
    """
    return var_name.lower().split('_')


def render_case(var_words, var_case):
    if var_case == SNAKE_CASE:
        return render_snake(var_words)
    elif var_case == CAMEL_CASE:
        return render_camel(var_words)
    elif var_case == KEBAB_CASE:
        return render_kebab(var_words)
    elif var_case == CONST_CASE:
        return render_const(var_words)
    else:
        raise ValueError('unknown case {}'.format(var_case))


def render_snake(var_words):
    """
    >>> render_snake(['snake', 'case'])
    'snake_case'
    """
    return '_'.join(var_words)


def render_camel(var_words):
    """
    >>> render_camel(['camel', 'case'])
    'CamelCase'
    """
    return ''.join([word.capitalize() for word in var_words])


def render_kebab(var_words):
    """
    >>> render_kebab(['kebab', 'case'])
    'kebab-case'
    """
    return '-'.join(var_words)


def render_const(var_words):
    """
    >>> render_const(['const', 'case'])
    'CONST_CASE'
    """
    return '_'.join(var_words).upper()


def main():
    """Runs main.

    Prompts for a variable name, detects its case, prints it out in all other cases.
    """
    var_name = prompt_for_var_name()
    var_words = normalize_var_name(var_name)
    for case in CASES:
        out_var_name = render_case(var_words, case)
        print(out_var_name)


if __name__ == '__main__':
    main()
