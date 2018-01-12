# Project Euler
# Problem 32

# Pandigital products

import numpy as np
import math

# RHS must be 4 digits, LHS can be 1 and 4 or 2 and 3
# Notation: m x n = p

products = []

# test 1-100 product with all possibilities that give a 4 digit result
for n in range(1,101):
    
    # check number of digits in n 
    n_digits = int(math.log10(n)) + 1
    m_digits = 5 - digits
    
    m_min = 1000//n + 1
    m_max = 9999//n
    
    for m in range(m_min, m_max + 1):
        
        pandigital = True
        n_string = str(n)
        m_string = str(m)
        p_string = str(m*n)
        
        # slight optimisation - none of the strings can contain a zero
        # there are a lot of small optimisations that could be done but ceebs
        if '0' in (n_string + m_string + p_string):
            continue
                
        fullstring = ''.join(sorted(n_string + m_string + p_string ))
        if fullstring == '123456789':
                if m*n not in products:
                    products.append(m*n)
                print(n_string+ ' x ' +m_string+ ' = ' +p_string) # check results
                
print(sum(products))        
