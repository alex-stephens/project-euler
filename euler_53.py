# Project Euler
# Problem 53

# Combinatoric selections

import numpy as np
from scipy.misc import comb

target = 1000000
count = 0

for n in range(23,101): # no solutions below n = 23

    middle = n//2    # works for both odd and even
    for r in range(2,n//2 + 1):
        if comb(n,r) > 1000000:
            count += (middle - r)*2 + 1 + (n % 2)
            break
    
print(count)