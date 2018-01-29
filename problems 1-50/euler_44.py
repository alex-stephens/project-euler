# Project Euler
# Problem 44

# Pentagonal numbers

import sys
sys.path.append('..')
from euler import isPerfectSquare
from math import sqrt

# computes the nth pentagonal number
def pent(n):
    return (n * (3*n - 1)) // 2

# difference between nth and n+1th pentagonal number
def pentDiff(n):
    return 1 + 3*n

# checks if a number is pentagonal
def isPent(n):
    if not isPerfectSquare(1+24*n):
        return False
    num = int(sqrt(1 + 24*n))
    if (num + 1) % 6 == 0:
        return True
    return False

j,k = 0,0
done = False

while not done:
    pk = pent(k)
    
    for j in range(1,k):
        pj= pent(j)
        if isPent(pk - pj) and isPent(pk + pj):
            done = True
            break        
    k += 1

print(pk - pj)