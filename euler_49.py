# Project Euler
# Problem 49

# Prime permutations
    
from euler import listPrimes

searchMax = 10000
primes = listPrimes(searchMax)
for i in range(len(primes)-1, -1, -1):
    if primes[i] <= 1000:
        primes.pop(i)

values = []

for n in primes:
    deltaMax = (9999 - n) // 2
    sortedTarget = sorted(str(n))
    
    for delta in range(2,deltaMax,2):
        if sorted(str(n+delta)) != sortedTarget:
            continue
        elif sorted(str(n+2*delta)) != sortedTarget:
            continue
        elif (n + delta) not in primes:
            continue
        elif (n + 2*delta) not in primes:
            continue
        
        values.append([n, n+delta, n+2*delta])
        
for i in values:
    string = ''
    for j in i:
        string += str(j)
    print(string)
           

