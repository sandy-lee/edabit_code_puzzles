#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def fizzbuzz(number=0):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)


def main():
    """ Main entry point of the app """
    while True:

        while True:
            number = input('Enter a number:')
            if number.isnumeric():
                break
            else:
                print("Invalid Input")
        fizzbuzz(int(number))
        while True:
            answer = input('Again? y/n')
            if answer in ('y', 'n'):
                break
            print("Invalid input")
        if answer == 'y':
            continue
        else:
            sys.exit("Goodbye")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()