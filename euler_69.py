# Project Euler
# Problem 69

# Euler's totient function

import numpy as np

target = 1000000

'''
MUCH faster approach : n/phi(n) is maximised when n is a product of all the 
smallest primes
'''

# Find all primes below 100
n = 100**2
primes = []

A = [True] * n
A[:2] = [False, False]

for i in range(2,int(np.sqrt(n)) + 1):
    
    if A[i]:
        primes.append(i)
        for j in range(i**2, n, i):
            A[j] = False
            
# Find maximum product of first primes below 1 million      
product = 1
i = 0       
while product*primes[i] <= target:
    product *= primes[i]
    i += 1
print(product)
    

'''
Compute totient function using Euler's product formula
'''
'''
def phi(n):
    result = n
    for p in range(2, int(np.sqrt(n)) + 1):
        if n % p == 0:
            result -= result/p
            while n % p == 0:
                n //= p
    
    if (n > 1):
        result -= result/n

    return int(result)

maxVal = 0

print(np.argmax([i/phi(i) for i in range(1,max+1)]) + 1)
'''

