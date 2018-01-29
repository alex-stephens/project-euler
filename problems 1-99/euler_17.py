# Project Euler
# Problem 17

# Number letter counts

import numpy as np
    
def count(n):
    # counts for numbers 0-19
    lookupUnits = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    lookupTens = [0,3,6,6,5,5,5,7,6,6]
    
    if n <= 19:
        return lookupUnits[n]
    elif n <= 99:
        tens = n // 10
        units = n % 10
        return lookupTens[tens] + lookupUnits[units]
    elif n <= 999:
        hundreds = n // 100
        tensAndUnits = n % 100
        
        added = 7 if (tensAndUnits==0) else 10 # extra chars for 'hundred and'
        
        ans = lookupUnits[hundreds] + added + count(tensAndUnits)
        return ans
    elif n == 1000:
        return 11

print(sum([count(i) for i in range(1,1001)]))
