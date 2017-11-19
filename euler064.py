"""

Question            : 64
Start Time          : 19.11.17 17:20
End Time            : 20.11.17 02:26
Total Time Spent    : 3-4 hours
Complexity          :
Answer              :

"""
from itertools import count
from collections import Counter


def repeating_sequence(seq):
    max_len = len(seq) / 2
    sequences = list()
    for i in range(1, max_len + 1):
        sequence = seq[len(seq) - i: len(seq)]
        count = 0
        for j in range(len(seq) - i, 0, -i):
            if sequence == seq[j:j + i]:
                count += 1
            else:
                break
        sequences.append((count, sequence))
    sequences = sorted(sequences, reverse=True)
    if sequences:
        return sequences[0][1]
    return []


def continued_fractions(n):
    for i in iter(count(1)):
        if i * i > n:
            break
    quotient = i - 1
    fractions = [quotient]
    numerator = 1
    denominator = -quotient
    j = 0
    while j < 1024 or not repeating_sequence(fractions):
        old_denom = denominator
        denominator = n - old_denom * old_denom
        quotient = 0
        denominator, numerator = denominator / numerator, numerator / numerator
        numerator = -old_denom
        while numerator * numerator < n:
             numerator -= denominator
             quotient += 1
        numerator += denominator
        quotient -= 1
        fractions.append(quotient)
        #print denominator, numerator, quotient
        denominator, numerator = numerator,  denominator
        j += 1
    return repeating_sequence(fractions)

num = 10000
squares = [n*n for n in range(num)]
irrationals = list(set(range(1,num)) - set(squares))

counter = 0
for i in irrationals:
    result = continued_fractions(i)
    if len(result) % 2 == 1:
        counter += 1

print counter
