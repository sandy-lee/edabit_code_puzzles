# edabit_code_puzzles

## FizzBuzz

Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5
Examples
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"
Notes
Try to be precise with how you spell things and where you put the capital letters.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

___
## Fibonacci Sequence
The Fibonacci Sequence is the sequence of numbers (Fibonacci Numbers) whose sum is the two preceding numbers (e.g. 0, 1, 1, 2, 3, etc). Using 0 and 1 as the starting values, create a function that returns a list containing all of the Fibonacci numbers less than 255.

Examples
On generating a Fibonacci number where input is the two preceding values starting from 0 and 1 [0, 1, ...].

0, 1 ➞ 1

1, 1 ➞ 2

1, 2 ➞ 3

Notes:
This function will take no parameters.
---

#Check If Lines Are Parallel
Given two lines, determine whether or not they are parallel.

Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ true
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ false
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ true
# Lines are parallel to themselves.
Notes
All the test cases use valid input (so no lists of the wrong size, for example).
All the coefficients will be integers (whole numbers).

---

## Two Distinct Elements
In each input list, every number repeats at least once, except for two.

Write a function that returns the two unique numbers.

Examples
returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]

##Notes
Keep the same ordering in the output.

---

##The Karaca's Encryption Algorithm

Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
o => 2
u => 3

## "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples

encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"
Notes

All inputs are strings, no uppercases and all output must be strings.

---
## Combined Consecutive Sequence

Write a function that returns True if two lists, when combined, form a consecutive sequence.

Examples

consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
Notes

The input lists will have unique values.
The input lists can be in any order.
A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

---
## Next Prime
Published by Helen Yu in Python
mathnumbers
Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

Examples

next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
(11 is a prime, so we return the number itself.)

---
## The Kempner Function
The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero which factorial is exactly divided by the number.

kempner(6) ➞ 3

1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0

kempner(10) ➞ 5

1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0
A Kempner Function applied to a prime will always return the prime itself.

kempner(2) ➞ 2
kempner(5) ➞ 5
Given an integer n, implement a Kempner Function.

Examples
kempner(6) ➞ 3

kempner(10) ➞ 5

kempner(2) ➞ 2

# Notes

* Try to solve this using a recursive method, with an approach oriented to higher order functions.

---

## The Happy Function

In this challenge, you have to implement an algorithm to establish if a given positive integer num is a Happy number, and how many steps of the algorithm are needed to establish it.

You have to repeatedly transform the given num into the sum of its squared digits:

If after the transformation the new number is equal to 1, num is a Happy number and the algorithm stops.
If after the transformation, the new number is not equal to 1, you have to transform it again.
Happy Numbers

If a number can't be reduced to 1, sooner or later the algorithm will enter into an infinitely repeating loop:

... 20, 4, 16, 37, 58, 89, 145, 42, 20, 4 ...
Given a positive integer num, implement a function that returns:

If num is a Happy number, the string "HAPPY x" with the "x" being the number of steps necessary to reduce num to 1.
If num is not a Happy number, the string "SAD x" with the "x" being the number of steps necessary to enter into the infinite loop reaching so any number in the series 4, 16, 37, 58, 89, 145, 42, 20, plus the number of steps necessary to obtain again that number.
Look at the examples below for a better visualization.

Examples

happy_algorithm(139) ➞ "HAPPY 5"

# Step 1: Transform 139
# 1² + 3² + 9² = 1 + 9 + 81 = 91

# Step 2: Transform 91
# 9² + 1² = 81 + 1 = 82

# Step 3: Transform 82
# 8² + 2² = 64 + 4 = 68

# Step 4: Transform 68
# 6² + 8² = 36 + 64 = 100

# Step 5: Transform 100
# 1² + 0² + 0² = 1 + 0 + 0 = 1

# The algorithm stops at step 5: 139 is a Happy number

happy_algorithm(67) ➞ "SAD 10"

# Step 1: Transform 67
# 6² + 7² = 36 + 49 = 85

# Step 2: Transform 85
# 8² + 5² = 64 + 25 = 89
# It entered into the infinite loop...
# ...but we have to demonstrate that is a loop!

# Step 3: Transform 89
# 8² + 9² = 64 + 81 = 145

# Step 4: Transform 145: result is 42
# Step 5: Transform 42: result is 20
# Step 6: Transform 20: result is 4
# Step 7: Transform 4: result is 16
# Step 8: Transform 16: result is 37
# Step 9: Transform 37: result is 58
# Step 10: Transform 58: result is 89

# 89 was the result of step 2: it's a loop
# The algorithm stops at step 10: 67 is not a Happy number

happy_algorithm(1) ➞ "HAPPY 1"

# Step 1: Transform 1
# 1² = 1

# The algorithm stops at step 1: 1 is a Happy number

happy_algorithm(89) ➞ "SAD 8"

# Step 1: Transform 89: result is 145
# Step 2: Transform 145: result is 42
# Step 3: Transform 42: result is 20
# Step 4: Transform 20: result is 4
# Step 5: Transform 4: result is 16
# Step 6: Transform 16: result is 37
# Step 7: Transform 37: result is 58
# Step 8: Transform 58: result is 89

# 89 was the original number: it's a loop
# The algorithm stops at step 8: 89 is not a Happy number

### Notes
* The transformation of a single-digit number is, trivially, the square of the digit (see example #3).

* If the given number is 1, a step is needed to establish if it's Happy (see example #3).

* To establish if a number is not happy, you have to find the number of steps necessary to obtain again a  number already found (it can be a number obtained through a transformation as in example #2 or the same given number as in example #4).

* You can expect only positive integers as input, without exceptions to handle.
