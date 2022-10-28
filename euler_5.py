# Project Euler
# Problem 5

# Smallest multiple

import numpy as np

maxval = 20
num = maxval

for currentFactor in range(maxval,0,-1):
    
    num *= currentFactor
    
    # find all prime factors of j
    temp = currentFactor
    primefacs = []
    fac = 2
    while fac <= temp:
        if temp % fac == 0:
            primefacs.append(fac)
            temp /= fac
            fac = 2
        else:
            fac += 1
            
    # Divide out all prime factors which preserve divisibility by j
    for i in primefacs:
        if num/i % currentFactor == 0:
            num /= i
        
print(int(num))