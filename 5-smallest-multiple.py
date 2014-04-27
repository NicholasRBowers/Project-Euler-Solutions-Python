#!/usr/bin/pythonw

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# This code runs in 6.89029693604e-05 seconds.
import time

# This function finds the prime factors of an integer, n.
def prime_factors(n):               # Accepts an integer, n, of which prime factors are found.
    i = 2                           # Sets our prime factor to 2.
    factors = []                    # Creating a list which will hold the prime factors.
    while n >= i:                   # While our number is greater than or equal to our prime factor,
        while n % i == 0:           # While the number is evenly divisible by our prime factor,
            factors.append(i)       # Add the factor to our list.
            n = n / i               # Cut down our number by dividing out the factor.
        if i == 2:                  # If our prime factor is 2,
            i += 1                  # Add one.
        else:                       # Otherwise,
            i += 2                  # Add two (all subsequent prime factors are odd).
    return factors                  # Return the list of the prime factors.

# This problem is solved by constructing the number by multiplying together the uncommon prime numbers and excluding any repeats not in the same group.
# Example:  The prime factors of 2520 are 2, 2, 2, 3, 3, 5, and 7.  Now we look at the prime factors for numbers 10 through 1:
# 10 = 2 * 5, 9 = 3 * 3, 8 = 2 * 2 * 2, 7 = 7, 6 = 2 * 3, 5 = 5, 4 = 2 * 2, 3 = 3, 2 = 2, and 1 = 1
# If we take the five from the 10, the two threes from the nine, the three twos from 8, and the seven from 7,
# All of the prime factors in this group are accounted for, and there are only as many of them as there are in one group
# (three two's from 8 and two three's from 9).  When we multiply all these factors, we get 2520, the smallest, evenly divisible number.
# This function finds the smallest number that is evenly divisible by all the numbers between 1 and an integer, n.
def evenly_divisible(n):                                                # Accepts an integer, n, which serves as the upper bound for divisible range.
    factors = []                                                        # Empty list to hold the prime factors we need to make our evenly divisible number.
    while n > 1:                                                        # While the upper bound is greater than one,
        primes = prime_factors(n)                                       # Import all of the prime factors for the upper bound.
        for i in primes:                                                # Iterate through all of the prime factors for the upper bound.
            if primes.count(i) > factors.count(i):                      # If # of a specific factor is greater than the # of that factor we have stored,
                for j in xrange(0, primes.count(i) - factors.count(i)): # Repeat the next step the (difference between the counts) times.
                    factors.append(i)                                   # Store this factor to our factor list.
        n -= 1                                                          # Decrement our number by 1.
    product = 1                                                         # Create a variable which will store our product.
    for k in factors:                                                   # Iterate through the list of factors we've compiled.
        product *= k                                                    # Multiply the product by the current factor.
    return product                                                      # Return the product

#print evenly_divisible(10)
s = time.time()
print evenly_divisible(20)
f = time.time()
print f - s