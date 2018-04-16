# Project Euler
# Problem 62

# Cyclical figurate numbers

import sys
sys.path.append('..')
from euler import isPerfectSquare
from math import sqrt

n = 6

'''
Generates a set of 6 cyclic 4-digit numbers using a single 12-digit number
'''
def generate(n):
    length = len(str(n))//2
    string = str(n)
    
    for i,c in enumerate(string):
        if i % 2 == 1 and c == '0':
            return None
        
    numbers = [0 for _ in range(length)]
    for i in range(length-1):
        numbers[i] = int(string[2*i:2*(i+2)])
    numbers[-1] = int(string[-2:] + string[:2])
        
    return numbers
        
# checks if a number is triangular
def isTri(n):
    if not isPerfectSquare(1+8*n):
        return False
    num = int(sqrt(1 + 8*n))
    if (num + 1) % 2 == 0:
        return True
    return False

# checks if a number is square
def isSquare(n):
    if not isPerfectSquare(n**2):
        return False
    return True

# checks if a number is pentagonal
def isPent(n):
    if not isPerfectSquare(1+24*n):
        return False
    num = int(sqrt(1 + 24*n))
    if (num + 1) % 6 == 0:
        return True
    return False


# checks if a number is hexagonal
def isHex(n):
    if not isPerfectSquare(1+8*n):
        return False
    num = int(sqrt(1 + 8*n))
    if (num + 1) % 4 == 0:
        return True
    return False

# checks if a number is heptagonal
def isHept(n):
    if not isPerfectSquare(9+40*n):
        return False
    num = int(sqrt(9 + 40*n))
    if (num + 3) % 10 == 0:
        return True
    return False

# checks if a number is octagonal
def isOct(n):
    if not isPerfectSquare(4+12*n):
        return False
    num = int(sqrt(4 + 12*n))
    if (num + 4) % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    
    for n in range(1000000, 999999):


