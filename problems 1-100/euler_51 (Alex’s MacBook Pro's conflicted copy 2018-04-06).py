# Project Euler
# Problem 51

# Prime digit replacements

import sys
sys.path.append('../')
from euler import listPrimes
from itertools import combinations
import time

for d in range(2,4):
    s = time.time()
    maxVal = 0
    
    print(d, 'DIGITS')
    lower, upper = 10**(d-1), 10**d - 1
    primes = listPrimes(10**d)
    
    digitsToReplace = [i for i in range(d-1)]
    
    occ = {}
    

    for p in primes:
        if p < lower: continue
    
        num = list(str(p))
    
        # number of digits to replace
        for n in range(1,d):
    
            # indices to replace
            for rep in combinations(digitsToReplace, n):
                
                val = num[rep[0]]
                result = True
                for i in rep[1:]:
                    if num[i] != val:
                        result = False
                        break
                    
                if result:
                    for i in rep:
                        num[i] = '*'
                        
                    numstr = ''.join(num)
                    
                    if numstr in occ:
                        occ[numstr] += 1
                    else:
                        occ[numstr] = 1
                        
    maxVal, string = 0, ''
    
    for k in occ.keys():
        
        if occ[k] > maxVal:
            maxVal = occ[k]
            string = k
            
    print(k)
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    