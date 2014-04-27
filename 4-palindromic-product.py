#!/usr/bin/pythonw

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindromic(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

i = 100
bank = 0
while i < 1000:
    j = 100
    while j < 1000:
        if is_palindromic(i * j) and (i * j) > bank:
            bank = i * j
        j += 1
    i += 1
print bank