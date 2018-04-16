# Project Euler
# Problem 119

# Digit power sum

from math import log

def digitSum(n):
    s = sum(list(map(int, list(str(n)))))
    return s

# returns true if a is a power of b
def power(a,b):
    n = int(log(a-1, b))
    #print(a,b,n)
    if b**n == a or b**(n+1) == a:
        return True
    return False

n = 1
x = 11

while n < 31:
    s = digitSum(x)
    if s == 1:    # powers of 1 don't grow
        pass
    elif s % 2 != x % 2:
        pass
    elif power(x, s):
        n += 1
        print(x)
    x += 1
        

