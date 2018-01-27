# Project Euler
# Problem 94

# Almost equilateral triangles

import sys
sys.path.append('../')
import numpy as np
from euler import isPerfectSquare
from time import time

start = time()
ans = 0
for i in range(10**9):
    ans += i
    
print(ans)
print('time taken: ' + str(time() - start) + ' seconds')

    
