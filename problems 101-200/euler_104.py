# Project Euler
# Problem 104

# Triangle containment

size = 1000
dp = [0 for _ in range(1000)]
dp[1], dp[2] = 1, 1


def fib(n):
    global dp,size
    # resize x2
    if n >= size:
        dp += [0 for _ in range(size)]
        size *= 2
    
    if n == 0 or dp[n] != 0: return dp[n]
    
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]


n = 540
while True: 
    F = fib(n)
    
    # last digits
    if ''.join(sorted(str(F)[-9:])) == '123456789':
        if ''.join(sorted(str(F)[:9])) == '123456789':
            print(n)
            break
    
    if n % 1000 == 0: print(n)
    n += 1

print(fib(50))
    
    




