# Project Euler
# Problem 21

# Amicable numbers

import numpy as np
    
def d(n):
    d = 0
    for i in range(1,n):
        if n % i == 0:
            d += i
    return d
       
numToCheck = 10000     
dvals = np.zeros(numToCheck)
answer =  0

for i in range(1,numToCheck+1):
    val = d(i)
    if val < i:
        if dvals[val-1] == i:
            answer += val + (i) 
        
    dvals[i-1] = val

print(answer)