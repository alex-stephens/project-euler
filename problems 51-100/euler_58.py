# Project Euler
# Problem 58

# Spiral primes

import sys
sys.path.append('../')
from euler import isPrime

n = 1
fracPrime = 1
numPrime = 0

while fracPrime >= 0.1:
    n += 2
    numOnDiags = 2*n + 1
    
    num = n**2 - 3*n + 3
    for _ in range(3):
        numPrime += 1 if isPrime(num) else 0
        num += (n-1)
    
    fracPrime = numPrime / numOnDiags
    
print(n)