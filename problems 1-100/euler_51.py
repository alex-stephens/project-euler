# Project Euler
# Problem 51

# Prime digit replacements

import sys
sys.path.append('../')
from euler import listPrimes
from itertools import product

class Pattern(object):
    def __init__(self, string=''):
        self.string = string
        self.numbers = []
        self.count = 0

    def add(self, number):
        self.numbers.append(number)
        self.count += 1

    def __repr__(self):
        return self.string + ': ' + ' '.join(map(str, self.numbers))

num_digits = 6
primes = listPrimes(10**num_digits)
primes = [p for p in primes if len(str(p)) == num_digits]

patterns = {}

def num_to_pattern_string(n, to_replace):
    pattern = list(str(n))
    for i in range(len(pattern)):
        if to_replace[i] == 1:
            pattern[i] = 'X'
    return ''.join(pattern)

def compute_pattern(p, to_replace, digit):
    if to_replace[0] == 1 and digit == 0:
        return
    if sum(to_replace) == 0:
        return

    valid = True
    for i, c in enumerate(str(p)):
        if to_replace[i] == 1 and int(c) != digit:
            valid = False 
            break
    if valid: 
        pattern_string = num_to_pattern_string(p, to_replace)
        if pattern_string not in patterns:
            patterns[pattern_string] = Pattern(pattern_string)

        patterns[pattern_string].add(p)
        

# Replace all instances of 1 with the specified digit
to_replace = list(product(range(2), repeat=num_digits))

for p in primes:
    for d in range(10): 
        for r in to_replace:
            compute_pattern(p, r, d)
 
p, maxval = None, 0

for k in patterns.keys():
    if patterns[k].count > maxval:
        maxval = patterns[k].count
        p = k
        
print(patterns[p].numbers)
print(min(patterns[p].numbers), ',', patterns[p].count)