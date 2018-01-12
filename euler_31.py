# Project Euler
# Problem 31

# Coin sums

import numpy as np

# Explanation of dynamic programming:
# http://www.algorithmist.com/index.php/Coin_Change

'''
Compute the number of ways of forming change of n cents with the first k coins
'''
def ways(coins, n,k=8):
    table = np.zeros([n+1, k]).astype(int)
    for i in range(n+1):
        for j in range(k):
        
            if i == 0:      # one way to make zero cents
                table[i][j] = 1
                
            elif j == 0:    # one way to make change using all ones 
                table[i][j] = 1

            elif coins[j] > i:
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = table[i,j-1] + table[i-coins[j]][j]
                
    return table[n][k-1]

coins = [1,2,5,10,20,50,100,200] 
n = 200
k = len(coins)
            
print(ways(coins, n,k))
                    