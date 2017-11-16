"""

Question            : 54
Start Time          : 16.11.17 15:15
End Time            : 16.11.17 18:52
Total Time Spent    : 03:37
Complexity          : ~~O(n) lots of small for loops inside
Answer              : 376

"""
from collections import namedtuple
from collections import Counter

def is_royal(player):
    royal_values = [14,13,12,11,10]
    return sorted(player) == sorted(royal_values)

def is_full_house(player):
    freq = Counter(player.values).most_common()
    return freq[0][1] == 3 and freq[1][1] == 2

def is_flush(player):
    return len(set(player.suits)) == 1

def is_straight(player):
    values = sorted(player.values)
    return range(values[0], values[4] + 1) == values

def evaluate_hand(hand):
    player = namedtuple('player',['values','suits'])
    #separate suits and values
    player = player(values=[hand[i][0] for i in range(5)]
                   ,suits=[hand[i][1] for i in range(5)])
    print player
    old = ['T','J','Q','K','A']
    new = ['10','11','12','13','14']
    table = {}
    for i in range(5):
        for keys, value in zip(old, new):
            if player.values[i] == keys:
                player.values[i] = int(value)
        player.values[i] = int(player.values[i])

    royal = is_royal(player)
    straight = is_straight(player)
    flush = is_flush(player)
    frequency = Counter(player.values).most_common()
    sorted_frequency = sorted(frequency, key = lambda x : (-x[1],-x[0])) # sort negatively according to second key
                                                                       # then sort negatively according to first key
    if royal and flush:
        return (9, sorted_frequency)
    elif straight and flush:
        return (8, sorted_frequency)
    elif frequency[0][1] == 4:
        return (7, sorted_frequency)
    elif frequency[0][1] == 3 and frequency[1][1] == 2: #full house
        return (6, sorted_frequency)
    elif flush:
        return (5, sorted_frequency)
    elif straight:
        return (4, sorted_frequency)
    elif frequency[0][1] == 3:
        return (3, sorted_frequency)
    elif frequency[0][1] == 2 and frequency[1][1] == 2:
        return (2, sorted_frequency)
    elif frequency[0][1] == 2:
        return (1, sorted_frequency)
    else:
        return (0, sorted_frequency)


hands = []
with open("p054_poker.txt") as file:
    lines = file.readlines()
    for line in lines:
        hands.append(line.split())

count = 0
for hand in hands:
    player1 =  evaluate_hand(hand[:5])
    player2 =  evaluate_hand(hand[5:])
    if player1[0] > player2[0]:
        count += 1
    elif player1[0] == player2[0]:
        for first, second in zip(player1[1],player2[1]):
            if first > second:
                count += 1
                break
            if first < second:
                break
print count
