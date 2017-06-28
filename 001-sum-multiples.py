#!/usr/bin/python3

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# This code runs in 0.000212907791138 seconds.
import time

# This function sums the multiples of factors, f, below some limit, n.
def sum_divisibles(n, *f):          # Accepts many factors as input.
    sum = 0                         # Variable to keep track of the sum.
    for i in range(1, n):          # Iterate through to the limit.
        for j in f:                 # Iterate through the factors.
            if i % j == 0:          # If the current number we're checking is evenly divisible by any of our factors.
                sum += i            # Add the number to the sum.
                break               # And break the 'for' loop to avoid double counting when a number is a multiple of more than one of factors.
    return sum                      # Return the sum.

#print sum_divisibles(10, 3, 5)
s = time.time()
print(sum_divisibles(1000, 3, 5))
f = time.time()
print(f - s)
