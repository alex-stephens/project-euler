# Project Euler
# Problem 109

# Darts

from itertools import combinations_with_replacement

mult = {'S':1, 'D':2, 'T':3}

# generate list of scores
score = dict()
score['S25'] = 25
score['D25'] = 50
for n in range(1,21):
    for c in mult:
        hit = c + str(n)
        score[hit] = mult[c] * n

def getScore(seq):
    return sum([score[x] for x in seq])

doubles = {x:score[x] for x in score if x[0] == 'D'}
sequences = []

# Generate all valid sequences ending on a double
for n in range(3):
    for c in combinations_with_replacement(score.keys(), n):
        for d in doubles.keys():
            seq = list(c) + [d]
            
            if getScore(seq) < 100:
                sequences.append(seq)
            
print(len(sequences))