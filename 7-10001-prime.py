#!/usr/bin/pythonw

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

# This code runs in 0.570377111435 seconds.
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

# This function finds the n-th prime.
def prime(n):                   # Accepts an integer, n, which tells the function which prime to find.
    primes = [2]                # Start off with a list to hold our primes pre-populated with a 2 (only even prime).
    i = 3                       # Start the counting at 3.
    while len(primes) < n:      # While the length of our list is less than the n (n-th prime),
        if is_prime(i):         # If i is prime,
            primes.append(i)    # Add it to our list.
        i += 2                  # Increment by two (all subsequent primes are odd).
    return primes[-1]           # Return the last member of our list.

#print prime(6)
s = time.time()
print prime(10001)
f = time.time()
print f - s