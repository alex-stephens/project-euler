# Project Euler
# Problem 89

# Roman numerals

val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
lines = [line.rstrip() for line in open('euler_89.txt')]
req = [0,1,2,3,2,1,2,3,4,2] 
saved = 0

for line in lines:
    # Calculate the represented number
    num = 0
    for i in range(len(line) - 1):
        cur, nex = val[line[i]], val[line[i+1]]
        sign = -1 if cur < nex else 1
        num += sign * cur
    num += nex

    # Count the number of characters in the minimal representation
    minRep = num//1000
    num %= 1000
    for inc in [100, 10,1]:
        minRep += req[num // inc]
        num %= inc
    saved += len(line) - minRep

print(saved)                