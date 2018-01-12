# Project Euler
# Problem 22

# Names scores

strings = open('euler_22.txt', 'r').read()
vals = [x for x in string.split(',')]

# remove quotation marks around each name
vals = [vals[i][1:-1] for i in range(len(vals))]
vals.sort()
ref = ord('A') - 1  # ASCII reference value
score = 0

for i in range(len(vals)):
    posScore = i + 1
    charScore = sum([ord(vals[i][j]) - ref for j in range(len(vals[i]))])
    score += posScore * charScore

print(score)
        