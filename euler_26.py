# Project Euler
# Problem 26

# Reciprocal cycles

import numpy as np
from math import gcd

'''
Compute the length of the repeating cycle a/b for a < b
'''
def cycleLength(a,b):
    divisor = gcd(a,b)
    a //= divisor
    b //= divisor
    
    twos = 0
    while b % 2 == 0:
        b //= 2
        twos += 1
    fives = 0
    while b % 5 == 0:
        b //= 5
        fives += 1
        
    if b == 1:
        return 0 
        
    transient = max(twos, fives)
    r = 1
    while 10**r % b != 1:
        r += 1
    
    return r 

print(np.argmax([cycleLength(1,i) for i in range(1,1000)]) + 1)    

