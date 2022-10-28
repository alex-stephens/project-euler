# Project Euler
# Problem 178

# Step numbers

digits = 40     # 10**40 - 1

# ways[i][n] is the number of ways to reach digit i ending with a value of n
ways = [[0 for _ in range(10)] for _ in range(digits+1)]

for n in range(1,10):
    ways[1][n] = 1
    
for i in range(2,digits+1):
    for n in range(10):
        
        if n > 0:
            ways[i][n] += ways[i-1][n-1]
        if n < 9:
            ways[i][n] += ways[i-1][n+1]
            
print(sum([ways[digits][n] for n in range(10)]))