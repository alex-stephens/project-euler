# Project Euler
# Problem 36

# Double-base palindromes

import numpy as np
from math import log

n = 1000000
ans = 0

for i in range(1,n):

    decimal = str(i) 
    binary = bin(i)[2:]
    
    if decimal == decimal[::-1] and binary == binary[::-1]:
        ans += i
    
print(ans)

