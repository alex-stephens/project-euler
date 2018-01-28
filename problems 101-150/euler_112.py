# Project Euler
# Problem 112

# Bouncy numbers

def bouncy(n):
    inc, dec = True, True
    digits = [int(a) for a in str(n)]
    for i in range(1,len(digits)):
        inc = False if digits[i] < digits[i-1] else inc
        dec = False if digits[i] > digits[i-1] else dec
        if (not inc) and (not dec):
            return True
    return False

numBouncy = 0
num = 1
percent = 99

while numBouncy * 100 != num * percent:
    num += 1
    numBouncy += 1 if bouncy(num) else 0
    
print(num)