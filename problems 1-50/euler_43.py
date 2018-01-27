# Project Euler
# Problem 43

# Sub-string divisibility

import numpy as np
from itertools import permutations

def cat(array):
    result = 0
    length = len(array)
    for i in range(length):
        result += 10**(length - i - 1) * array[i]
    return result


array = [i for i in range(10)] 
result = 0 

for n in permutations(array):
    
    if n[0] == 0:
        continue
    
    if cat(n[7:]) % 17 != 0: 
        continue
    if cat(n[6:9]) % 13 != 0: 
        continue
    if cat(n[5:8]) % 11 != 0: 
        continue
    if cat(n[4:7]) % 7 != 0: 
        continue
    if cat(n[3:6]) % 5 != 0: 
        continue
    if cat(n[2:5]) % 3 != 0: 
        continue
    if cat(n[1:4]) % 2 != 0: 
        continue
    #print(cat(n))
    result += cat(n)

print(result)
  
   


