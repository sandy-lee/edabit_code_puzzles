#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import math 

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial(n-1)


def kempner(n):
    if math.factorial(n) / n == 0:
        print(math.factorial(n))
        print(n)
        return n
    else:
        return kempner(n-1)


def main():
    print(kempner(4))


if __name__ == "__main__":
    main()