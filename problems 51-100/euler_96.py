# Project Euler
# Problem 96

# Su Doku

file = open('euler_96_test.txt', 'r')
lines = file.readlines()


for puzzle in range(len(lines)//10):
    grid = [[0 for x in range(9)] for y in range(9)]
    for i in range(0,9):
        for j in range(0,9):
            grid[i][j] = int(lines[i+1][j])
    
print(grid)
    