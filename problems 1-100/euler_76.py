# Project Euler
# Problem 76

# Counting summations

import numpy as np

'''
Compute the number of ways an integer n can be written as the sum of two or 
more positive integers
'''

def partition(n):
    nums = [x for x in range(1,n+1)]
    k = n-1
    table = np.zeros([n+1, k]).astype(int)
    for i in range(n+1):
        for j in range(k):
        
            if i == 0:      # one way to make zero cents
                table[i][j] = 1
                
            elif j == 0:    # one way to make change using all ones 
                table[i][j] = 1

            elif nums[j] > i:
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = table[i,j-1] + table[i-nums[j]][j]
                
    return table[n][k-1]

n = 100            
print(partition(n))
                    