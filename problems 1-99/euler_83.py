# Project Euler
# Problem 83

# Path sum: four ways

import numpy as np
from math import inf

matrix = np.loadtxt("euler_83.txt", dtype='i', delimiter=',')
[rows, cols] = np.shape(matrix)

distance = inf*matrix
distance[0][0] = matrix[0][0]
visited = [[False for x in range(rows)] for y in range(cols)]

def adjacent(i,j):
    result = []
    if i > 0: result.append((i-1,j))
    if j > 0: result.append((i,j-1))
    if i < rows-1: result.append((i+1,j))
    if j < cols-1: result.append((i,j+1))
    return result

current = (0,0)
queue, distqueue = [], []

while True:
    (i,j) = current

    # get new nodes
    for x,y in adjacent(i,j):
        distance[x][y] = min(distance[x][y], distance[i][j] + matrix[x][y])
        if not visited[x][y]:# and (x,y) not in queue:
            queue.append((x,y))
            distqueue.append(distance[x][y])
            
    while current in queue:
        index = queue.index(current)
        queue.pop(index)
        distqueue.pop(index)
        
    
    if len(queue) == 0:     # no more nodes to visit
        break

    index = np.argmin(distqueue)   
    current = queue[index]
    visited[i][j] = True  

print(int(distance[-1][-1]))