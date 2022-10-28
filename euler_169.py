# Project Euler
# Problem 169

# Expressing numbers as a sum of powers of 2

import math


n = 10**25

maxPower = int(log(n, 2))

powers = [2**p for p in range(maxPower+1)]
print(powers)

dp = [0 for _ in range(n+1)]

def ways(n):
    pass
    


