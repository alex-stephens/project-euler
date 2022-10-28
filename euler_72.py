# Project Euler
# Problem 72

# Counting fractions

import math
import time 

maxD = 1000

f = set()

s = time.time()

for d in range(2,maxD+1):
    
    for n in range(1,d):
        
        if n % 2 == 0 and d % 2 == 0:
            continue
        if n % 3 == 0 and d % 3 == 0:
            continue
        
       
        div = math.gcd(n,d)
        string = '{}/{}'.format(n//div, d//div)
        
        f.add(string)
        
print(len(f))

print('time taken: {:.3f} seconds'.format(time.time()-s))
        