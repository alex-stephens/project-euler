# Project Euler
# Problem 93

# Arithmetic expressions

from itertools import combinations

'''
There are a LOT of better and cleverer ways to do this, but it works...
'''

'''
Input a set of numbers {a,b,c,d}
Returns results of all possible arithmetic expressions made from all four
'''
def expressions(array):
    length = len(array)
    if length == 2:
        a = array[0]
        b = array[1]
        result = pairwise(a,b)
    else:
        result = []
        for (i,j) in combinations(range(length), 2):
            a = array[i]
            b = array[j]
            collapsed = pairwise(a,b)
            others = [array[x] for x in range(len(array)) if (x!=i and x!=j)]
            
            for x in collapsed:
                newTerms = expressions([x] + others)
                result.extend(newTerms)
    result = list(set(result))    
    
    return(result)

'''
Input a pair of number (a,b)
Returns results of all possible pairwise arithmetic (incl. fractional divison)
'''    
def integersOnly(array):
    result = set([]) 
    for x in array:
        if x - int(x) <= 0.001:
            result.add(int(x))
    return result
        
def pairwise(a,b):
    result = set([])
    result.add(a + b)
    result.add(a * b)
    result.add(abs(a - b))
    if a > 0: 
        result.add(b/a)
    if b > 0:
        result.add(a/b)

    return result
 
maxConsecutive = 0
best = None
for digits in combinations(range(10),4):
    targets = set(expressions(digits))
    targets.discard(0)
    targets = integersOnly(targets)    
    
    consecutive = 0
    for i in targets:
        if i != consecutive+1:
            break
        else:
            consecutive += 1
    
    if consecutive > maxConsecutive:
        maxConsecutive = consecutive
        best = digits 

print(best)
print(maxConsecutive)



