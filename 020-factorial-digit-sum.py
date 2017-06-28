#!/usr/bin/python3

"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

# This code runs in 0.0002543926239013672 seconds.
import time
import math

# This function determines the sum of the digits of the factorial of a number, n.
def factorial_digit_sum(n):
    factorial = str(math.factorial(n))      # Find the factorial of n and convert it to a iterable string.

    sum = 0

    for digit in factorial:
        sum += int(digit)

    return sum

s = time.time()
print(factorial_digit_sum(100))
f = time.time()
print(f - s)