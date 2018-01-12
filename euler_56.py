# Project Euler
# Problem 54

# Poker hands

import numpy as np

maxDigitSum = 0
for a in range(90,100): # don't check low vals where results have few digits
    for b in range(90,100):
        maxDigitSum = max(sum([int(i) for i in str(a**b)]),maxDigitSum)
print(maxDigitSum)