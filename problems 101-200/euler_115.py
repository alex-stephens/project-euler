# Project Euler
# Problem 115

# Counting block combinations II

def F(m,n):

    dp = [0 for _ in range(n+1)]
    dp[:m] = [1] * m
    
    for i in range(m, n+1):
        
        dp[i] += dp[i-1] # insert a blank at current position
        
        for r in range(m, i+1):
            if i == r:
                dp[i] += dp[i-r]    # no need for a black block before
            else:
                dp[i] += dp[i-r-1]  # red block with a black block before
            
    return dp[n]

m = 50
target = 1000000
n = m + 1

while F(m,n) < target:
    n += 1
print(n)
    
