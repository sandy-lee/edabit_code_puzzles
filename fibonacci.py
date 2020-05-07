#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sandy Lee"
__version__ = "0.1.0"
__license__ = "MIT"

import timeit
my_code = '''
def fibonacci():
    fib_series = [0, 1]
    for index, value in enumerate(fib_series):
        fib_value = value + fib_series[(index + 1)]
        if fib_value > 255:
            break
        else:
            fib_series.append(fib_value)
    return fib_series
'''

terse_code = '''
def fibonacci():
    fib = [0,1]
    while fib[-1] < 255:
        fib.append(fib[-2] + fib[-1])
    # the first fib number bigger then 255 always added, so remove it
    return fib[:-1]
'''

def main():
    """ Main entry point of the app """
    my_code_time = round(timeit.timeit(stmt=my_code, number=1000000), 5)
    terse_code_time = round(timeit.timeit(stmt=terse_code, number=1000000), 5)
    print(f'Execution time for my code:       {my_code_time}s.')
    print(f'Execution time for terse code:    {terse_code_time}s.')
    print(f'The difference is:                {round(my_code_time - terse_code_time,5)}s')
    if my_code_time < terse_code_time:
        print('My code is quicker.')
    else:
        print('Terse code is quicker.')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
