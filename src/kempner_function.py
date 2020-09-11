#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"


def factorial(n):
    number = 0
    for i, n in enumerate(n):
        number = i*n
    return number



def kempner(n):
  if (n > 0):
    result = n + kempner(n - 1)
    print(n)
  else:
    result = 0
  return result
  


def main():
  factorial(5)


if __name__ == "__main__":
    main()