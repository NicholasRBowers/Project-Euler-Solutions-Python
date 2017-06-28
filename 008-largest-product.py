#!/usr/bin/python3

"""
Find the greatest product of five consecutive digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""

# This code runs in 0.00127100944519 seconds.
import time

number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# This function finds the largest product of m consecutive digits in a number, n.
def largest_product(n, m):                              # Accepts two integers: n, the # to analyze, and m, the # of digits which form the product.
    n = str(n).split('0')                               # Convert n to a string & split it up into a list of consecutive numbers which don't include zero.
    n = [item for item in n if len(item) >= m]          # Get rid of all of the consecutive numbers with less than m members (would include a zero).
    largest_product = 1                                 # Create a variable to store our largest product.
    for i in n:                                         # Iterate through our list of consecutive numbers.
        product = 1                                     # Create a variable to hold the current product.
        matrix = []                                     # Create an empty matrix which will serve as a sliding window of m length.
        for j in range(m):                             # Repeat m times.
            matrix.append(i[j])                         # Append the first five members of the current string to our sliding window.
            product *= int(i[j])                        # And calculate the initial product for these five integers.
        k = m                                           # Create a counter variable which marks the ending of our sliding window.
        x = product                                     # Create a variable which will help us find the greatest product in each member of n.
        while k < len(i):                               # While the window is not at the end of the current string,
            x = x / int(matrix[0])                      # Divide out the first member of the window.
            del matrix[0]                               # Delete the first member of the window.
            matrix.append(i[k])                         # Add the next number in the current string to the sliding window.
            x = x * int(matrix[m - 1])                  # Multiply in that next number to our temporary product holder.
            if x > product:                             # If this product is greater than the previous product we had stored for this string,
                product = x                             # Overwrite it.
            k += 1                                      # Move on to the next string.
        if largest_product < product:                   # If the largest product in the current string is greater than the global one we have stored,
            largest_product = product                   # Overwrite it.
    return largest_product                              # Return the largest product.

s = time.time()
print(largest_product(number, 5))
f = time.time()
print(f - s)