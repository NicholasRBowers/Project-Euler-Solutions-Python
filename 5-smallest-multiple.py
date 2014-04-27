#!/usr/bin/pythonw

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def prime_factors(n):
    i = 2
    factors = []
    while n >= i:
        while n % i == 0:
            factors.append(i)
            n = n / i
        i += 1
    return factors

def evenly_divisible(n):
    factors = []
    while n > 0:
        constituent_factors = prime_factors(n)
        for i in constituent_factors:
            if constituent_factors.count(i) > factors.count(i):
                for j in range(0, constituent_factors.count(i) - factors.count(i)):
                    factors.append(i)
        n -= 1
    product = 1
    for k in factors:
        product *= k
    return product

print evenly_divisible(20)