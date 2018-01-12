# Project Euler
# Problem 52

# Permuted multiples

digits = 0
found = False
mult = 6

while not found:
    digits += 1
    start = 10**(digits-1) 
    cap = 10*start // mult
    
    for n in range(start, cap+1):
        sortedStr = sorted(str(n))
        skip = False
        
        for i in range(2,mult+1):
            if sortedStr != sorted(str(i*n)):
                skip = True
                break
        if skip:
            continue
        
        found = True
        break

print(n)
        
    
    
