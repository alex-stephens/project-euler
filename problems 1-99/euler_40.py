# Project Euler
# Problem 40

# Champernowne's constant
    
import numpy as np

def champ(n):
    rem = n
    digits = 1
    advance = 9
    while rem > advance:
        rem -= advance
        digits += 1
        advance = digits * 9 * (10**(digits - 1))
        
    advance = (rem // digits) * digits
    num = 10**(digits - 1) + (rem - 1) // digits
    rem -= advance
    
    return int(str(num)[rem-1])

result = np.product([champ(10**n) for n in range(7)])
print(result)