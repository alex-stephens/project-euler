# Project Euler
# Problem 100

# Arranged probability

from itertools import product

size = 50
count = 0

for coord in product(range(size+1),repeat=4):
    (x1,y1,x2,y2) = coord
                
    # invalid triangles
    if [x1,y1] == [x2,y2]:                      # coincident points
        continue
    elif [x1,y1] == [0,0] or [x2,y2] == [0,0]:  # point on origin
        continue
    elif [x1,x2] == [0,0] or [y1,y2] == [0,0]:  # degenerate triangle (hor/ver)
        continue
    elif x1 == y1 and x2 == y2:                 # degenerate triangle (diagonal)
        continue
    
    # one edge along x=0, other along y=0
    if min(x1,x2) == 0 and min(y1,y2) == 0:
        count += 1

    # one edge along x=0 or y=0
    elif (x1 == x2 and 0 in [y1,y2]) or (y1 == y2 and 0 in [x1,x2]):
        count += 1
        
    # right angle at 45 degrees to the grid
    elif (x2-x1) * x1 == -(y2-y1) * y1:
        count += 1

    # right angle at 45 degrees to the grid
    elif (x1-x2) * x2 == -(y1-y2) * y2:
        count += 1

print(count//2)
    
''' 
Attempt at direct calculation - conditions for right triangle

- one x=0 and one y=0
- one x=x or one y=y
- [abs(x2-x1),abs(y2-y1)] == m * [abs(y1), abs(x1)]
    
'''

'''
count = 0

count += size * size * 2        # triangles with one edge along x=0 or y=0
count += size * size            # triangles with one edge along x=0, other y=0
count += 2 * (size//2)
tilted = size * (size+1)//2 - 3*size + 3
tilted //= 2

for i in range

count += tilted
print(count)
'''
