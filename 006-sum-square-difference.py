#!/usr/bin/python3

"""
The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# This code runs in 3.79085540771e-05 seconds.
import time

# This function finds the sum of the squares of the numbers one through an integer, n.
def sum_of_squares(n):              # Accepts an integer, n, as the upper bound.
    sum = 0                         # A variable to hold the sum.
    for i in range(n+1):           # Iterate through to the upper bound.
        sum += i ** 2               # Add the square of each integer to the sum.
    return sum                      # Return the sum.

# This function finds the square of the sum of the numbers one through an integer, n.
def square_of_sum(n):               # Accepts an integer, n, as the upper bound.
    sum = 0                         # A variable to hold the sum.
    for i in range(n+1):           # Iterate through to the upper bound.
        sum += i                    # Add each integer to the sum.
    return sum ** 2                 # Return the squared sum.

#print square_of_sum(10) - sum_of_squares(10)
s = time.time()
print(square_of_sum(100) - sum_of_squares(100))
f = time.time()
print(f - s)