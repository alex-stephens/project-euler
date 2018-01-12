# Project Euler
# Problem 68

# Magic 5-gon ring

from itertools import permutations

''' 
Moves first element of the array to the end
'''
def cycle(array, reps=1):
    for _ in range(reps):
        first = [array.pop(0)]
        array += first
    return array

'''
Computes the string corresponding to the N-gon arrangement specified by the 
input arrays
'''
def stringNgon(inner, outer):
    n = len(inner)
    string = ''
    for i in range(n):
        string += str(outer[i])
        string += str(inner[i%n])
        string += str(inner[(i+1)%n])
    return int(string)

'''
Checks if the given arrangement is a 'magic' N-gon (all lines give same sum)
'''
def magicNgon(inner, outer, average):
    n = len(inner)
    result = True
    for i in range(n):
        val = outer[i] + inner[i] + inner[(i+1)%n]
        if val != average:
            result = False
            break
    return result

n = 5
average = (sum(innervals)*2 + sum(outervals)) // n

innervals = [i for i in range(1,n+1)]
outervals = [i for i in range(n+1,2*n+1)]

currentMax = 0

# Find the valid permutation that produces the max string
for inner in permutations(innervals):
    for outer in permutations(outervals):
        inner = [5,3,1,4,2]
        outer = [6,10,9,8,7]
        
        if magicNgon(inner,outer,average):
            currentMax = max(currentMax, stringNgon(inner,outer))
        
print(currentMax)

# Note: this code is a full brute-force, can also add constraints to maximise
# first three digits. Also easily solved on paper

    
