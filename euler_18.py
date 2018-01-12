# Project Euler
# Problem 18

# Maximum path sum I

import numpy as np

with open('euler_18.txt') as file:
    lines = file.read().split("\n")

maxSum = []

for i in range(len(lines)):
    currentLine = [int(x) for x in lines[i].split()]
    
    if i == 0:
        maxSum.append(currentLine[0])
        continue
    
    maxSumNew = np.zeros(i+1)
    maxSumNew[0] = currentLine[0] + maxSum[0]
    maxSumNew[i] = currentLine[i] + maxSum[i-1]
    
    for j in range(1,i):
        maxSumNew[j] = np.max([maxSum[j-1],maxSum[j]]) + currentLine[j]
        
    maxSum = maxSumNew
    
print("Maximum path sum: " + str(int(np.max(maxSum))))