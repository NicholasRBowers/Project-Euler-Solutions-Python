#!/usr/bin/pythonw

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2; for example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc.
"""

# This code runs in 0.0454270839691 seconds.
import time

# This function finds the first Pythagorean triplet which adds up to in a number, n.
def triplet(n):                         # Accepts a sum, n, a Pythagorean triplet.
    for a in xrange(1, n):              # Iterate a from 1 to the sum.
        for b in xrange(1, n):          # Do the same for b.
            c = n - a - b               # Set c, so that the sum is always n.
            if a**2 + b**2 == c**2:     # If the set of numbers is a Pythagorean triplet,
                return a * b * c        # Return their product.

#print triplet(25)
s = time.time()
print triplet(1000)
f = time.time()
print f - s