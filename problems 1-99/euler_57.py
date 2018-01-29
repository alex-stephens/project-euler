# Project Euler
# Problem 57

# Square root convergents

def nextTerm(a, b):
    return [a+2*b, a+b]

[a,b] = [3,2]
count = 0

for _ in range(1000):
    count += (1 if len(str(a)) > len(str(b)) else 0)
    [a,b] = nextTerm(a,b)

print(count)