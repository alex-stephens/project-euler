# Project Euler
# Problem 97

# Large non-Mersenne prime

num = 28433
exp = 7830457
digits = 10
mod = 10**digits

for _ in range(exp):
    num = (num*2)%mod

print(num + 1)