# Project Euler
# Problem 100

# Arranged probability

import numpy as np

'''
Need to solve
b(b-1) / n(n-1) = 1/2
2b**2 - 2b = n**2 - n
'''

start = 10**12
n = start
A = 2
B = -2

while n < 10*start:
    C = -(n**2 - n)
    b = int((-B + (B**2 - 4*A*C)**(1/2))/(2*A))

    if 2*b*(b-1) == -C:
        break

    n += 1

print(b)
print(n)
print(b * (b-1) / (n * (n-1)))
    
    