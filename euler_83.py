# Project Euler
# Problem 83

# Path sum: four ways

import numpy as np

digits = 1
power = 5
maxNum = 9
while digits * 9**power >= maxNum:
    digits += 1
    maxNum = maxNum * 10 + 9
maxNum = digits * 9**power

def digitsPower(n,power):
    string = str(n)
    return sum([int(x)**power for x in string])

result = 0
for i in range(10,maxNum+1):
    result += (i if digitsPower(i,power) == i else 0)  

print(result)