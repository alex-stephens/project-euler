# Project Euler
# Problem 7

# 10001st prime

import numpy as np

num = 10001
found = 3
current = 5

while found < num:
    
    current += 2
    currentIsPrime = True;
    
    for i in range(3,current-1,2):
        if current%i == 0:
            currentIsPrime = False 
            break
    
    if currentIsPrime:
        found += 1
        
print(str(num) + "th prime is " + str(current))
        