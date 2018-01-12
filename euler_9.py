# Project Euler
# Problem 9

# Special Pythagorean triplet

import numpy as np

target = 1000
cap = int(target/2)
 
for a in range(1,cap):
    print(a)
    
    for b in range(a+1,cap):
        
        c2 = a**2 + b**2
        c = int(np.sqrt(c2))+1
        for n in range(1,c):
            perfectSquare = False
            if c2 == n**2:
                c = n
                perfectSquare = True
                break

        #print(a+b+c)
        if perfectSquare and a + b + c == target:
            sol = a*b*c
            break

print(sol)        

    
    
