# Project Euler
# Problem 78

# Coin partitions

# algorithm: http://www.mathpages.com/home/kmath383.htm

n = 0
target = 1000000

p = [1]
ans = p[0]

while p[-1] % target != 0:
    n += 1
    k = 1
    ans = 0
    while k*(3*k+1)/2 <= n:
        ans += (-1)**(k-1) * p[int(n - k*(3*k+1)/2)]
        k += 1
    k = 1
    while k*(3*k-1)/2 <= n:
        ans += (-1)**(k-1) * p[int(n - k*(3*k-1)/2)]
        k += 1
    
    p.append(ans)
    
print("n = " + str(n))