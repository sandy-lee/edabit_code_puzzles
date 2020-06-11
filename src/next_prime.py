#!/usr/bin/env python3.8

import math

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


def is_prime(n):
    divisor = 2
    wall = math.sqrt(n)
    while divisor <= wall:
        if n % divisor == 0:
            return False
        divisor += 1
    else:
        return True


def next_prime(n):
    next_prime = False
    if is_prime(n):
        return(n)
    else:
        while next_prime is False:
            next_prime = is_prime(n)
            n += 1
    return(n-1)


def main():
    """ Main entry point of the app """
    print(next_prime(12))
    print(next_prime(24))
    print(next_prime(11))


"""
TODO: optimise isprime(n) as per:
https://en.wikipedia.org/wiki/Primality_test
TODO: add interface to accept any prime
TODO: error checking for 0, 1 or negative values into isprime(n)
"""


if __name__ == "__main__":
    main()
