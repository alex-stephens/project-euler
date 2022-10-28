# Project Euler
# Problem 114

# Counting block combinations I

length = 50
min_size = 3
dp = [0 for _ in range(length+1)]
dp[:min_size] = [1] * min_size

for n in range(min_size, length+1):
    
    dp[n] += dp[n-1] # insert a blank at current position
    
    for r in range(min_size, n+1):
        if n == r:
            dp[n] += dp[n-r]    # no need for a black block before
        else:
            dp[n] += dp[n-r-1]  # red block with a black block before
        
print(dp[length])