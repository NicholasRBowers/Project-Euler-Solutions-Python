#!/usr/bin/pythonw

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import time

def is_prime(n):
    j = 3
    while j <= n ** 0.5:
        if n % j == 0:
            return False
        j += 1
    return True

def prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes[-1]

s = time.time()
print prime(10001)
f = time.time()
print f - s