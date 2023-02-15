'''
A prime number is a positive integer greater than 1 that has no positive integer divisors
other than 1 and itself. In other words, a prime number is only divisible by 1 and itself. 

For example, the first few prime numbers are:
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

'''

import math

def is_prime_number(n):
    if n < 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:      # dividing by every number between 2 to square root of the number (inclusive).
            return False
    return True




print(is_prime_number(11))
