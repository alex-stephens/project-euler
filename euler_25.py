# Project Euler
# Problem 25

# 1000-digit Fibonacci number

import numpy as np
from math import log

n = 2
target = 1000

fibonacci = [0,1,1]
digits = 1

while digits < target:
    n += 1
    current = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(current)
    fibonacci.pop(0)    # remove extra elements to save space
    digits = int(log(current,10)) + 1
    
print(n)
