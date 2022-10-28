# Project Euler
# Problem 87

# Prime power triples

import sys
sys.path.append('../')
from euler import listPrimes
import math
from bisect import bisect_left

cap = 50 * 10**6
a_cap = int(cap ** (1/2))

primes = listPrimes(int(math.sqrt(cap)))
numbers = set()

for a in primes:
    
    b_cap = bisect_left(primes, (cap -  a**2)**(1/3))
    for b in primes[:b_cap]:
        
        c_cap = bisect_left(primes, (cap -  a**2 - b**3)**(1/4))
        for c in primes[:c_cap]:
    
            num = a**2 + b**3 + c**4
            if num < cap:
                numbers.add(num)
    
print(len(numbers))