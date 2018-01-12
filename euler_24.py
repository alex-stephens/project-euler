# Project Euler
# Problem 24

# Lexicographic permutations

import numpy as np
    
size = 10
step = 1000000
array = [i for i in range(size)]

for _ in range(step-1):
    done = False
    i = len(array) - 1
    while array[i-1] >= array[i]:
        i -= 1
        if i == 0:
            array.sort() # reorder to original array
            done = True
    
    if done:
        continue
            
    j = len(array) - 1
    while array[j] <= array[i-1]:
        j -= 1
        if j == i:
            break # maybe not needed
    
    # swap elements i-1 and j
    temp1 = array[i-1]
    temp2 = array[j]
    array.pop(j)
    array.insert(j, temp1)
    array.pop(i-1)
    array.insert(i-1, temp2)
        
    sub = array[i:]
    sub.reverse()
    array[i:] = sub

for i in range(size):
    print(array[i], end="")
