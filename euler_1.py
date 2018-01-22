# Project Euler
# Problem 1

# Multiples of 3 and 5

import numpy as np

'''
Very fast solution, works for larger numbers
'''

result = 0
n = 10**10

def triangular(n):
    return n * (n+1) // 2

chainSums = [i*multiples((n-1) // i) for i in [3,5,15]]

result = chainSums[0] + chainSums[1] - chainSums[2]
print(result)


'''
Brute-force solution

for i in range(1,n):
    if (i % 3 is 0) or (i % 5 is 0):
        result += i      
        
print(result)
'''