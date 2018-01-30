# Project Euler
# Problem 85

# Counting rectangles

'''
Partially brute forced solution, could easily be improved a lot 
'''

x,y,cap = 1,1,1
target = 2 * 10**6
best = target

'''
Explicit formula for the number of rectangles in an a x b grid 
'''
def num(a,b):
    return (a * (a+1) * b * (b+1)) // 4

# Get an initial cap
count = num(1,cap)
while count < target:
    cap += 1
    count = num(1,cap)

for x in range(1,cap):
    for y in range(1,cap):
        count = num(x,y)
        diff = abs(count - target)
        if diff < best:
            best = diff
            area = x*y

print(area)