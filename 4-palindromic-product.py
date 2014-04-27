#!/usr/bin/pythonw

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# This code runs in 0.479487895966 seconds.
import time

# This function determines whether or not an integer is palindromic.
def is_palindromic(n):              # Accepts an integer, n, which it checks for palindromic structure.
    n = str(n)                      # Converts the integer to a string.
    if n == n[::-1]:                # If the number reads the same forwards as it does backwards,
        return True                 # Return True.
    else:                           # Otherwise,
        return False                # Return False.

# This function finds the largest palindromic number made from the product of two numbers with n digits.
def largest_palindrome(n):                          # Accepts an integer, n, which describes how many digits the factors have.
    i = 10 ** (n - 1)                               # Our first factor starts at 10 to the n - 1 (i = 100 for n = 3).
    largest = 0                                     # Declare a variable which will keep track of our largest palindrome.
    while i < 10 ** n:                              # While the first factor is still n digits long,
        j = 10 ** (n - 1)                           # Create a second factor with n digits.
        while j < 10 ** n:                          # While the second factor is still n digits long,
            p = i * j                               # Store the product of the two factors.
            if is_palindromic(p) and (p) > largest: # If the product of the two factors are palindromic, and larger than our current largest palindrome,
                largest = p                         # Overwrite the largest palindrome.
            j += 1                                  # Increment the second factor.
        i += 1                                      # Increment the first factor.
    return largest                                  # Return the largest palindrome.

#print largest_palindrome(2)
s = time.time()
print largest_palindrome(3)
f = time.time()
print f - s