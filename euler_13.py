# Project Euler
# Problem 13

# Large sum

import numpy as np

digits = 10

string = open('euler_13.txt', 'r').read()
vals = [int(x) for x in string.split()]

sumstr = str(np.sum(vals))

print(sumstr[0:digits])