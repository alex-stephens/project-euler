# Project Euler
# Problem 14

# Longest Collatz sequence

import numpy as np

maxLength = 0
n = 0

for val in range(2,1000000):
    chainLength = 1
    n = val
    while n != 1:
        n = int(n/2) if n%2==0 else 3*n+1
        chainLength += 1
    
    if chainLength > maxLength: 
        maxNum = val
        maxLength = chainLength
        
print(maxNum)