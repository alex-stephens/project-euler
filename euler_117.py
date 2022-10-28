# Project Euler
# Problem 117

# Red, green or blue tiles

size = 50
r,g,b,black = 2,3,4,1

ways = [0 for _ in range(size+1)]
ways[0] = 1

for i in range(size+1):
    for j in (r, g, b, black):
        if i >= j:
            ways[i] += ways[i-j]

print(ways[-1])