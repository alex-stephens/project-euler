# Project Euler
# Problem 46

# Goldbach's other conjecture

import numpy as np

max = 10000

A = [True] * max
A[:2] = [False, False]

# Find all primes up to max (Sieve of Eratosthenes)
for i in range(2,int(np.sqrt(max)) + 1):
    
    if A[i]:
        for j in range(i**2, max, i):
            A[j] = False
    
# Go through all odd numbers up to max
for i in range(3,max+1,2):
    
    if A[i]:
        continue
    
    result = False
    for j in range(2,i-1):
        if not A[j]:
            continue
        if int(math.sqrt((i - j) // 2))**2 == (i - j) // 2:
            result = True
    
    if not result:
        break
    
print(i)