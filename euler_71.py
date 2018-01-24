# Project Euler
# Problem 71

# Ordered fractions

(x,y) = (3,7)       # target
targetNum = x/y
size = 1000000
minDiff = 1

for b in range(2,size+1):
    if b % y == 0:      # skip exact answers
        continue
    
    a = (b * x) // y
    if targetNum - a/b < minDiff and (a,b) != (x,y):
        minDiff = targetNum - a/b
        (num,denom) = (a,b)
        
print(num)