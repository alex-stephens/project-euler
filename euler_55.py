# Project Euler
# Problem 55

# Lychrel numbers

def lychrel(n):
    for _ in range(50):
        n = n + int(str(n)[::-1])
        if n == int(str(n)[::-1]): return False
    return True

print(sum([lychrel(n) for n in range(1,10000)]))