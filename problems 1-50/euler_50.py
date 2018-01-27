# Project Euler
# Problem 50

# Consecutive prime sum

import sys
sys.path.append('../')
from euler import listPrimes

target = 10**6
longest = 21
primes = listPrimes(target)
ans = 2
i = 0 

while primes[i] * longest < target:
    length = longest    
    j = i + longest
    
    sumSeq = sum(primes[i:j])
    while sumSeq  < target:
        
        if sumSeq in primes:
            longest = length
            ans = sumSeq

        length += 1
        j += 1
        sumSeq = sum(primes[i:j])
    
    i += 1

print(ans)