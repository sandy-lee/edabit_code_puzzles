#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def encrypt(message=None):
    cipher = [message.lower()]
    step_1 = reversed(cipher)
    return step_1


def main():
    text = encrypt("test")
    print(list(text))

    # TODO: how to make it print out a reverse list as a sting from a generator
    # while True:
    #     text = input('Enter word to encrypt:')
    #     print(list(encrypt(text)))
    #
    #     while True:
    #         again = input('Again? y/n')
    #         if again in ('y', 'n'):
    #             break
    #         else:
    #             print('Invalid Input')
    #     if again == 'y':
    #         continue
    #     sys.exit('Goodbye')


if __name__ == "__main__":
    main()
