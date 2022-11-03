# Project Euler
# Problem 164

# Consecutive digits sum

import numpy as np
from itertools import product

"""
dp[n][d1][d2][d3] is the number of solutions
with n digits, ending in d1, d2, d3.
"""


def main():
    N = 20
    limit = 9
    
    dp = np.zeros((N + 1, 10, 10, 10), dtype="int")

    # base case n = 3 with no leading zeros
    for d1 in range(1, 10):
        for d2, d3 in product(range(10), repeat=2):
            if d1 + d2 + d3 <= limit:
                dp[3][d1][d2][d3] = 1

    for n in range(4, N + 1):
        for d2, d3, x in product(range(10), repeat=3):
            if d2 + d3 + x <= limit:
                dp[n][d2][d3][x] += np.sum(dp, axis=1)[n - 1][d2][d3]

    print(np.sum(dp, axis=(1, 2, 3))[N])


if __name__ == "__main__":
    main()
