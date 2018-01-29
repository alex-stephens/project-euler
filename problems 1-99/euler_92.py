# Project Euler
# Problem 92

# Square digit chains

import numpy as np

def nextInChain(n):
    string = str(n)
    return sum([int(x)**2 for x in string])

count = 0 
num = 10**7
digits = int(np.log10(num))
A = [0] * (9**2 * digits + 1)   # max value occurs at 9,999,999
A[1] = 1
A[89] = 89

for n in range(1,num+1):
    orig = nextInChain(n)
    n = orig
    currentChain = [orig]
    
    while A[n] == 0:
        n = nextInChain(n)
        currentChain.append(n)
        
    val = (89 if A[n] == 89 else 1)
    for i in range(len(currentChain)):
        A[currentChain[i]] = val
    count += (1 if val == 89 else 0)

print(count)