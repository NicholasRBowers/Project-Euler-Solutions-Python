#!/usr/bin/pythonw

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# Adapt code to use this instead: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes.

# This code runs in 35.3155958652 seconds.
import time

# This function determines whether or not an integer, n, is a prime number.
# Can only analyze positive numbers correctly.
def is_prime(n):                # Accepts an integer, n, which has its primeness tested.
    j = 3                       # We start a counter at 3.
    while j <= n ** 0.5:        # While j is less than or equal to the square root of the number,
        if n % j == 0:          # If, at any point, n is evenly divisible by j,
            return False        # Return False.
        j += 1                  # Increment our counter by 1.
    return True                 # Return true if we couldn't get the number to divide evenly by any factor.

# This function finds the sum of primes under a number, n.
def sum_primes_under(n):        # Accepts an integer, n.
    sum_of_primes = 2           # Set up a variable to keep track of the sum.
    i = 3                       # Start the counting at 3.
    while i <= n:               # While our prime, i, is less than the number, n,
        if is_prime(i):         # If i is prime,
            sum_of_primes += i  # Add it to our sum.
        i += 2                  # Increment by two (all subsequent primes are odd).
    return sum_of_primes        # Return the sum of primes under the number, n.

#print sum_primes_under(10)
s = time.time()
print sum_primes_under(2000000)
f = time.time()
print f - s