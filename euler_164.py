# Project Euler
# Problem 164

# Consecutive digits sum


maxsum = 9
digits = 3
totaldigits = 20
# dp[n][x][d] is the number of ways to get the last d digits
# up to n to sum to x

dp = [[[0 for _ in range(digits+1)] for _ in range(maxsum+1)]
            for _ in range(totaldigits+1)]

# sum of previous 1 digit
for n in range(totaldigits):
    for val in range(0, maxsum-digits+2):
        dp[n][val][1] = 1

# first digit only
for x in range(1,maxsum+1):
    dp[1][x][1] = 1

for d in range(2,digits+1):
    for n in range(1,totaldigits+1):
        for x in range(digits, maxsum+1):
            for i in range(1,x-1):
                dp[n][x][d] += dp[n-1][x-i][d-1]

ans = sum([dp[20][x][2] for x in range(2,3)])
print(dp)


# given a KNOWN string of n digits where 3 consecutive never exceed 9:

# [x1 x2 x3 x4] 