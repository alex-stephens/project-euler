# Project Euler
# Problem 27

# Quadratic primes

import numpy as np

n = int(2e6)

isPrime = [True] * n
isPrime[:2] = [False, False]
primes = []

for i in range(2,int(np.sqrt(n)) + 1):
    
    if isPrime[i]:
        if i <= 1000:
            primes.append(i)
        for j in range(i**2, n, i):
            isPrime[j] = False


def quadraticEval(a,b,n):
    return n**2 + a*n + b

def sequenceLength(a,b):
    if isPrime[b] is False:
        return 0
    n = 1
    while isPrime[quadraticEval(a,b,n)]:
        n += 1
        
    return n

longestSequence = 0
coeffs = [0,0]
    
for b in primes:
    for a in range(-999,1000):
        length = sequenceLength(a,b)
        if length > longestSequence:
            longestSequence = length
            coeffs = [a,b]
print(coeffs[0]*coeffs[1])