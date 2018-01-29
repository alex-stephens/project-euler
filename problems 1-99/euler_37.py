# Project Euler
# Problem 37

# Truncatable primes
    
import sys
sys.path.append('../')
from euler import listPrimes
import numpy as np

primes = listPrimes(1000000)
maxIndex = np.shape(primes)[0] - 1

target = 11
i = 0
count = 0
truncatablePrimes = []
while count < target and i < maxIndex:
    n = primes[i]
    i += 1
    if n < 10:
        continue
    truncatable = True
    
    string = str(n)
    for j in '02468':
        if j in string[1:]:
            truncatable = False
            break
    if not truncatable:
        continue
        
    # truncating from right
    for j in range(len(string) - 1):
        trunc = string[:(-1-j)]
        if int(trunc) not in primes[:i]:
            truncatable = False
            break
    
    # truncating from left
    for j in range(len(string) - 1):
        trunc = string[(j+1):]
        if int(trunc) not in primes[:i]:
            truncatable = False
            break
    
    if truncatable:
        print(n)
        count += 1
        truncatablePrimes.append(n)
        
if i == maxIndex:
    print('Error - insufficient search range')
else:
    print(sum(truncatablePrimes))
    