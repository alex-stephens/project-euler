# Project Euler
# Problem 101

# Optimum polynomial

count = 0

for line in open('euler_102.txt'):
    [x1,y1,x2,y2,x3,y3] = [int(x) for x in line.split(',')]
    xm, ym = (x1+x2)/2, (y1+y2)/2   # mean of points 1 and 2

    # point 3 must be on the opposite side of lines 1 and 2 to the mean
    if (x1*y3 > y1*x3) is (x1*ym > y1*xm):
        continue
    elif (x2*y3 > y2*x3) is (x2*ym > y2*xm):
        continue
    count += 1

print(count)