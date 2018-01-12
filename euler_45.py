# Project Euler
# Problem 45

# Triangular, pentagonal, hexagonal

def triangular(n):
    return (n * (n+1)) // 2

def pentagonal(n):
    return (n * (3*n-1)) // 2
            
def hexagonal(n):
    return n * (2*n-1)

t = 2
p = 2
h = 2
count = 0

while count < 2:
    T = triangular(t)
    P = pentagonal(p)
    H = hexagonal(h)

    if (T == P and T == H):
        count += 1
        print(str(t) + '\t' + str(p) +  '\t' + str(h))

    minimum = min(T,P,H)
    if minimum == T:
        t += 1
    elif minimum == P: 
        p += 1
    else:
        h += 1
        

        


