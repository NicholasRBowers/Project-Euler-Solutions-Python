#!/usr/bin/pythonw

"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# This code runs in 0.0103161334991 seconds.
import time

# This function determines the sum of the self powers of the first n, integers.
def sum_self_powers(n):             # Accepts an integer, n, which serves as an upper limit.
    sum = 0                         # A variable to keep track of our sum.
    for i in xrange(1, n + 1):      # Iterate through each of the numbers in the series.
        sum += i**i                 # Add the number's self power to the sum.
    return sum                      # Return the final sum.

#print sum_self_powers(10)
s = time.time()
print sum_self_powers(1000) % 10000000000 # The modulus strips off the last 10 digits.
f = time.time()
print f - s