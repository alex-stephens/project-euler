# Project Euler
# Problem 121

# Disc game prize fund

from itertools import combinations

turns = 15
num = [x for x in range(2,turns+2)]
requiredWins = turns // 2 + 1
p = 0

for r in range(requiredWins,turns+1):
    for c in combinations(num,r):
        pnew = 1
        for x in num:
            if x in c:
                pnew *= 1/x
            else:
                pnew *= 1 - 1/x
        p += pnew

print(int(1/p))