# Project Euler
# Problem 44

# Pentagonal numbers

def pentagonal(n):
    return (n * (3*n - 1)) // 2

# difference between nth and n+1th pentagonal number
def pentDiff(n):
    return 1 + 3*n

maxVal = 1000
pent = [pentagonal(i) for i in range(1,maxVal+5)]

diffMin = None
for i in range(maxVal):
    for j in range(i,maxVal):
        sumVals = pent[i] + pent[j]
        diffVals = pent[j] - pent[i]
        if sumVals not in pent:
            continue
        elif diffVals not in pent:
            continue
        if diffMin == None:
            diffMin = diffVals
        else:
            diffMin = min(diffMin, diffVals)
            print(i)
            print(j)
            
            
print(diffMin)
