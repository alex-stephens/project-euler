# Project Euler
# Problem 62

# Cubic permutations

target = 5
done = False
digits = 2

while not done:

    start = 10 ** (digits - 1)
    cap = 10 * start
    n = int(start ** (1/3))
    
    cubes = []  # cubes with digits sorted
    bases = []  # corresponding bases
    candidates = []
    current = n**3
    while current < cap:
        n += 1
        current = n**3
        sortedDigits = int(''.join(sorted(str(current))))
        cubes.append(sortedDigits)
        bases.append(n)
        
        if cubes.count(sortedDigits) == target:
            done = True
            lowestBase = bases[cubes.index(sortedDigits)]
            candidates.append(lowestBase)
         
        # maybe unnecessary - removes a candidate if exceeded the target     
        elif cubes.count(sortedDigits) == target+1: 
            lowestBase = bases[cubes.index(sortedDigits)]
            candidates.pop(candidates.index(lowestBase)) # remove entry 
    
    if len(candidates) > 0:
        result = candidates[0]**3
        break
    digits += 1
    
print(result)

