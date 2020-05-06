#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"


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
    again = True
    while again:

        number = input('Enter an integer:')
        fizzbuzz(int(number))
        again = input('Again? y/n')
        if again == 'y':
            again = True
        elif again == 'n':
            again = False
        else:
            continue
    """
    put in a nested while clause here
    """



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()