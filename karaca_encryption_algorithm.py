#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def encrypt(message=None):
    """
    :param message:
    :return:
    """
    response = ""
    vowel_mapping = {'a': 'O',
                     'e': '1',
                     'o': '2',
                     'u': '3'}
    final_append = ['a', 'c', 'a']

    lower_case = message.lower()
    reverse_order = list(reversed(lower_case))
    vowel_replace = reverse_order.copy()
    for index, letter in enumerate(vowel_replace):
        if letter in vowel_mapping.keys():
            vowel_replace[index] = vowel_mapping[letter]
    append_step = vowel_replace + final_append
    return response.join(append_step)


def main():
    """
    lorum ipsum
    """
    while True:
        text = input('Enter word to encrypt:')
        print(encrypt(text))

        while True:
            again = input('Again? y/n')
            if again in ('y', 'n'):
                break
            print('Invalid Input')
        if again == 'y':
            continue
        sys.exit('Goodbye')


if __name__ == "__main__":
    main()
