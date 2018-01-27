# Project Euler
# Problem 11

# Largest product in a grid

import numpy as np

matrix = np.loadtxt("euler_11.txt", dtype='i')
print(matrix)

[rows, cols] = np.shape(matrix)
length = 4  # length of product to consider
maxProduct = 0

# horitzontal
for i in range(rows-length):
    for j in range(cols):
        product = np.product(matrix[i:i+length,j])
        maxProduct = product if product > maxProduct else maxProduct

# vertical
for i in range(rows):
    for j in range(cols-length):
        product = np.product(matrix[i,j:j+length])
        maxProduct = product if product > maxProduct else maxProduct

# diagonal (top left - bottom right)
for i in range(rows-length):
     for j in range(cols-length):
        product = np.product([matrix[i][j] for i,j in \
                              zip(range(i,i+length),range(j,j+length))])
        maxProduct = product if product > maxProduct else maxProduct

# diagonal (top right - bottom left)
for i in range(rows-length):
     for j in range(length-1,cols):
        product = np.product([matrix[i][j] for i,j in \
                              zip(range(i,i+length),range(j,j-length,-1))])
        maxProduct = product if product > maxProduct else maxProduct
       
print(maxProduct)
        