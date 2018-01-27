# Project Euler
# Problem 41

# Pandigital prime
    
from euler import listPrimes
import numpy as np
from itertools import permutations

num = 987654321
primes = listPrimes(int(np.sqrt(num)))

def isPrime(primes, n):
    result = True
    for i in primes:
        if i > np.sqrt(n):
            break
        if n % i == 0:
            result = False
            break
    return result

print('starting....')   

'''
code takes long ish for 9 digits

only need to check up to 7 digits because all 8- and 9-digit pandigital 
numbers are divisible by 3 (sum of digits divisible by 3) and hence not prime
'''
for digits in range(1,10):
    result = None
    
    minLim = sum([(10**(digits-i))*i for i in range(1,digits+1)])
    array = [i for i in range(1,digits+1)]
    
    for n_array in permutations(array):
        n = sum([(10**(digits-i-1))*n_array[i] for i in range(digits)])
        if int(''.join(sorted(str(n)))) == minLim:

            if isPrime(primes,n):
                result = n
    print(str(digits) + ' digit(s): ' + str(result))


    