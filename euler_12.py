# Project Euler
# Problem 12

# Highly divisible triangular number

import numpy as np
from math import gcd

def triangle(n):
    return sum([i for i in range(1,n+1)])

def countDivisors(n): 
    repetitions = []
    if n % 2 == 0:
        n //= 2
        reps = 1
        while n % 2 == 0:
            n //= 2
            reps += 1
        repetitions.append(reps)
    divisor = 3
    
    while n > 1:
        reps = 1
        if n % divisor == 0:
            n //= divisor
            while n % divisor == 0:
                n //= divisor
                reps += 1
            repetitions.append(reps)
        divisor += 1
    return np.product([i+1 for i in repetitions])
            
n = 1
target = 500
while countDivisors(triangle(n)) < target:
    n += 1
    
print(triangle(n))

