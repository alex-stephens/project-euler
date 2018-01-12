# Project Euler
# Problem 6

# Sum square difference

import numpy as np

num = 100
sumsquares = np.sum([x**2 for x in range(1,num+1)])
squaresum = np.sum([range(1,num+1)])**2
diff = squaresum - sumsquares
print(diff)