# Project Euler
# Problem 79

# Passcode derivation


lines = [x.strip() for x in open('euler_79.txt')]

entries = set()
for line in lines:
    for i in range(1,len(line)):
        entries.add(tuple([int(x) for x in line]))

passcode = []
for entry in entries:
    for x in entry:
        passcode.append(x)
  
'''
Checks if passcode is valid with respect to every entry
'''       
def isValid(passcode, entries):
    for entry in entries:
        thisEntry = False
        i = 0
        for j in range(len(passcode)):
            i += 1 if passcode[j] == entry[i] else 0
            if i >= len(entry):
                thisEntry = True
                break
        if thisEntry == False:
            return False
    return True

    
# delete each character that can be deleted while preserving validity
for i in range(len(passcode)-1, -1, -1):
    if isValid(passcode[:i] + passcode[i+1:], entries):
        print(i)
        passcode.pop(i)
        print(passcode)

digits = [x for x in range(0,10) if x in passcode]     
print('-----------------------------------------------')
print('STARTING SWAP OPERATIONS')

for digit in digits:
    indices = [i for i, x in enumerate(passcode) if x == digit]
    firstIndex = -1

    while True:
        firstIndex -= 1
        indices = [i for i, x in enumerate(passcode) if x == digit]
        if firstIndex < -len(indices):
            break
        
        if len(indices) < 2:
            break
        i,j = indices[firstIndex], indices[firstIndex + 1]
        #i = 
        
        # bring first one forward
        valid = True
        while i < j-1:
            passcode[i],passcode[i+1] = passcode[i+1],passcode[i]
            print(passcode)
            valid = isValid(passcode,entries)
            if not valid:
                print('NOT VALID')
                passcode[i],passcode[i+1] = passcode[i+1],passcode[i]
                break
            i += 1
        
        if isValid(passcode[:j] + passcode[j+1:], entries):
            passcode.pop(j)
            print('deleted a ' + str(digit))
        
        # bring second one back
        valid = True
        while j > i+1:
            passcode[j],passcode[j-1] = passcode[j-1],passcode[j]
            print(passcode)
            valid = isValid(passcode,entries)
            if not valid:
                print('NOT VALID')
                passcode[j],passcode[j-1] = passcode[j-1],passcode[j]
                break
            j -= 1

        
        if isValid(passcode[:i] + passcode[i+1:], entries):
            passcode.pop(i)
            print('deleted a ' + str(digit))
        else:
            print('could not delete ' + str(digit))

# do another round of deletions
for i in range(len(passcode)-1, -1, -1):
    if isValid(passcode[:i] + passcode[i+1:], entries):
        print(i)
        passcode.pop(i)
        print(passcode)

        
print('length: ' + str(len(passcode)))     
print(''.join([str(x) for x in passcode]))           

            



