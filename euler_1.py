# Project Euler
# Problem 1

# Multiples of 3 and 5

import numpy as np

sum = 0

for i in range(1,1000):
    if (i % 3 is 0) or (i % 5 is 0):
        sum += i      
        
print(sum)