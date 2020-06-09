#!/usr/bin/env python3
"""
Given an integer, create a function that returns the next prime.
If the number is prime, return the number itself.

Examples

next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"


# def next_prime(number):
#     if (number % number == 0) and (number / 1 == number):
#         return(number)

import sympy


def main():
    """ Main entry point of the app """
    print(sympy.isprime(11))


if __name__ == "__main__":
    main()
