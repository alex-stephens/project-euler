# Project Euler
# Problem 160

# Factorial trailing digits

import sys
sys.path.append('../')
import euler

primes = euler.listPrimes(100)
print(primes)


def f(N):
    ans = 1
    
    for n in range(1,N+1):
        while n % 10 == 0:
            n //= 10
        ans *= n
        while ans % 10 == 0:
            ans //= 10
        ans %= 1000000
        print(str(n) + '   ' + str(ans))
    
    return ans

print(str(f(20))[-5:])