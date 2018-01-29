# Project Euler
# Problem 15

# Lattice paths

import numpy as np
from scipy.misc import comb

n = 20

print(int(comb(2*n, n)))
