# Project Euler
# Problem 51

# Prime digit replacements

import sys
sys.path.append('../')
from euler import listPrimes, isPrime
from itertools import combinations
import time


def findOccurences(string, c):
    return [i for i, letter in enumerate(string) if letter == c]


for d in range(7,8):
    s = time.time()
    
    print(d, 'DIGITS')
    lower, upper = 10**(d-1), 10**d - 1
    primes = listPrimes(10**d)    
    
    occ = {}
    
    maxCount = 0
    
    for p in primes:
        if p < lower:
            continue
        
        string = str(p)
        
        # digit to replace (0,1,2,...)
        for n in range(0,9):
            
            ind = findOccurences(string, str(n))
            numIndices = len(ind)
            
            # number of instances of the digit to replace
            for x in range(1,numIndices+1):
                
                # which digits to replace
                for comb in combinations(ind, x):
                    
                    # generate the generic string
                    generic = list(string)
                    for i in comb:
                        generic[i] = '*'
                    generic = ''.join(generic)
                    #print(p, generic)
                    
                    if generic not in occ:
                        occ[generic] = 1
                    else:
                        occ[generic] += 1
                        maxCount = max(maxCount, occ[generic])
                        
    print(maxCount)


    print('time taken for {} digits: {:.2f} seconds'.format(d, time.time()-s))