# Project Euler
# Problem 166

# Criss cross

def valid():
    s = sum([grid[0][c] for c in range(4)])
    for r in range(4):
        if sum([grid[r][c] for c in range(4)]) != s:
            return False
    for c in range(4):
        if sum([grid[r][c] for r in range(4)]) != s:
            return False
    if sum([grid[i][i] for i in range(4)]) != s:
        return False
    if sum([grid[i][3-i] for i in range(4)]) != s:
        return False

    return True

def dfs():



'''
grid = [[6, 3, 3, 0],
        [5, 0, 4, 3],
        [0, 7, 1, 4],
        [1 ,2, 4, 5]]
'''

grid = [[0 for _ in range(4)] for _ in range(4)]
i = 0





print(valid())
