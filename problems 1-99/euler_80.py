# Project Euler
# Problem 80

# Square root digital expansion

from math import sqrt

print(sqrt(2))

target = 2
placeVal = 1
val = placeVal

num = [0] * (2 + 100)
# [tens, ones, tenths, hundredths, ...]
digits = 100

def evaluate(number, highestPlaceVal):
    result = 0
    pval = highestPlaceVal
    for i in range(len(number)):
        result += pval * number[i]
        pval /= 10
    return result


for digits in range(digits):
    
    while evaluate(num[:digits+1], 1)**2 < target:
        num[digits] += 1
    num[digits] -= 1
        
        
