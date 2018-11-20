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

'''
Returns a list of all squares less than or equal to n
'''

def listSquares(n):
    squares = []
    i = 1
    while i**2 <= n:
        squares.append(i**2)
        i += 1
    return squares

'''
Checks if n is a perfect square
'''
def isPerfectSquare(n):
    x = int(math.sqrt(n))
    sq = x**2
    while sq <= n:
        if sq == n:
            return True
        else:
            x += 1
            sq = x**2
    return False

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


'''
Checks if a number is prime using the AKS primality test algorithm
'''
def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


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
