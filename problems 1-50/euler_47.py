# Project Euler
# Problem 47

# Distinct primes factors
    
import sys
sys.path.append('../')
from euler import listPrimes
from math import sqrt

searchMax = 1000000
primes = listPrimes(int(sqrt(searchMax)))

target = 4
primeFacs = [[] for _ in range(target)]
numPrimeFacs = [0]*target


for n in range(2,searchMax):
    orig = n
    primeFacs.pop(0)
    numPrimeFacs.pop(0)
    primeFacs.append([])
    
    i = 0
    while primes[i] <= int(sqrt(n)):
        if n % primes[i] == 0:
            primeFacs[-1].append(primes[i])
            n //= primes[i]
        while n % primes[i] == 0:
            n //= primes[i]
        i += 1
    if n > 1:
        primeFacs[-1].append(n)
        
    numPrimeFacs.append(len(primeFacs[-1]))
    
    candidate = (True if numPrimeFacs == [target]*target else False)
    if not candidate:
        continue
    
    allFacs = []
    for sublist in primeFacs:
        for item in sublist:
            allFacs.append(item)

    for i in range(1,len(allFacs)):
        if allFacs[i] == allFacs[i-1]:
            candidate = False
            
    if candidate:
        break

if candidate:
    print(str(orig-target+1))
else:
    print('Insufficient search range')
        
    
