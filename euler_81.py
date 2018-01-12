# Project Euler
# Problem 81

# Path sum: two ways

import numpy as np

matrix = np.loadtxt("euler_81.txt", dtype='i', delimiter=',')

minPathSum = np.zeros(np.shape(matrix)).astype(int)
[rows, cols] = np.shape(matrix)


for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            minPathSum[i][j] = matrix[i][j]
        elif i == 0:
            minPathSum[i][j] = minPathSum[i][j-1] + matrix[i][j]
        elif j == 0:
            minPathSum[i][j] = minPathSum[i-1][j] + matrix[i][j]
        else:
            options = [minPathSum[i-1][j], minPathSum[i][j-1]]
            minPathSum[i][j] = min(options) + matrix[i][j]

print(minPathSum[-1][-1])

'''
# unnecessarily complicated indexing
diagRows = rows + cols - 1

for s in range(diagRows):   # iterate through diagonals of constant s=i+j
    
    num = min([s+1, diagRows - s])
    first = min([s,rows-1])
    last = first - (num - 1)
    
    for i in range(first, last - 1, -1):
        j = s - i
        
        if i == 0 and j == 0:
            minPathSum[i][j] = matrix[i][j]
        elif i == 0:
            minPathSum[i][j] = minPathSum[i][j-1] + matrix[i][j]
        elif j == 0:
            minPathSum[i][j] = minPathSum[i-1][j] + matrix[i][j]
        else:
            options = [minPathSum[i-1][j], minPathSum[i][j-1]]
            minPathSum[i][j] = min(options) + matrix[i][j]

print(minPathSum[-1][-1])
'''

