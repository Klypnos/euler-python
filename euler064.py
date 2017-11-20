"""

Question            : 64
Start Time          : 19.11.17 17:20
End Time            : 20.11.17 02:26
Total Time Spent    : 3-4 hours
Complexity          : O(n*k) k: length of fraction until repetition starts
Answer              : 1322

"""
from itertools import count
from math import sqrt
from collections import defaultdict

def continued_fractions(n):
    fractions = defaultdict(lambda: defaultdict(list))
    q = 1
    p = int(sqrt(n))
    fractions[p][q] = 0
    for i in count(1):
        q = (n - (p * p)) / q
        floor = int((sqrt(n) + p) / float(q))
        p = -1 * (p - (floor * q))
        if fractions[p] and fractions[p][q]:
            #print p, q
            return i - fractions[p][q]
        fractions[p][q] = i

num = 10001
squares = [n*n for n in range(num)]
irrationals = list(set(range(1,num)) - set(squares))

counter = 0
for i in irrationals:
    result = continued_fractions(i)
    if result % 2 == 1:
        counter += 1
    #print i, result % 2 == 1
print counter
