#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def parallel(line_one, line_two):
    if len(line_one) != 3:
        sys.exit("Error, wrong size list supplied for first line")
    elif len(line_two) != 3:
        sys.exit("Error, wrong size list supplied for second line")
    else:
        for element in line_one:
            if type(element) != int:
                sys.exit("Non-integer supplied for first line")
        for element in line_two:
            if type(element) != int:
                sys.exit("Non-integer supplied for second line")
    if line_one[:2] == line_two[:2]:
        print("Lines are parallel")
    else:
        print("Line are not parallel")
    return


def main():
    """ Main entry point of the app """
    line_one, line_two = [0, 0, 0], [0, 0, 0]
    while True:
        try:
            line_one[0] = int(input('Enter line one coefficient a:'))
        except:
            ValueError
            print("int only")
        try:
            line_one[1] = int(input('Enter line one coefficient b:'))
        except:
            ValueError
            print("int only")
        try:
            line_one[2] = int(input('Enter line one coefficient c:'))
        except:
            ValueError
            print("int only")
        try:
            line_two[0] = int(input('Enter line two coefficient a:'))
        except:
            ValueError
            print("int only")
        try:
            line_two[1] = int(input('Enter line two coefficient b:'))
        except:
            ValueError
            print("int only")
        try:
            line_two[2] = int(input('Enter line two coefficient c:'))
        except:
            ValueError
            print("int only")

    # TODO: look into error handling for data validation


    # parallel(line_one, line_two)
    # print(line_one[1:3])
    # print(line_two[1:3])



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()