# Project Euler
# Problem 82

# Path sum: three ways

import numpy as np

matrix = np.loadtxt("euler_82.txt", dtype='i', delimiter=',')

minPathSum = np.zeros(np.shape(matrix)).astype(int)
[rows, cols] = np.shape(matrix)


for j in range(cols):
    for i in range(rows):
        
        if j == 0:
            minPathSum[i][j] = matrix[i][j]
        else:
            minPathSum[i][j] = minPathSum[i][j-1] + matrix[i][j]
    
    # sweep down
    for i in range(1,rows):
        minPathSum[i][j] = min(minPathSum[i][j], minPathSum[i-1][j] + matrix[i][j])
    # sweep up
    for i in range(rows-2, -1, -1):
        minPathSum[i][j] = min(minPathSum[i][j], minPathSum[i+1][j] + matrix[i][j])

print(min(minPathSum[:,-1]))