# Project Euler
# Problem 71

# Ordered fractions

a = 1
b = 8
target = 2/5

for _ in range(9):
    if a/b > target:
        b -= 1
    elif a/b < target :
        a += 1
    
    print(str(a) + ' / ' + str(b))