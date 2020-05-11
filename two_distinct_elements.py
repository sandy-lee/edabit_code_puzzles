#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"


def return_uniques(list):
    uniques = []
    for number in list:
        if list.count(number) == 1:
            uniques.append(number)
    return uniques


def main():
    print(return_uniques([1, 9, 8, 8, 7, 6, 1, 6]))

    print(return_uniques([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))

    print(return_uniques([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))


if __name__ == "__main__":
    main()
