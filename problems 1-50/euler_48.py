# Project Euler
# Problem 48

# Self powers

import numpy as np

num = 0
print(type(num))
for i in range(1,1001):
    num += i**i
    num %= 10**10 # remove all but last 10 digits
print(num)

'''
# Full brute force
num = sum([i**i for i in range(1,1001)])
print(str(num)[-10:])
'''