# Project Euler
# Problem 34

# Digit factorials

import math

digits = 1
maxnum = 9
ninefac = math.factorial(9)
while digits * ninefac > maxnum:
    digits += 1
    maxnum += 10*maxnum
maxnum = digits * ninefac

def factorialDigitSum(n):
    return sum([math.factorial(int(i)) for i in str(n)])

result = 0
for n in range(10,maxnum+1):
    result += (n if factorialDigitSum(n) == n else 0)
    
print(result)

# one line madness
#print(sum([(n if factorialDigitSum(n) == n else 0) for n in range(10,maxnum+1)]))
