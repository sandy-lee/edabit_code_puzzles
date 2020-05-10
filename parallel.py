#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def get_value(value_name):
    """Get values and validate"""
    while True:
        try:
            value = int(input(f'Enter {value_name}:'))
        except ValueError as error:
            print(f'{error} \nInteger Values Only')
        else:
            return value


def parallel(line_one, line_two):
    """Assess whether lines are parallel"""
    if line_one[:2] == line_two[:2]:
        print("Lines are parallel")
    else:
        print("Line are not parallel")


def main():
    """ Main entry point of the app """
    while True:
        line_one, line_two = [0, 0, 0], [0, 0, 0]
        line_one[0] = get_value('line one coefficient a')
        line_one[1] = get_value('line one coefficient b')
        line_one[2] = get_value('line one coefficient c')
        line_two[0] = get_value('line two coefficient a')
        line_two[1] = get_value('line two coefficient b')
        line_two[2] = get_value('line two coefficient c')
        parallel(line_one, line_two)
        while True:
            more = input('Again? y/n')
            if more in ('y', 'n'):
                break
            print('Invalid Input')
            continue
        if more == 'y':
            continue
        sys.exit('Goodbye')


if __name__ == "__main__":
    main()
