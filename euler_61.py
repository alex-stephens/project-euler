from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

for x in range(1,500):
    f = fib(x)

print(f)