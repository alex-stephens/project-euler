# Project Euler
# Problem 119

# Digit power sum

from math import log

cap = 100 # maximum digit sum to consider

base = [n for n in range(2,cap+1)]
power = [n for n in base]

'''
Check if a number is a power of its digit sum.
'''
def isPower(n):
    digitsum = sum([int(x) for x in str(n)])
    d = digitsum
    
    if d == 1 or len(str(n)) == 1: 
        return False

    while d < n:
        d *= digitsum
    
    return d == n

ans = set()

for _ in range(10000):
    i = power.index(min(power))

    if power[i] < 10 or power[i] in ans:
        pass
    if isPower(power[i]):
        ans.add(power[i])

    power[i] *= base[i]

a = sorted(list(ans))
print("Found", len(ans), "terms")
print("a30 =", a[29])

