# Project Euler
# Problem 23

# Non-abundant sums

import numpy as np

def sumDivisors(n):
    if n == 0:
        return 0
    result = 1
    
    if n % 2 != 0:  # odd
        for i in range(3, n//3 + 1, 2):
            result += (i if n % i == 0 else 0)
            
    else:           # even
        for i in range(2, n//2 + 1):
            result += (i if n % i == 0 else 0)
            
    return result

target = 28123
abundant = [False] * (target + 1)

for i in range(1,target):
    if sumDivisors(i) > i:
        abundant[i] = True

ans = 0

for i in range(1,target+1):
    sumAbundant = False
    
    for j in range(1,i//2 + 1):
        if abundant[j] and abundant[i-j]:
            sumAbundant = True
            break
    ans += (i if not sumAbundant else 0)

print(ans)