#!/usr/bin/python3

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

import time

# Return the sum of the digits of 2 raised to any number, n.
def power_digit_sum(n):
    power = str(2**n)              # Convert 2^n to an iterable string.

    sum = 0

    for digit in power:
        sum += int(digit)

    return sum


s = time.time()
print(power_digit_sum(1000))
f = time.time()
print(f - s)