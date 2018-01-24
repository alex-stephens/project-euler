# Project Euler
# Problem 65

# Convergents of e

def convergent(start, array):
    if len(array) is 0:
        return start
    a,b = array[-1],1
    for i in range(len(array)-1,-1,-1):
        if i > 0:
            new = array[i-1]
        else:
            new = start
        temp = b
        b = a
        a = new*b + temp
        
    return(a,b)
    
def getArray(n):
    k = 1
    arr = [1] * n
    if n is 0:
        arr = []
    for i in range((n+1)//3):
        arr[3*i + 1] = 2*(i+1)
    return arr

n = 100
string = str(convergent(2,getArray(n-1))[0])
print(sum([int(x) for x in string]))