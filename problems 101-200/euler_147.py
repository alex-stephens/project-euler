# Project Euler
# Problem 147

# Crosshatched rectangles

height, width = 2, 3

ways = 0

# parallel recntangles (sides horizontal or vertical) - O(mn)
for w in range(1,width+1):
    for h in range(1,height+1):
        ways += (width-w+1) * (height-h+1)
print(ways)

minDim = min(width, height)
# iterate through bottom corner locations
for r in range(1, height):
    for c in range(width-1):
        



        newWays = (width - w + 1) * (height - h + 1)
        ways += (width - w + 1) * (height - h + 1)
        print(w, h, newWays)
print(ways)
