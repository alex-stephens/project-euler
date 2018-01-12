# Project Euler
# Useful methods

import math

'''
Returns a list of all primes less than or equal to n
'''
def listPrimes(n):
    A = [True] * (n+1)
    A[:2] = [False, False]
    
    for i in range(2,int(math.sqrt(n)) + 1):
        
        if A[i]:
            for j in range(i**2, n+1, i):
                A[j] = False
        
    primes = [i for i in range(len(A)) if A[i] is True]
    return primes

def listSquares(n):
    squares = []
    i = 1
    while i**2 <= n:
        squares.append(i**2)
        i += 1
    return squares


''' 
Computes the maximum sum of a sublist using Kadane's algorithm
'''
def maxSublistSum(array):
    maxSoFar = 0
    maxEndingHere = 0
    
    for n in array:
        maxEndingHere += n
        maxSoFar = max(maxSoFar,maxEndingHere)
        maxEndingHere = max(0,maxEndingHere)
    return maxSoFar

def nextLex(n):
    array = [int(i) for i in str(n)]
    length = len(str(n))
    done = False
    i = len(array) - 1
    while array[i-1] >= array[i]:
        i -= 1
        if i == 0:
            array.sort() # reorder to original array
            done = True
    
    if done:
        return sum([10**(length - 1 - i)*array[i] for i in range(length)])
            
    j = len(array) - 1
    while array[j] <= array[i-1]:
        j -= 1
        if j == i:
            break # maybe not needed
    
    # swap elements i-1 and j
    temp1 = array[i-1]
    temp2 = array[j]
    array.pop(j)
    array.insert(j, temp1)
    array.pop(i-1)
    array.insert(i-1, temp2)
        
    sub = array[i:]
    sub.reverse()
    array[i:] = sub
    return sum([10**(length - 1 - i)*array[i] for i in range(length)])
        
        
        
        
        
        
        
        
        