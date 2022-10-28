# Project Euler
# Problem 35

# Circular primes
    
target = int(1000000)

A = [True] * target
A[:2] = [False, False]

for i in range(2,int(np.sqrt(target)) + 1):
    
    if A[i]:
        for j in range(i**2, target, i):
            A[j] = False
    
primes = [A[i]*i for i in range(len(A))]
for i in range(len(primes)-1,-1,-1):
    if primes[i] == 0:
        primes.pop(i)

def circPermute(n):
    string = str(n)
    return int(string[-1] + string[:-1])

count = 0
for n in primes:
    if n > 2:
        if ('2' in str(n) or '4' in str(n) or '6' in str(n) or '8' in str(n)):
            continue
    
    circular = True
    for perms in range(len(str(n))): 
        if n not in primes:
            circular = False
        n = circPermute(n)
    count += (1 if circular else 0)
print(count)



