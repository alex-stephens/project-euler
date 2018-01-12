# Project Euler
# Problem 54

# Poker hands

import numpy as np

cardValues = {'2':2 , '3':3, '4':4, '5':5, '6':6, '7':7, \
              '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

handRankings = {'RF':1,'SF':2,'4K':3,'FH':4,'FL':5,'ST':6, '3K':7, '2P':8, \
                '1P':9, 'HK':10}

'''
Returns a list containing all indices at which the specified value occurs in 
the array
'''
def listIndices(array, value):
    indices = []
    for i in range(len(array)):
        if array[i] == value:
            indices.append(i)
    return indices

'''
Takes a string of 5 cards as input and returns the corresponding poker hand, 
with kicker cards listed in descending order separated by spaces
'''
def pokerHand(hand):
    cards = hand.split()
    numbers = sorted([cardValues[cards[i][0]] for i in range(len(cards))])
    suits = sorted([cards[i][1] for i in range(len(cards))])
    
    counts = [0] * (cardValues['A'] + 1)
    for i in numbers:
        counts[i] += 1
    
    # check for straights and flushes
    suitsSame = [(1 if suits[i] == suits[0] else 0) for i in range(len(suits))]
    flush = (True if sum(suitsSame) == 5 else False)
    
    inSequence = [(1 if numbers[i]==numbers[0]+i else 0) for i in range(len(numbers))]
    if numbers[-1] == cardValues['A'] and numbers[0] == cardValues['2']:
        inSequence[-1] = 1
    
    straight = (True if sum(inSequence) == 5 else False) 
    if straight:
        wrapAround = (True if numbers[-1] == cardValues['A'] and \
                numbers[0] == cardValues['2'] else False)

    
    # royal flush and straight flush
    if straight and flush:
        if numbers[0] == cardValues['T']:
            result = 'RF'
        else:
            high = (5 if wrapAround else numbers[-1])
            result = 'SF ' + str(high)
            
    # flush
    elif flush:
        result = 'FL'
        indices = listIndices(counts, 1)
        for i in range(4,-1,-1):
            result += ' ' + str(indices[i])
            
    # straight
    elif straight:
        high = (5 if wrapAround else numbers[-1])
        result = 'ST ' + str(high)

    # four of a kind
    elif max(counts) == 4:
        result = '4K ' + str(counts.index(4)) + ' ' + str(counts.index(1))
        
    # full house
    elif max(counts) == 3 and 2 in counts:
        result = 'FH ' + str(counts.index(3)) + ' ' + str(counts.index(2))
    
    # three of a kind
    elif max(counts) == 3:
        result = '3K ' + str(counts.index(3)) + ' ' 
        indices = listIndices(counts, 1)
        result += str(max(indices)) + ' ' + str(min(indices))
    
    # two pair
    elif max(counts) == 2 and counts.count(2) == 2: 
        indices = listIndices(counts,2)
        kicker = counts.index(1)
        result = '2P ' + str(max(indices)) + ' ' + str(min(indices))
        result += ' ' + str(kicker)
    
    # one pair    
    elif max(counts) == 2:
        result = '1P ' + str(counts.index(2)) + ' ' 
        indices = listIndices(counts,1)
        result += str(indices[2]) + ' ' + str(indices[1]) + ' ' + str(indices[0])
        
    else:
        result = 'HK'
        indices = listIndices(counts,1)
        for i in range(4, -1, -1):
            result += ' ' + str(indices[i])
        
    return result

def compareHands(h1, h2):
    hand1 = pokerHand(h1).split()
    hand2 = pokerHand(h2).split()
    if handRankings[hand1[0]] < handRankings[hand2[0]]:
        return 1
    elif handRankings[hand2[0]] < handRankings[hand1[0]]:
        return 2
    
    else:   # high card tie-breakers
        for i in range(1, len(hand1)):
            if int(hand1[i]) > int(hand2[i]):
                return 1
            elif int(hand2[i]) > int(hand1[i]):
                return 2
    return 0     

player1wins = 0
with open('euler_54.txt') as file:
    for line in file:
        cards = line.split()
        hand1 = ' '.join(cards[:5])
        hand2 = ' '.join(cards[5:])
        player1wins += (1 if compareHands(hand1,hand2) == 1 else 0)
print(player1wins)
        
