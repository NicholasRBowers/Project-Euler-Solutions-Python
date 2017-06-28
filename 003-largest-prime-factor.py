#!/usr/bin/python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

# This code runs in 0.00055193901062 seconds.
import time

# This function finds the largest prime factor of a number, n.
def largest_prime_factor(n):        # Accepts a number, n, for which the largest prime factor will be found.
    i = 2                           # Declaring a variable which we'll use to cut n into it's prime factors, we start with 2.
    while n > i:                    # While our number we're cutting down is bigger than our prime factor,
        while n % i == 0:           # While our number can be evenly divided by our prime factor,
            n = n / i               # Cut down n by dividing out the prime factor.
        if i == 2:                  # If our potential factor is 2,
            i += 1                  # Increment our potential factor by one.
        else:                       # Otherwise,
            i += 2                  # Increment our potential factor by two (all subsequent prime factors are odd).
    return n                        # We are left with the largest prime factor.  Return this.

#print largest_prime_factor(13195)
s = time.time()
print(largest_prime_factor(600851475143))
f = time.time()
print(f - s)