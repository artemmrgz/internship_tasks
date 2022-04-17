import sys
from string import ascii_uppercase, ascii_lowercase, punctuation, digits


LENGTH = 14
NO_UPPER_LOWER = '- Password must contain \
                    both lowercase and uppercase characters'
NO_PUNCTUATION = f'- Password must contain \
                     at least one punctuation character {punctuation}'
NO_DIGITS = '- Password must contain digits'
TOO_SHORT = '- Password must be at least 14 characters long'
WEAK_PSW = 'Weak password:'
STRONG_PSW = 'Strong password'


def contains(required_chars, password):
    return any(char in required_chars for char in password)


def has_upper_lower(password):
    return contains(ascii_uppercase, password) and \
           contains(ascii_lowercase, password)


def has_digit(password):
    return contains(digits, password)


def has_punctuation(password):
    return contains(punctuation, password)


def has_proper_length(password):
    return len(password) >= LENGTH


def checker(password):
    criteria = [(has_upper_lower, NO_UPPER_LOWER),
                (has_punctuation, NO_PUNCTUATION),
                (has_digit, NO_DIGITS),
                (has_proper_length, TOO_SHORT)]
    errors = [message for func, message in criteria if not func(password)]
    return errors


def main():
    try:
        password = sys.argv[1]
        errors = checker(password)
        if errors:
            print(WEAK_PSW)
            print('\n'.join(errors))
        else:
            print(STRONG_PSW)
    except IndexError:
        print('There is no password to check')


if __name__ == '__main__':
    main()
