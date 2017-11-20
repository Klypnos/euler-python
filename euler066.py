"""

Question            : 66
Start Time          : 20.11.17 14:30
End Time            : 20.11.17 22.05
Total Time Spent    : Around 4 hours
Complexity          : O(n*m*m) m: average order of convergent num, denom
Answer              : 661

"""
from math import sqrt
from itertools import count
from collections import defaultdict


def continued_fractions(n):
    fractions = defaultdict(lambda: defaultdict(list))
    q = 1
    p = int(sqrt(n))
    frac = list()
    frac.append(p)
    fractions[p][q] = 0
    for i in count(1):
        q = (n - (p * p)) / q
        floor = int((sqrt(n) + p) / float(q))
        p = -1 * (p - (floor * q))
        if fractions[p] and fractions[p][q]:
            return frac
        frac.append(floor)
        fractions[p][q] = i


def convergent_parts(sequence, n):
    while n > len(sequence):
        sequence.extend(sequence[1:])
    denominator = 0
    numerator = 1
    for fraction in reversed(sequence[:n]):
        denominator += numerator * fraction
        denominator, numerator = numerator, denominator
    return (numerator, denominator)


def diophantine(d):
    #x*x-d*y*y=1
    fractions = continued_fractions(d)
    for i in count(1):
        (x, y) = convergent_parts(fractions,i)
        if x*x - d*y*y == 1:
            return x

max_x, max_d = 0, 0
for i in range(1001):
    root = int(sqrt(i))
    if i != root * root:
        result = diophantine(i)
        max_d = i if result > max_x else max_d
        max_x = result if result > max_x else max_x
print max_x, max_d
