# Project Euler
# Problem 113

# Non-bouncy numbers

''' 
Neat combinatoric solution
'''

from scipy.misc import comb
digits = 6
ans = 0
for n in range(1,digits+1):
    ans += comb(n+8, n)     # increasing - start from 1, increase 8 times
    ans += comb(n+9, n)     # decreasing - start from 9, decrease 9 times
    ans -= 10               # duplicates (e.g. 99, 111, etc.)
print(int(ans))


'''
Overcomplicated dynamic programming solution
'''

#inc[m][n] is the number of m-digit numbers starting with a minimum of n that 
#are increasing
inc = [[0 for _ in range(10)] for _ in range(digits)]
# base cases (1 digit)
for x in range(10):
    inc[0][x] = min(10 - x,9) # no leading zeros
# base cases (min value is 9)
for x in range(digits):
    inc[x][9] = 1

for m in range(1,digits):
    for n in range(8, -1, -1):
        if n >= 1:
            inc[m][n] = inc[m][n+1] + inc[m-1][n]
        else:
            inc[m][n] = inc[m][n+1]

# dec[m][n] is the number of m-digit numbers starting with a maximum of n that 
# are decreasing

dec = [[0 for _ in range(10)] for _ in range(digits)]
# base cases (1 digit)
for x in range(10):
    dec[0][x] = x


for m in range(1,digits):
    for n in range(1,10):
        dec[m][n] = dec[m][n-1] + dec[m-1][n] + 1

increasing = sum([inc[x][0] for x in range(digits)])
decreasing = sum([dec[x][-1] for x in range(digits)])
both =  9 * digits
nonbouncy = increasing + decreasing - both
print(nonbouncy)