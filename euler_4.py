# Project Euler
# Problem 4

# Largest palindrome product

import numpy as np

start = 100
end = 1000
max = 0

for i in range(start,end):
    for j in range(start,end):
        
        val = i*j
        string = str(val)
        
        if string == string[::-1] and val > max:
            max = val
        
print(max)