# Project Euler
# Problem 80

# Square root digital expansion

import sys
sys.path.append('..')
from euler import isPerfectSquare

'''
Calculates the sum of the first d digits of sqrt(num)
'''
def sqrtDecimalSum(num, d):
    target = num
    n = 1
    
    for i in range(d):
        while (n+1)**2 < target:
            n += 1
        n *= 10
        target *= 100
    return str(n)

ans =  0

for n in range(1,101):
    if not isPerfectSquare(n):
        ans += sum([int(x) for x in sqrtDecimalSum(n,100)])
print(ans)        
