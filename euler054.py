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

def royal_flush(player):
    flush_values = [14,13,12,11,10]
    if sorted(player.values) == sorted(flush_values):
        return len(set(player.suits)) == 1
    return False

def straight_flush(player):
    values = sorted(player.values)
    if range(values[0], values[4] + 1) == values:
        return len(set(player.suits)) == 1
    return False

def four_of_a_kind(player):
    freq = Counter(player.values).most_common()
    return freq[0][1] == 4

def full_house(player):
    freq = Counter(player.values).most_common()
    return freq[0][1] == 3 and freq[1][1] == 2

def flush(player):
    return len(set(player.suits)) == 1

def straight(player):
    values = sorted(player.values)
    return range(values[0], values[4] + 1) == values

def three_of_a_kind(player):
    freq = Counter(player.values).most_common()
    return freq[0][1] == 3

def two_pairs(player):
    freq = Counter(player.values).most_common()
    return (freq[0][1] == 2 and freq[1][1] == 2)

def one_pair(player):
    freq = Counter(player.values).most_common()
    return freq[0][1] == 2

def high_card_on_tie(players):
    freq1 = sorted(players[0].values, reverse=True)
    freq2 = sorted(players[1].values, reverse=True)
    print players[0], freq1
    print players[1], freq2
    for f1, f2 in zip(freq1, freq2):
        if f1 > f2:
            return 0
        elif f1 < f2:
            return 1

def high_card(players):
    freq1 = Counter(players[0].values).most_common()
    freq2 = Counter(players[1].values).most_common()
    print players[0], freq1
    print players[1], freq2
    for f1, f2 in zip(freq1, freq2):
        if f1 > f2:
            return 0
        elif f1 < f2:
            return 1

def evaluate_hand(hand):
    player = namedtuple('player',['values','suits'])
    #separate suits and values
    players = list()
    players.append(player(values=sorted([hand[i][0] for i in range(5)]), suits=[hand[i][1] for i in range(5)]))
    players.append(player(values=sorted([hand[i][0] for i in range(5, 10)]), suits=[hand[i][1] for i in range(5, 10)]))
    old = ['T','J','Q','K','A']
    new = ['10','11','12','13','14']
    table = {}
    for j in range(2):
        for i in range(5):
            for keys, value in zip(old, new):
                if players[j].values[i] == keys:
                    players[j].values[i] = int(value)
            players[j].values[i] = int(players[j].values[i])

    if royal_flush(players[0]) != royal_flush(players[1]):
        return royal_flush(players[1])

    if straight_flush(players[0]) == straight_flush(players[1]) == 1:
        return high_card(players)
    elif straight_flush(players[0]) != straight_flush(players[1]) :
        return straight_flush(players[1])

    if four_of_a_kind(players[0]) == four_of_a_kind(players[1]) == 1:
        return high_card(players)
    elif four_of_a_kind(players[0]) != four_of_a_kind(players[1]):
        return four_of_a_kind(players[1])

    if full_house(players[0]) == full_house(players[1]) == 1:
        return high_card(players)
    elif full_house(players[0]) != full_house(players[1]) :
        return full_house(players[1])

    if flush(players[0]) == flush(players[1]) == 1:
        return high_card(players)
    elif flush(players[0]) != flush(players[1]):
        return flush(players[1])

    if straight(players[0]) == straight(players[1]) == 1:
        return high_card(players)
    elif straight(players[0]) != straight(players[1]):
        return straight(players[1])

    if three_of_a_kind(players[0]) == three_of_a_kind(players[1]) == 1:
        return high_card(players)
    elif three_of_a_kind(players[0]) != three_of_a_kind(players[1]):
        return three_of_a_kind(players[1])

    if two_pairs(players[0]) == two_pairs(players[1]) == 1:
        return high_card(players)
    elif two_pairs(players[0]) != two_pairs(players[1]):
        return two_pairs(players[1])

    if one_pair(players[0]) == one_pair(players[1]) == 1:
        return high_card(players)
    elif one_pair(players[0]) != one_pair(players[1]):
        return one_pair(players[1])

    return high_card_on_tie(players)


hands = []
with open("p054_poker.txt") as file:
    lines = file.readlines()
    for line in lines:
        hands.append(line.split())

count = 0
for hand in hands:
    value =  evaluate_hand(hand)
    count += value
    print value
print len(hands) - count
