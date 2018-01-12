# Project Euler
# Problem 29

# Distinct powers
    
numbers = []
cap = 100

for a in range(2,cap+1):
    for b in range(2,cap+1):
        num = a ** b
        if num not in numbers:
            numbers.append(num)

print(len(numbers))
            
        