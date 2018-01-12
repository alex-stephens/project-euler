# Project Euler
# Problem 33

# Digit cancelling fractions

import math

numerator = 1
denominator = 1

for b in range(10,100):
    for a in range(10**int(math.log10(b)),b):

        if a == b or (a%10 == 0 and b%10 == 0):
            continue
        
        a_str = str(a)
        b_str = str(b)
        
        for i in range(len(a_str)):
            if a_str[i] in b_str:
                a_reduced = a_str[:i] + a_str[i+1:]
                index = b_str.find(a_str[i])
                b_reduced = b_str[:index] + b_str[index+1:]
                
                
                if a*int(b_reduced) == b*int(a_reduced):
                    print(str(a) + ' / ' + str(b))
                    numerator *= int(a_reduced)
                    denominator *= int(b_reduced)
                    
#print(str(numerator) + ' / ' + str(denominator))
print(denominator // math.gcd(numerator, denominator))
        