# Project Euler
# Problem 38

# Pandigital multiples
    
import numpy as np

maxValue = 0

for n in range(1,10000):
    string = str(n)
    m = 1
    while len(string) < 9:
        m += 1
        string += str(m * n)
    if len(string) > 9:
        continue
    
    if ''.join(sorted(string)) != '123456789':
        continue
    
    maxValue = max(maxValue,int(string))
    
print(maxValue)    