# Project Euler
# Problem 86

# Cuboid route

from euler import isPerfectSquare
from time import time

'''
Returns the number of cuboid paths of integral length for a max dimension
M x M x M
'''
def paths(M):
    count = 0
    for c in range(3,M+1):
        for ab in range(3,2*c):
            if c % 2 == 1 and ab % 2 == 1:
                continue
            elif isPerfectSquare(ab**2 + c**2):
                if ab < c:
                    count += ab//2
                else:
                    count += c + 1 - (ab+1)//2
    return count

start = time()
target = 10**6
M = 100
cur = paths(M)
inc = 2**10
overshot = False
while inc >= 1 or not overshot:
    if cur < target:
        M += inc
        new = paths(M)
        overshot = True if new > target else False
    elif cur > target:
        M -= inc
        new = paths(M)
        overshot = True if new < target else False
    
    if overshot:
        inc //= 2
    cur = new
M += 1 if new < target else 0
print(M)
print('time taken: ' + str(time() - start) + ' seconds')

     

   