# Project Euler
# Problem 28

# Number spiral diagonals

import numpy as np

size = 1001
increment = 2
n = 3
ans = 1

for j in range(size // 2):
    ans += sum([n + i*increment for i in range(4)])    
    n += 3*increment + 2 * (j+2)
    increment += 2

print(ans)