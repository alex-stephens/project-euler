# Project Euler
# Problem 87

# Prime power triples

from euler import listPrimes
import math
from itertools import product

cap = 50  * 10**4

primes = listPrimes(int(math.sqrt(cap)))
numbers = set()

for comb in product(primes,repeat=3):
    (a,b,c) = comb
    
    ans = a**2 + b**3 + c**4
    if ans <= cap:
        numbers.add(ans)
    
    #print(comb)
print(numbers)