#!/usr/bin/pythonw

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(n):
    i = 2
    while n > i:
        while n % i == 0:
            n = n / i
        i += 1
    print n

#largest_prime_factor(13195)
largest_prime_factor(600851475143)