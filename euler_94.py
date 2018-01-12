# Project Euler
# Problem 94

# Almost equilateral triangles

import numpy as np

squares = []
n = 1
nextSq = n**2
cap = 10**9
while nextSq <= cap:
    squares.append(nextSq)
    n += 1
    nextSq = n**2
    
    
'''
Checks if a triangle with 
'''
def integralArea(a, b):
    