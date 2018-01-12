# Project Euler
# Problem 58

# Spiral primes

import numpy as np
from euler import listPrimes

size = 1
increment = 2
n = 3
diagonals = []
fracPrime = 1
cap = 10**7     # probably need 10**8 to get the solution
primes = listPrimes(cap)
numPrime = 0
print('memed')
found = True

while fracPrime >= 0.1:
    size += 2
    if size**2 > cap:
        found = False
        break
    
    
    for i in range(3):  # no need to check bottom right diagonal
        newEl = n + i*increment
        
        isPrime = False  # search for element near start of sorted primes list
        j = 0
        while primes[j] <= newEl:
            if primes[j] == newEl:
                isPrime = True
                break
            j += 1
        
        numPrime += (1 if isPrime else 0)
        
    n += 3*increment + (size+1)
    increment += 2
    fracPrime = numPrime / (size*2 - 1)
    print(str(size) + '    ' + str(fracPrime))
    
    #print(str(numPrime) + '   ' + str(size*2-1) + '  ' + str(size))
    
    while len(primes) > 0 and newEl > primes[0]:
        primes.pop(0)

if found:       
    print(size)
else:
    print('Insufficient search range')