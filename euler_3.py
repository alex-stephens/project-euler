# Project Euler
# Problem 3

# Largest prime factor

import numpy as np

n = 600851475143
fac = 2
primefacs = []

while fac <= n:
    if n % fac == 0:
        primefacs.append(fac)
        n /= fac
        fac = 2
    else:
        fac += 1
        
        
print(primefacs)
        
