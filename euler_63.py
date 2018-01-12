# Project Euler
# Problem 63

# Powerful digit counts

digits = 1
lower = (10 ** (digits - 1)) ** (1/digits)
upper = 9 # 10**digits always has one too many digits
count = 0
while lower <= upper:
    count += int(upper - lower + 1)
    digits += 1
    lower = (10 ** (digits - 1)) ** (1/digits)

print(count)