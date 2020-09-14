#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import math

divisor = 0
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial(n-1)

# def iterative_factorial(n):
#     result = 1
#     for i in range(2,n+1):
#         result *= i
#     return result


# def kempner(n):
#     global divisor
#     if math.factorial(n) % divisor == 0:
#         return n
#     elif math.factorial(n) % divisor > 0:
#         return kempner(n-1)

def kempner(n):
    for i in range(1, n):
        if math.factorial(n) % divisor == 0:
            return i
        elif math.factorial(n) % divisor > 0:
            return kempner(n-1)



def main():
    global divisor
    number_to_check = 6
    divisor = 6
    print(kempner(number_to_check))


if __name__ == "__main__":
    main()

"""
TODO:
[] step through variable in debug mode to make sure global variable is working
[] fix non-recusive way of doing factorials
[] put in place very basic ui and input validation
"""


