# Project Euler
# Problem 74

# Digit factorial chains

from math import factorial

factorials = [factorial(x) for x in range(10)]

def nextInChain(n):
    string = str(n)
    return sum([factorials[int(x)] for x in string])

num = 10**6
chain = [0] * (factorial(9) * 6 + 1)
count = 0
target = 60

for n in range(1,num+1):
    indices = [n]
    length = 1
    x = nextInChain(n)        
    
    while x not in indices:
        if chain[x] != 0:
            length += chain[x]
            break
        length += 1
        indices.append(x)
        x = nextInChain(x)
        
    for i in range(len(indices)):
        chain[indices[i]] = length - i
    count += (1 if length == target else 0)
        
print(count)
    
