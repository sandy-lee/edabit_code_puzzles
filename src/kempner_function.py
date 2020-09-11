#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"


def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


def kempner(n):
    if factorial(n) / n == 0:
        return n
    else:
        return kempner(n-1)


# def kempner(n):
#     divisor = n
#     if factorial(n) / divisor == 0:
#         return ("it works!!")
#     else:
#         return("it sucks")


def main():
    print(kempner(6))


if __name__ == "__main__":
    main()