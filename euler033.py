"""

Question            : 33
Start Time          : 12.11.17 16:38
End Time            : 12.11.17 17:24
Total Time Spent    : 00:46
Complexity          : O(n^2)
Answer              : 100

"""
from math import sqrt
numerator = 1
denominator = 1
for first in range(10, 100):
    for second in range(first + 1, 100):
        digitsFirst = map(int, [i for i in str(first)])
        digitsSecond = map(int, [i for i in str(second)])
        intersection = list(set(digitsFirst) & set(digitsSecond))
        if 0 in intersection:
            intersection.remove(0)
        for val in intersection:
            digitsFirst.remove(val)
            digitsSecond.remove(val)
            if digitsSecond[0] != 0 and digitsFirst[0] / float(digitsSecond[0]) == first / float(second):
                numerator *= first
                denominator *= second
            digitsFirst.append(val)
            digitsSecond.append(val)
i = 2
while i <= numerator:
    while numerator % i == 0 and denominator % i == 0:
        denominator /= i
        numerator /= i
    i += 1
print denominator
