# Project Euler
# Problem 10

# Summation of primes

# Algorithm: Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# O(nloglogn) complexity

import numpy as np

n = int(2e6)

A = [True] * n
A[:2] = [False, False]

for i in range(2,int(np.sqrt(n)) + 1):
    
    if A[i]:
        for j in range(i**2, n, i):
            A[j] = False
    
result = np.sum([A[i]*i for i in range(len(A))])
print(result)
