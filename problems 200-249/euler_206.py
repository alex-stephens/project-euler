# Project Euler
# Problem 206

# Concealed square

import sys
sys.path.append('..')
from euler import isPerfectSquare
from itertools import product

l = [str(x) for x in range(10)]
num = '1234567890'

def splice(str1, str2):
    result = str1[0]
    for i in range(len(str2)):
        result += str2[i] + str1[i+1] 
    return result

for p in product(l,repeat=9):
    string = splice(num, ''.join(p))
    if isPerfectSquare(int(string)):
        break

print(int(int(string)**(1/2)))
