#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

# import math

from math import factorial as f

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

def kempner(n, i=1, total=1):
    # return max(1, i-1) if total%n == 0 else kempner(n, i+1, total*i)
    if total % n == 0:
        return max(1, i-1)
    else:
        return kempner(n, i+1, total*i)

#why does this wind down after the condition is met and go down again?


# def kempner(n, i=1):
#     # return kempner(n, i +1) if f(i)%n else i
#     if f(i) % n:
#         return kempner(n, i+1)
#     else:
#         return i


def main():
    global divisor
    number_to_check = 10
    divisor = 10
    print(kempner(number_to_check))



if __name__ == "__main__":
    main()

"""
TODO:
[] step through variable in debug mode to make sure global variable is working
[] fix non-recusive way of doing factorials
[] put in place very basic ui and input validation
"""


