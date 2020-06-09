#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"


def consecutive_combo(list_1, list_2):
    """
    Function Docstring
    """
    combined_list = (list_1 + list_2)
    combined_list.sort()
    compare_list = list(range(min(combined_list), max(combined_list) + 1))
    return combined_list == compare_list


def consecutive_combo_optimum(lst1, lst2):
    lst3 = lst1 + lst2
    return max(lst3) - min(lst3) == len(lst3) - 1


def main():
    """
    Main entry point into the program
    """
    print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
    print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
    print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
    print(consecutive_combo([44, 46], [45]))

if __name__ == "__main__":
    main()
