# Project Euler
# Problem 87

# Prime power triples

from euler import listPrimes
import math
from itertools import product

cap = 50  * 10**6
a_cap = int(cap ** (1/2))
b_cap = int(cap ** (1/3))
c_cap = int(cap ** (1/4))

primes = listPrimes(int(math.sqrt(cap)))
numbers = set()

for comb in product(primes,repeat=3):
    (a,b,c) = comb
    if a > a_cap or b > b_cap or c > c_cap:
        continue
    
    
    ans = a**2 + b**3 + c**4
    if ans <= cap:
        numbers.add(ans)
    
    #print(comb)
print(len(numbers))