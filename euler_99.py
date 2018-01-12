# Project Euler
# Problem 99

# Largest exponential

import numpy as np
    
numbers = np.loadtxt(open('euler_99.txt', "rb"), delimiter=",").astype(int)

[rows,_] = np.shape(numbers)

maxLine = 0
maxValue = 0

for i in range(rows): 
    currentValue = numbers[i][1] * np.log(numbers[i][0])
    if currentValue > maxValue:
        maxLine = i
        maxValue = currentValue
        
print(maxLine + 1)
    
    

    