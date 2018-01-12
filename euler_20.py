# Project Euler
# Problem 20

# Factorial digit sum

import numpy as np

target = 100
factorial = 1

for i in range(1,target):
    factorial *= i

string = str(int(factorial))  
print(string)  

digitSum = np.sum([int(string[i]) for i in range(len(string))])
print(digitSum)
