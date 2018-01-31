# Project Euler
# Problem 100

# Arranged probability

import sys
sys.path.append('..')
from euler import isPerfectSquare
from math import sqrt
import time

'''
Need to solve
b(b-1) / n(n-1) = 1/2
2b**2 - 2b = n**2 - n
2(b - 1/2)**2 = n**2 - n + 1/2
b = 0.5 + 0.5 * sqrt(n**2 - n + 1/2)
'''
start = time.time()

target = 10**1
n = target

x = int(target * sqrt(2))
x += 1 - (x % 2)        # make x odd only
while not isPerfectSquare(2*x**2 - 1):
    x += 2
    #print(x)
    
n = int(0.5 * (1 + sqrt(2*x**2 - 1)) + 1/2)  # + 1/2 for rounding
print('n = ' + str(n))

b = int(0.5 * (1 + sqrt(2*n**2 - 2*n + 1)) + 1/2)   
print('b = ' + str(b))

print(b * (b-1) / (n * (n-1)))

print('time taken: ' + str(time.time() - start) + ' seconds')

    
        
    