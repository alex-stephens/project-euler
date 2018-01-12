# Project Euler
# Problem 72

# Counting fractions

''' 
d = 8
1/2, 1/3, 1/4, 1/5, 1/6, 1/7 , 1/8
2/3, 2/4, 2/5, 2/6, 2/7, 2/8
3/4, 3/5, 3/6, 3/7, 3/8
4/5, 4/6, 4/7, 4/8
5/6, 5/7, 5/8
6/7, 6/8
7/8


number of terms (ideal):
(d-1) + (d-2) + ... + 1 = d * (d-1) // 2

'''

d = 10000
termsIdeal = sumToN(d-1) # = d * (d-1) // 2
doubleCounted = 0


print(count)


'''
Computes the sum 1 + 2 + ... + n
'''
def sumToN(n):
    return n*(n+1)//2