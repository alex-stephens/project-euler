# Project Euler
# Problem 39

# Integer right triangles
    
from euler import listSquares
import numpy as np

pmax = 1000
squares = listSquares(pmax**2)
p = [0] * (pmax + 1)

for a in range(1,1000):
    b = a # test only b >= a
    while b**2 <= pmax**2 - a**2:       
        if a**2 + b**2 in squares:
            perim = a + b + int(np.sqrt(a**2 + b**2))
            if perim < pmax:
                p[perim] += 1 
            #print(str(a) + '^2 \t+ ' + str(b) + '^2 = ' + str(int(math.sqrt(a**2+b**2))) + '^2')
        b += 1

print(p.index(max(p)))