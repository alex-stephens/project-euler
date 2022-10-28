# Project Euler
# Problem 2

# Even Fibonacci numbers

import numpy as np

fibnprev = 1
fibn = 1
sum = 0

while fibn < 4e6:
    if fibn % 2 == 0:
        sum += fibn
        
    temp = fibnprev
    fibnprev = fibn
    fibn = fibn + temp
    
print(sum)