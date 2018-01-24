# Project Euler
# Problem 90

# Cube digit pairs

from itertools import combinations

nums = set([0,1,2,3,4,5,6,7,8,9])
count = 0

for cube1 in combinations(nums,6):
    for cube2 in combinations(nums,6):
                
        if not ((0 in cube1 and 1 in cube2) or (0 in cube2 and 1 in cube1)):
             continue
        elif not ((0 in cube1 and 4 in cube2) or (0 in cube2 and 4 in cube1)):
             continue
        elif not ((0 in cube1 and 9 in cube2) or (0 in cube2 and 9 in cube1) \
                  or (0 in cube1 and 6 in cube2) or (6 in cube1 and 0 in cube2)):
            continue
        elif not ((1 in cube1 and 6 in cube2) or (1 in cube2 and 6 in cube1) \
                  or (1 in cube1 and 9 in cube2) or (1 in cube2 and 9 in cube1)):
            continue
        elif not ((2 in cube1 and 5 in cube2) or (2 in cube2 and 5 in cube1)):
             continue
        elif not ((3 in cube1 and 6 in cube2) or (3 in cube2 and 6 in cube1) \
                  or (3 in cube1 and 9 in cube2) or (3 in cube2 and 9 in cube1)):
            continue
        elif not ((4 in cube1 and 6 in cube2) or (4 in cube2 and 6 in cube1) \
                  or (4 in cube1 and 9 in cube2) or (4 in cube2 and 9 in cube1)):
            continue
        elif not ((6 in cube1 and 4 in cube2) or (6 in cube2 and 4 in cube1) \
                  or (9 in cube1 and 4 in cube2) or (9 in cube2 and 4 in cube1)):
            continue
        elif not ((8 in cube1 and 1 in cube2) or (8 in cube2 and 1 in cube1)):
             continue
        
        count += 1
       
print(ans//2)