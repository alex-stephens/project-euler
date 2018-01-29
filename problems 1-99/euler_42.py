# Project Euler
# Problem 42

# Coded triangle numbers

def triangle(n):
    return (n**2 + n) // 2

def getScore(word):
    #ref = ord('A') - 1
    ref = 64
    return sum([ord(word[i]) - ref for i in range(len(word))])

string = open('euler_42.txt', 'r').read()
words = [x for x in string.split(',')]

# remove quotation marks around each word
words = [words[i][1:-1] for i in range(len(words))]

maxWordLength = 20 # assumed cap for English word length
maxScore = getScore('Z' * maxWordLength)

n = 1
triangularNumbers = []
while triangle(n) <= maxScore:
    triangularNumbers.append(triangle(n))
    n += 1

count = 0

for i in range(len(words)):
    score = getScore(words[i])
    count += (1 if score in triangularNumbers else 0)
    
print(count)
