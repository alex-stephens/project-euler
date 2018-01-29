# Project Euler
# Problem 114

# Counting block combinations I

from scipy.misc import comb

size = 50
r,g,b = 2,3,4
ways = 0

for x in [r,g,b]:
    for num in range(1,size//x+1):        
        tiles = num + (size - num*x)
        ways += comb(tiles,num)
     
print(int(ways))