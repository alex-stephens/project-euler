# Project Euler
# Problem 100

# Arranged probability

import math

def main():

    n = 10**12

    while True:
        if n % 10**6 == 0:
            print(f"solving {n}")
        X = n * (n-1)
        b = int((2 + math.sqrt(4 + 8*X)) / 4)

        if 2 * b * (b-1) == X:
            break 
        n += 1 

    print(b)

if __name__ == '__main__':
    main()
    