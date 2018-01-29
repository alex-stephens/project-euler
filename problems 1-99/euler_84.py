# Project Euler
# Problem 84

# Monopoly odds

import matplotlib.pyplot as plt
from random import randint
import numpy as np

size = 40
visits = [0] * size

pos = 0
dieSides = 4

CClocs = [2,17,33]
CHlocs = [7,22,36]
Rlocs = [5,15,25,35]
Ulocs = [12,28]

G2J = 30
jail = 10

CCresult = ['0','10','n','n','n','n','n','n','n','n','n','n','n','n','n','n']
CHresult = ['0','10','11','24','39','5','R','R','U','-3', 'n','n','n','n','n','n']
cards = 16

CCcard, CHcard, countDoubles = 0, 0, 0

# Each loop is either a dice roll or a card draw
for _ in range(10**6):
    visits[pos] += 1

    die1 = randint(1,dieSides)
    die2 = randint(1,dieSides)
    
    countDoubles = (countDoubles + 1 if die1 == die2 else 0)

    if countDoubles == 3:   # 3 consecutive doubles = go to jail   
        pos = jail
        countDoubles = 0
        continue
    else:
        pos = (pos + die1 + die2) % size     # advance the player
    
    if pos == G2J:
        pos = jail
        continue
    
    cardstr = 'n'    
    if pos in CClocs:
        CCcard = (CCcard + 1) % cards
        cardstr = CCresult[CCcard]
    elif pos in CHlocs:
        CHcard = (CHcard + 1) % cards
        cardstr = CHresult[CHcard]
            
    # parsing the strings
    if cardstr is 'n':
        continue
    elif cardstr.isdigit():
        pos = int(cardstr)
    elif cardstr is 'R':
        if pos == CHlocs[0]:
            pos = 15
        elif pos == CHlocs[1]:
            pos = 25
        else:
            pos = 5
    elif cardstr is 'U':
        if pos == CHlocs[0] or pos == CHlocs[2]:
            pos = 12
        else:
            pos = 28

    elif cardstr is '-3':
        pos -= 3
        if pos == 33:
            CCcard = (CCcard + 1) % cards
            cardstr = CCresult[CCcard]
            if cardstr is not 'n':
                pos = int(cardstr)

    
plt.bar(range(len(visits)),visits)  # arguments are passed to np.histogram
plt.title("Histogram")
plt.show()
       
# get modal string (top 3)
modal = ''
clone = list(visits)
for _ in range(3):
    index = np.argmax(clone)
    filler = '0' if index < 10 else ''
    modal += filler + str(index)
    clone[index] = 0
    
print(modal)
 
    
    