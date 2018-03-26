# Project Euler
# Problem 173

# Hollow square laminae

def ringSize(n):
    return 4*(n-1)


if __name__ == '__main__':

    tiles = 1000000
    cap = tiles//4 + 1
    #cap -= cap % 2
    rings = 0

    for n in range(cap, 2, -1):
        n_orig = n
        tot = ringSize(n)
        while tot <= tiles:
            rings += 1

            n -= 2
            if n <= 2: break
            tot += ringSize(n)

    print(rings)
